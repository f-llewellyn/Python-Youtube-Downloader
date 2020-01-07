#ImportsYouTube module from pytube
from pytube import YouTube

#Imports Playlist module from pytube
from pytube import Playlist

resolutions = {
    "1" : "2160p",
    "2" : "1440p",
    "3" : "1080p",
    "4" : "720p",
    "5" : "480p",
    "6" : "360p",
    "7" : "240p",
    "8" : "144p",
    "9" : "Audio Only",
}

#def getGlobals():
#    global streamList
#    global streamFilter
#    global streamFormat
#    global streamOrder
#    global videoURL
#    global video

#Saves URL into variable
def getURL():
    global video
    global videoURL
    videoURL = input("Enter the URL of the video you would like to download: ")
    video = YouTube(videoURL)
    print("Video:", video.title)


def getResolution():
    global resNum
    print("Here's a list of resolutions:")
    print(resolutions)
    resNum = str(input("Please enter the corresponding number to your desired resolution: "))
    
#Lists streams from best to worse
def getStreams():
    global streamList
    if resNum == 9:
        streamList = video.streams.filter(only_audio = True).all()
        print("created list")
    else:
        streamList = video.streams.filter(res = resolutions[resNum]).desc().all()
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
   
# def main():
getURL()
getResolution()
getStreams()
#streamDownload()
#main()

#TO DO:
"""
1) More choice for stream download
        a) List all available streams and let the user choose the desired one --done
        b) Make the stream output dump human readable 
        c) List basic attributes of streams, with option to get more info
        d) Only audio option
        e) Choose download directory
        *f) Clip feature (custom start and end points)

2) Error handling

3) GUI for ease of use
        a) Input box for URL
        b) Downlaod button
        c) Dropdown menu for stream choice
        *d) Progress bar
        *e) details of ongoing tasks for progress bar

*4) In program post processing processing to sew video only and audio only together for full adaptive video
        a) Download both one after the other
        b) Give instructions on how to do out of program
        *c) Sew together in program (VLC library?)

* How the fuck do I do that?

==========================================================================

Downloads video from URL at the highest available quality
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.first().download()

Lists all availabe qualaties
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.all()

Only displays progressive videos
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.filter(progressive = True).all()

Only displays DASH/adaptive videos
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.filter(adaptive = True).all()

Downloads entire playlist at highest progressive quality available
Playlist("Playlist URL").download_all()

Downloads video to specific directory
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.first().download()("/path/to/directory")

Filter for specific needs
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.filter(any of the below).all()

Filters:
only_audio
subtype
progressive
only_video

Filter for specific tag
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.get_by_itag(tag number)

Orders for specific needs
YouTube('https://youtu.be/3n1T3HxHd7Y').streams.filter(progressive=True).order_by('resolution').desc().all()

For more info, go to https://github.com/nficano/pytube
"""