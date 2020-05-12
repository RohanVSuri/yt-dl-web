from pytube import YouTube
import os
from os import listdir
class Down():
    def __init__(self, link, title="Video"):
        self.link = link
        self.title= title

    def dl(self):
        yt = YouTube(self.link)
        self.title=yt.title
        yt.streams.filter(file_extension='mp4').first().download(output_path=os.getcwd()+"/app/download", filename=yt.title)
        print("we be downloading" + self.link)

    def clear_folder(self):
        folder_path=os.getcwd()+'/app/download/'
        for file_name in listdir(folder_path):
            os.remove(folder_path + file_name)
