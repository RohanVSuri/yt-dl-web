from pytube import YouTube
import os
class Down():
    def __init__(self, link, title="Video"):
        self.link = link
        self.title= title

    def dl(self):
        yt = YouTube(self.link)
        self.title=yt.title
        yt.streams.filter(file_extension='mp4').first().download(output_path=os.getcwd()+"/app")
        print("we be downloading" + self.link)
