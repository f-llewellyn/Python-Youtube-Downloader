#ImportsYouTube module from pytube
from pytube import YouTube

#Imports Playlist module from pytube
from pytube import Playlist

#Saves URL into variable
def getURL():
    global video
    global videoURL
    videoURL = input("Enter the URL of the video you would like to download: ")
    video = YouTube(videoURL)
    print("Video:", video.title)
    
#Lists streams from best to worse
def getStreams():
    global streamList
    streamList = video.streams.filter(progressive = True).desc().all()
    for i in range(len(streamList)):
        streamList[i]
        print("[", i, "]", streamList[i])

#Gets stream for download and downloads it
def streamDownload():
    while True:
        try:
            chosenStream = int(input("Which stream would you like to download?"))
            streamList[chosenStream].download()
            break
        except (ValueError, IndexError):
            print("That stream isn't excepted.")
    print("Dowlnoad Finished.")
   

getURL()
getStreams()
streamDownload()