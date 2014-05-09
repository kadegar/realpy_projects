#basic web services ex

import gdata.youtube
import gdata.youtube.service
import requests

youtube_service=gdata.youtube.service.YouTubeService()

developer_key ='AIzaSyBrGvwEMv8iLwg2_pP3av1lRCymdXq-J7g'

user=raw_input("Please enter the user ID: ")

url="https://www.googleapis.com/youtube/v3/playlists"
playlist_url=url+"?part=snippet&channelID="+user+"&key="+developer_key

video_feed=requests.get(playlist_url)

print "\nPlaylists for "+str.format(user)+":\n"

for p in video_feed:
	print p
	