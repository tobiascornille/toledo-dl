import time
from http.cookiejar import MozillaCookieJar
import requests
import re
import subprocess
import pathlib
import hashlib
import sys
import os


def dl_url(url, cj):
  # List of (p, entry_id) tuples
  videos = []

  # Scrape video information from Toledo page
  r = requests.get(url, cookies=cj)
  html_content = r.text
  if ('Kies een instelling' in html_content):
    print('Authentication failed. Please refresh your cookies.')
  for line in iter(html_content.splitlines()):
    if '<iframe name="KalturaIframe"' in line:
      pattern = '/p/(.+)/sp/.*/entry_id/(.*)/version'
      regex_res = re.search(pattern, line)
      try:
        kaltura_p = regex_res.group(1)
        kaltura_entry_id = regex_res.group(2)
        videos.append((kaltura_p, kaltura_entry_id))
      except:
        print("Regex matching failed on: " + line)

  print('Found {} videos'.format(len(videos)))

  # Make directory for videos
  dir_name = 'toledo-dl-{}'.format(int(hashlib.sha512(url.encode()).hexdigest(), 16) % 262144)
  dir_path = pathlib.Path(dir_name)
  dir_path.mkdir(exist_ok=True)

  # Download videos using youtube-dl
  for idx, video in enumerate(videos):
    print('Downloading video {}/{}'.format(idx + 1, len(videos)))
    subprocess.run('cd {}; youtube-dl -f "[protocol=m3u8_native]" kaltura:{}:{} --restrict-filenames'.format(dir_name, video[0], video[1]), shell=True)


def shorten_videos():
  # Shortens videos
  for path in pathlib.Path(".").rglob('*.mp4'):
      video_path = str(path)
      if not video_path.endswith('_ALTERED.mp4') and not pathlib.Path('{}_ALTERED.mp4'.format(video_path[:-4])).is_file():
        print('Shortening video {}'.format(video_path))
        subprocess.run('./jumpcutter.exe --input_file "{}"'.format(video_path), shell=True)


# Cookies
# Fix cookies.txt
with open('cookies.txt', 'r') as original: data = original.read()
# Fix 0 expiry time, see https://stackoverflow.com/questions/14742899/using-cookies-txt-file-with-python-requests
expiry_time = round(time.time() + 14 * 24 * 3600)
data = data.replace('\t0\t', '\t{}\t'.format(expiry_time))
with open('cookies.txt', 'w') as modified:
  if not data.startswith('# Netscape'):
    # Add correct first line, see https://stackoverflow.com/questions/14742899/using-cookies-txt-file-with-python-requests
    modified.write('# Netscape HTTP Cookie File\n' + data)
  else:
    modified.write(data)
# Load cookies from cookies.txt
cj = MozillaCookieJar('cookies.txt')
cj.load(ignore_discard=True)
print('Read {} cookies from cookies.txt'.format(len(cj)))

# Reading input file
with open(sys.argv[1], 'r') as input_file:
  for url in input_file.readlines():
    dl_url(url, cj)
shorten_videos()
