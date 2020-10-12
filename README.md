# toledo-dl

toledo-dl is a Python script for downloading Kaltura videos from Toledo and shortening them using Jumpcutter.

## Installation
- Install youtube-dl: https://github.com/ytdl-org/youtube-dl#installation 
- Install jumpcutter in this directory: https://github.com/Lamaun/jumpcutter#building-without-nix
- Install the cookies.txt browser extension: https://chrome.google.com/webstore/detail/njabckikapfpffapmjgojcnbfjonfjfg

:warning:	There seems to be a problem with the cookies.txt browser extension. As a work-around, you can install the EditThisCookie browser extension http://www.editthiscookie.com/
You should got to the extension options after installing, and change the export format to 'Netscape HTTP Cookie File'.

## Usage 
1. Sign in to Toledo with your student account.
2. Download the cookies in your browser with the cookies.txt browser extension. If you're using the EditThisCookie browser extension, you have to paste the exported cookies in a file called `cookies.txt` in this directory.
3. Create an input file, for example `input.txt` and paste the Toledo urls you want to download from, one url per line. The script will download all the videos from a certain url, so paste the url of the overview page.
4. Run the toledo-dl script as follows:

```
python3 toledo-dl.py [INPUT_FILE]
```

### Extra options
toledo-dl uses the default jumpcutter settings. If you want to change the jumpcutter configuration, you can run 
``` 
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
This script was made to speed up the learning process of individual students