from pytube import YouTube
import os

def download_video(url,name):
    try:
        yt =YouTube(url)
        yt.set_filename(name)
        curr_dir=os.path.dirname(os.path.abspath(__file__))
        video=yt.filter('mp4')[-1]
        video.download(curr_dir)
        return True
    except:
        return False