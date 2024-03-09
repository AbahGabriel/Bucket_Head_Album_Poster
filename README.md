# BucketHead Album Poster  
Script that checks for new Buckethead albums and makes a post to [r/Buckethead](https://www.reddit.com/r/Buckethead/) when new albums are found.

## Installation
- Install Python. You can download it here https://www.python.org/downloads/ (Add to PATH during the installation).  
- Download the ZIP file of this repo (Click on ```Code``` -> ```Download ZIP```).
- Unzip the ZIP file.
- Open your command prompt and change your directory to that of the unzipped files.  
- Install the required packages  :
  ```
  pip install -U praw requests lxml
  ```
## Configuration
- Create a Reddit App (script) at https://www.reddit.com/prefs/apps/ and get your ```client_id``` and ```client_secret```.  
- Edit the ```config.ini``` file with your details and save:
  ```
  [REDDIT]
  CLIENT_ID = your_client_id
  CLIENT_SECRET = your_client_secret
  PASSWORD = your_reddit_password
  USERNAME = your_reddit_username

  Set to 'Y' for the initial run
  Set to 'N' for every other run
  [VARS]
  POPULATE_DB = Y or N
  ```

## Running the script
Replace 'C:\path\to\the\main.py' with the actual path to the main.py script.  
You can run it as an hourly task (Windows):  
  ```
  schtasks /create /tn BucketHeadAlbumPoster /tr "python C:\path\to\the\main.py" /sc hourly
  ```
