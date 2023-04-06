from youtube import *
from pathlib import Path
import time
import sys
import os


''''
Todo:
4 Add check for invalid URL
5 Turn in into desktop applications
6 Convert the code to .exe
7 Step by step guide (Readme - github)
'''

download_dir = str(Path.home() / "Downloads" / "Link Downloader")
os.makedirs(download_dir, exist_ok=True)

# Custom download animation
def animation():
    chars = "/—\|" # animation characters
    for i in range(101):
        time.sleep(0.1)
        sys.stdout.write(f"\rDownloading... [{chars[i % 4]}] {i}%")
        sys.stdout.flush()
    sys.stdout.write("\rDownload complete!          \n")

if __name__ == "__main__":
    yt_main()

