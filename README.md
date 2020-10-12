# toledo-dl

**toledo-dl is a Python script for downloading Kaltura videos from Toledo and shortening them using Jumpcutter.**

It downloads all videos from one or more Toledo pages and automatically runs Jumpcutter on the downloaded files afterwards. Jumpcutter speeds up the silent parts of a video, so you can expect to shorten a lecture by 15-30 minutes. Afterwards, you can of course still watch the video sped up using your favorite video player, since toledo-dl outputs regular .mp4 files.

:warning: As Jumpcutter runs, it saves every frame of the video as an image file in a temporary folder. If your video is long, this could take a LOT of space. It also takes a lot of time, but since this tool is automatic, you can just leave it running in the background.



## Installation
- Install youtube-dl: https://github.com/ytdl-org/youtube-dl#installation 
- Install jumpcutter in this directory: https://github.com/Lamaun/jumpcutter#building-without-nix
- Install the cookies.txt browser extension: https://chrome.google.com/webstore/detail/njabckikapfpffapmjgojcnbfjonfjfg

:warning:	There seems to be a problem with the cookies.txt browser extension. As a work-around, you can install the EditThisCookie browser extension http://www.editthiscookie.com/
You should go to the extension options after installing, and change the export format to 'Netscape HTTP Cookie File'.

## Usage 
1. Create an input file, for example `input.txt` and paste the Toledo urls you want to download from, one url per line. The script will download all the videos from a certain url, so paste the url of the overview page. You can reuse this file multiple times.
---
Do every time:

2. Sign in to Toledo with your student account.
3. Download the cookies in your browser with the cookies.txt browser extension. If you're using the EditThisCookie browser extension, you have to paste the exported cookies in a file called `cookies.txt` in this directory.

4. Run the toledo-dl script as follows:

```
python3 toledo-dl.py [INPUT_FILE]
```
The script will create a new directory per url. This directory will contain the downloaded videos and the sped-up versions. If you re-run the script, it won't download or speed up the videos again, given that you don't change the name of the files/directories. This means you can re-run this script periodically and only process the new videos on the Toledo page. Do keep in mind you have to download your cookies again every time, because they expire quickly.

### Extra options
toledo-dl uses the default Jumpcutter settings. If you want to change the Jumpcutter configuration, you can run 
``` 
cd jumpcutter
python3 jumpcutter.py --help
``` 
to see the list of all available commands and make changes on line 46 of toledo-dl.py

### Example
See `example.txt` for an example of the url file.
```
python3 toledo-dl.py example.txt
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
This script was made to download Toledo videos for personal use only. Don't redistribute the downloaded videos, as they're still the intellectual property of the lecturer/university.