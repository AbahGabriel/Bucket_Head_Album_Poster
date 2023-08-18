import sqlite3
from sqlite3 import Error

def connect_to_db():
    try:
        connection = sqlite3.connect('albums.db')
        connection.execute("""
                    CREATE TABLE IF NOT EXISTS albums (
                        album_name TEXT NOT NULL,
                        album_link TEXT NOT NULL
                    );
                    """)
        
        return connection
    except Error as e:
        print(e)
        raise

def retrieve_album(connection, album):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM albums WHERE album_name = ?", (album.name,))
    
    return cursor.fetchone()

def insert_album(connection, album):
    result = retrieve_album(connection, album)

    if not result:
        connection.execute("INSERT INTO albums (album_name, album_link) VALUES (?, ?)", (album.name, album.link))
        connection.commit()

def close_connection(connection):
    connection.close()