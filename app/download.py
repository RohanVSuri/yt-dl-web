from pytube import YouTube
import os
from os import listdir
import taglib
import time
class Down():
    def __init__(self, link, title = "YouTube", extension = "mp3"):
        self.link = link
        self.yt = YouTube(self.link)
        self.title= self.yt.title.replace(".","")
        self.extension = extension
        self.path = os.getcwd()+"/app/tmp/"
        self.itag = 18
    def get_itag(self):
        if(self.extension=="mp3"):
            self.itag=18
        else:
            self.itag=18

    def dl(self):
        # self.yt.streams.get_by_itag(self.itag).download(filename=self.title)
        # self.yt.streams.get_by_itag(self.itag).download(filename=self.title, output_path=path)
        self.yt.streams.filter(file_extension='mp4').first().download(output_path=self.path, filename=self.title)

    def dl_link(self):
        # return self.yt.streams.filter(file_extension="mp4", only_audio=(self.extension=="mp3")).get_highest_resolution().url
        return self.yt.streams.get_by_itag(self.itag).url

    def convert(self):
        import moviepy.editor as mp
        clip = mp.VideoFileClip(f'app/tmp/{self.title}.mp4')
        clip.audio.write_audiofile(f'app/tmp/{self.title}.mp3')
        clip.close()
    def change_metadata(self, title, artist, album):
        song = taglib.File(f"{self.path}{self.title}.{self.extension}")
        song.tags["ARTIST"] = artist
        song.tags["ALBUM"] = album
        song.tags["TITLE"] = title
        song.save()

    def clear_folder(self):
        for file_name in listdir(self.path):
            os.remove(self.path + file_name)
