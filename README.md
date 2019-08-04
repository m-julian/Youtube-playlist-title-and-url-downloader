# Playlist title and url downloader

Makes a text file that contains title and url of each video in a playlist from Youtube

Required Packages:
google-api-python-client ---> install with pip install --upgrade google-api-python-client

API key is required. --- > Follow Instructions here on how to get one  https://developers.google.com/maps/documentation/javascript/get-api-keyGoogle

How to use:
Run the python script.
1. Program will ask for API key, copy and paste it in.
2. Enter the playlist ID. This is found at the end of the youtube url
Example : https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8
The playlist ID for this youtube playlist is PLE7DDD91010BC51F8
3. Write desired name for output file. Example: output.txt
4. If everything worked correctly, a file with he name output.txt will be saved in the current working directory with the names and urls for every video in the playlist.


Works with Python3.6 and above due to f strings. Works on Linux computers.
