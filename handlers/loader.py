from pytube import YouTube
import uuid


def download_video(url):
    yt = YouTube(url)
    video_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_audio=True).first().download(
        "../media/video", f"{video_id}.mp3"
    )
    return f"media/video/{video_id}.mp3"


