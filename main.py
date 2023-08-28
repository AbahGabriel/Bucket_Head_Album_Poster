import requests
from lxml import html
from utilities import config_util, reddit_util, database_util
import time

connection = database_util.connect_to_db()
config = config_util.load_config()
reddit = reddit_util.initialize_reddit(config)

# Represents an Album (obv lol)
class Album():
    def __init__(self, name, link):
        self.name = name
        self.link = link

def main():
    # Get page data
    url = 'https://music.bucketheadpikes.com/'
    response = requests.get(url)
    doc = html.fromstring(response.content)

    # Retrieve albums from html
    albums = doc.xpath(".//div[@class='leftMiddleColumns']//li")
    album_objects = []

    # Only checking the first 25 albums, cuz the artist only releases a maximum of 10 so
    # there's no need to keep track of so many albums at once.
    for album in albums[:25]:
        album_link = f"https://music.bucketheadpikes.com{album.xpath('.//a')[0].get('href')}".strip()
        album_name = album.xpath(".//a//p")[0].text_content().strip()

        album_obj = Album(album_name, album_link)
        album_objects.append(album_obj)

    if config['VARS']['POPULATE_DB'].lower() == 'y':
        populate_db(album_objects)
    
    subreddit = reddit.subreddit("Buckethead")
    if not subreddit.user_is_moderator:
       print(f"You must be a mod in r/Buckethead to run this script.")
       exit()

    # Post the albums that have been recently added to the page.
    for album in album_objects:
        album_record = database_util.retrieve_album(connection, album)
        if album_record:
            continue

        time.sleep(3)
        create_post(subreddit, album)
        database_util.insert_album(connection, album)

    database_util.close_connection(connection)

def populate_db(album_objects):
    # Populates DB with all current releases and exits the program.
    # This is to create an initial database that the program can work with later.
    for album in album_objects:
        database_util.insert_album(connection, album)
    
    exit()
    
def create_post(subreddit, album):
    print("Making post...")

    title = f"New Release - {album.name}"
    body = album.link

    subreddit.submit(
        title=title,
        flair_id='b653ad32-5692-11ea-9f08-0e0657fffd2b',
        url=body
    )

if __name__ == "__main__":
    main()
