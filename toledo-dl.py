import hashlib
import os
import pathlib
import re
import subprocess
import sys
import requests


def dl_url(toledo_url):
    # List of (p, entry_id) tuples
    videos = []
    headers = {'Cookie': cookies}

    # Scrape video information from Toledo page
    r = requests.get(url, headers=headers)
    html_content = r.text
    for line in iter(html_content.splitlines()):
        if '<iframe name="KalturaIframe"' in line:
            pattern = '/p/(.+?)/sp/.*?/entry_id/(.*?)/version'
            regex_res = re.search(pattern, line)
            try:
                kaltura_p = regex_res.group(1)
                kaltura_entry_id = regex_res.group(2)
                videos.append((kaltura_p, kaltura_entry_id))
            except:
                print("Regex matching failed on: " + line)

    print('Found {} videos'.format(len(videos)))

    # Make directory for videos
    dir_name = 'toledo-dl-{}'.format(int(hashlib.sha512(toledo_url.encode()).hexdigest(), 16) % 262144)
    dir_path = pathlib.Path(dir_name)
    dir_path.mkdir(exist_ok=True)
    # For some reason cd command doesn't work on Windows. Took it out of the subprocess call.
    os.chdir(dir_path)

    # Download videos using youtube-dl, if there were any videos found on the page
    if len(videos) > 0:
        # Check whether the last argument is an integer. If True only download last n videos of all videos from every link in urls
        if sys.argv[-1].isdigit():
            to_download = int(sys.argv[-1])
            if sys.argv[-2] == "top":
                print('Downloading first {} videos from a total of {} video(s)'.format(to_download, len(videos)))
                idx = 0
                while idx < to_download:
                    print('Downloading video {}/{}'.format(idx + 1, to_download))
                    subprocess.run('youtube-dl -f best kaltura:{}:{}'.format(videos[idx][0],
                                                                             videos[idx][1]),
                                   shell=True)
                    idx += 1
            else:
                print('Downloading last {} videos from a total of {} video(s)'.format(to_download, len(videos)))
                while to_download > 0:
                    print('Downloading video {}/{}'.format(len(videos) - to_download + 1, len(videos)))
                    subprocess.run('youtube-dl -f best kaltura:{}:{}'.format(videos[len(videos) - to_download][0],
                                                                             videos[len(videos) - to_download][1]),
                                   shell=True)
                    to_download -= 1
        else:
            if sys.argv[-1] == "top":
                print("Check if you wanted to download only a certain amount of videos, no amount was specified")
                return
            for idx, video in enumerate(videos):
                print('Downloading video {}/{}'.format(idx + 1, len(videos)))
                subprocess.run('youtube-dl -f best kaltura:{}:{}'.format(video[0], video[1]), shell=True)
    else:
        print("No videos found, check if urls are correct or if cookies are still valid.")

    # Change back to parent folder after downloading all videos in list.
    os.chdir('..')


# Cookies
# Fix cookies.txt
with open('cookies.txt', 'r') as cookies_file:
    cookies = cookies_file.read() \
        .replace("Cookie: ", "") \
        .replace("\n", "") \
        .strip()

# Reading input file
input_file = open(sys.argv[1], 'r')
for url in input_file.readlines():
    dl_url(url)
