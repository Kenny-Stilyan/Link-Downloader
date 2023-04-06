from pytube import YouTube, Playlist
from main import animation, download_dir
import os

# Download a single video with the highest quality
def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print("Downloading:", yt.title)
    animation()
    stream.download(output_path=download_dir)

# Download a playlist of videos with the highest quality
def download_video_playlist(url):
    pl = Playlist(url)
    print("Downloading Playlist: ", pl.title)
    print("Number of videos in playlist:", len(pl.video_urls))
    for idx, video in enumerate(pl.videos):
        stream = video.streams.get_highest_resolution()
        print("Downloading video {}/{}:".format(idx+1, len(pl.video_urls)), video.title)
        animation()
        stream.download(output_path=download_dir)

# Download only the audio of a video in MP3 format
def download_music(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    print("Downloading:", yt.title)
    animation()
    file_path = stream.download(output_path=download_dir, filename_prefix="")
    # Rename the downloaded file to .mp3
    new_file_path = file_path.replace(".mp4", ".mp3")
    os.rename(file_path, new_file_path)

# Download a playlist of music with the highest quality
def download_music_playlist(url):
    pl = Playlist(url)
    print("Downloading Playlist: ", pl.title)
    print("Number of videos in playlist:", len(pl.video_urls))
    for idx, video in enumerate(pl.videos):
        audio_streams = video.streams.filter(only_audio=True)
        if len(audio_streams) > 0:
            stream = audio_streams.first()
            print("Downloading audio {}/{}:".format(idx+1, len(pl.video_urls)), video.title)
            animation()
            file_path = stream.download(output_path=download_dir, filename_prefix="")
            # Rename the downloaded file to .mp3
            new_file_path = file_path.replace(".mp4", ".mp3")
            os.rename(file_path, new_file_path)

# Allow the user to choose between options
def yt_main():
    print("Choose an option:")
    print("1. Download a single video")
    print("2. Download a video playlist")
    print("3. Download only the audio of a video")
    print("4. Download a music playlist")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        url = input("Enter the video URL: ")
        download_video(url)
    elif choice == 2:
        url = input("Enter the videos playlist URL: ")
        download_video_playlist(url)
    elif choice == 3:
        url = input("Enter the music URL: ")
        download_music(url)
    elif choice == 4:
        url = input("Enter the musics playlist URL: ")
        download_music_playlist(url)
    else:
        print("Invalid choice")
