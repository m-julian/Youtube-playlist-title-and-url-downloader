from googleapiclient.discovery import build
import os

api_key = input("Enter Google API key: ")   # Enter API Key that you get from website (linked in github description )
youtube = build("youtube", "v3", developerKey=api_key)

def get_playlist_videos(playlist_id):    # gets list with information about the videos
    videos = []
    next_page_token = None
    while True:
        playlist_items = youtube.playlistItems().list(playlistId=playlist_id, part='snippet',  maxResults=50, pageToken=next_page_token).execute()
        videos += playlist_items['items']
        next_page_token = playlist_items.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

user_input = input("Enter playlist ID. This is the letter/numbers after playlist?list= when viewing a Youtube playlist: ")
playlist_videos = get_playlist_videos(user_input)
i = 1
name_output_file = input("Write name of output file. It will be saved in the current working directory.: ")
current_directory = str(os.getcwd())

for video in playlist_videos:  # gets only the titles and urls for the videos in the playlist and saves to file
    print ((f'{i}' + " " + str(video["snippet"]["title"]) + " " + "https://www.youtube.com/watch?v=" + str(video["snippet"]["resourceId"]["videoId"])))
    output_file = open(current_directory + "/" + name_output_file, "a+")
    output_file.write((f'{i}' + " " + str(video["snippet"]["title"]) + " " + "https://www.youtube.com/watch?v=" + str(video["snippet"]["resourceId"]["videoId"])) + "\n")
    i += 1
