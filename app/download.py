from pytube import YouTube
import os
from os import listdir
class Down():
    def __init__(self, link = None, title="Video", extension = "mp3"):
        self.link = link
        self.yt = YouTube(self.link)
        self.title= self.yt.title
        self.extension = extension

    def dl_link(self):
        # return self.yt.streams.filter(file_extension="mp4", only_audio=(self.extension=="mp3")).get_highest_resolution().url
        if(self.extension=="mp3"):
            itag=251
        else:
            itag=18
        return self.yt.streams.get_by_itag(itag).url
