from pytube import YouTube
import os
from os import listdir
# import taglib
class Down():
    def __init__(self, link, itag, title = "YouTube"):
        self.link = link
        self.yt = YouTube(self.link)
        self.title = self.yt.title.replace(".","")
        # while(self.title=="YouTube"):
        #     print("hi2")
        #     self.yt=YouTube(self.link)
        #     self.title=self.yt.title.replace(".","")
        self.path = os.getcwd()+"/app/tmp/"
        self.itag = itag

    def dl(self):
        self.yt.streams.get_by_itag(self.itag).download(filename=self.title, output_path=path)

    def dl_link(self):
        print(self.yt.streams.get_by_itag(self.itag).url)
        return self.yt.streams.get_by_itag(self.itag).url

    def convert(self):
        import moviepy.editor as mp
        clip = mp.VideoFileClip(f'app/tmp/{self.title}.mp4')
        clip.audio.write_audiofile(f'app/tmp/{self.title}.mp3')
        clip.close()
    # def change_metadata(self, title, artist, album):
    #     song = taglib.File(f"{self.path}{self.title}.mp4") - installing taglib is hard :(
    #     song.tags["ARTIST"] = artist
    #     song.tags["ALBUM"] = album
    #     song.tags["TITLE"] = title
    #     song.save()

    def clear_folder(self):
        for file_name in listdir(self.path):
            os.remove(self.path + file_name)
