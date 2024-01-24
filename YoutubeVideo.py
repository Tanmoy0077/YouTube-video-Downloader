from pytube import YouTube

def VideoChecker(link, quality):
    youtubeObject = YouTube(link)
    streams = youtubeObject.streams.filter(resolution=quality, progressive=True)
    if len(streams) != 0:
        return True
    else:
        return False
    
def Download(link, quality):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(resolution=quality, progressive=True)
    return youtubeObject[0].download()


def log_printer(youtubeObject):
    for i in youtubeObject:
        print(i)
    

if __name__ == '__main__':
    file = open("links.txt", "r")
    for vid in file:
        print("Downloading ",vid)
        Download(vid, "360p")
        print("File downloaded")