from pytube import YouTube

# * For Checking the video quality

def VideoChecker(link, quality):
    youtubeObject = YouTube(link)
    try:
        youtubeObject.check_availability()
    except:
        return False
    
    streams = youtubeObject.streams.filter(resolution=quality, progressive=True,file_extension='mp4')
    if len(streams) != 0:
        return True
    else:
        return False

# * For downloading a file
        
def Download(link, quality):
    youtubeObject = YouTube(link)
    downloadObject = youtubeObject.streams.filter(resolution=quality, progressive=True,file_extension='mp4')
    downloadObject[0].download(output_path="./out/", filename="video.mp4")

# * Download using a list of links present inside a text file
def myDownload(link, quality):
    youtubeObject = YouTube(link)
    downloadObject = youtubeObject.streams.filter(resolution=quality, progressive=True)
    downloadObject[0].download()

if __name__ == '__main__':
    file = open("links.txt", "r")
    for vid in file:
        print("Downloading ",vid)
        myDownload(vid, "360p")
        print("File downloaded")