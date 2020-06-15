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
        # return self.yt.streams.filter(only_audio=False).url
        if(self.extension=="mp3"):
            itag=251
        else:
            itag=313
        return self.yt.streams.get_by_itag(itag).url

    def dl(self):
        self.yt.streams.filter(file_extension='mp4').first().download(output_path=os.getcwd()+"/app/download", filename=self.title)
        print("we be downloading" + self.link)



    def clear_folder(self):
        folder_path=os.getcwd()+'/app/download/'
        for file_name in listdir(folder_path):
            os.remove(folder_path + file_name)
