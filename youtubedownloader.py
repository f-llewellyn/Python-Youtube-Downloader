#Imports Required Modules
import os
from pytube import YouTube
import moviepy.editor as mpe

#Saves URL into variable
def getURL():
    while True:
        try:
            global video, videoURL
            videoURL = input("Enter the URL of the video you would like to download: ")
            video = YouTube(videoURL)
            print("")
            print("Video:", video.title)
            break
        except:
            print("")
            print("Sorry, we couldn't find that video")
    
    
# Lists vidoes from best to worse and downloads the desired file
def getVideo():
    global streamList
    streamList = video.streams.filter(video_codec= "vp9").desc().all()
    for i in range(len(streamList)):
        streamList[i]
        print("[", i, "]", streamList[i])
    
    while True:
        try:
            chosenStream = int(input("Which stream would you like to download?"))
            print("")
            print("WARNING: This may take a while depending on your internet connection and the file size")
            print("")
            streamList[chosenStream].download(filename = "video")
            break
        except (ValueError, IndexError):
            print("That stream isn't excepted.")

# Lists audio from best to worse and downloads the desired file
def getAudio():
    global streamList
    streamList = video.streams.filter(only_audio = True).desc().all()
    for i in range(len(streamList)):
        streamList[i]
        print("[", i, "]", streamList[i])

    while True:
        try:
            chosenStream = int(input("Which stream would you like to download?"))
            print("")
            print("WARNING: This may take a while depending on your internet connection and the file size")
            print("")
            streamList[chosenStream].download(filename = "audio")
            break
        except (ValueError, IndexError):
            print("That stream isn't excepted.")

def composite():
    global video
    my_clip = mpe.VideoFileClip("video.webm")
    audio_background = mpe.AudioFileClip("audio.webm")
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(video.title + ".mp4", fps=30)

def cleanup():
    print("Running Cleanup")
    os.remove("video.webm")
    os.remove("audio.webm")
    print("Finished Cleanup")


getURL()
getVideo()
getAudio()
composite()
cleanup()