from pytube import YouTube
import os
from os import listdir
class Down():
    def __init__(self, link = None, title="Video"):
        self.link = link
        self.yt = YouTube(self.link)
        self.title= self.yt.title

    def dl(self):
        self.yt.streams.filter(file_extension='mp4').first().download(output_path=os.getcwd()+"/app/download", filename=self.title)
        print("we be downloading" + self.link)

    def dl_link(self):
        return self.yt.streams.filter(file_extension='mp4').get_highest_resolution().url

    def clear_folder(self):
        folder_path=os.getcwd()+'/app/download/'
        for file_name in listdir(folder_path):
            os.remove(folder_path + file_name)
