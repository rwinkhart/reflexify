#!/usr/bin/env python3
from os import name
from os.path import expanduser
from pathlib import Path
from requests import get

download_dir = input('download location (full path): ').rstrip('\\').rstrip('/')

# set divider character based on OS
if name == 'nt':
    divider = '\\'
else:
    divider = '/'

if download_dir == '' or download_dir == ' ':
    download_dir = expanduser(f"~{divider}Downloads{divider}reflexTracks")

credentials = input('PHPSESSID cookie: ')
try:
    start = int(input('ID to start downloading from (1): '))
except ValueError:
    start = 1
try:
    stop = int(input('last ID to download (10): '))
except ValueError:
    stop = 10

# set the "PHPSESSID" cookie to log the user in
cookies = {"PHPSESSID": credentials}

# ensure download location exists
Path(download_dir).mkdir(mode=0o700, parents=True, exist_ok=True)

# track download loop
download_id = start
while download_id < stop + 1:
    print(f"\rprogress: {str('{:04d}'.format(download_id))}/{str('{:04d}'.format(stop))}", end='')
    if not Path(download_dir + divider + str('{:04d}'.format(download_id))).is_file():
        response = get(f"https://reflex-central.com/download.php?track_id={str(download_id)}", cookies=cookies)
        with open(download_dir + divider + str('{:04d}'.format(download_id)), "wb") as f:
            f.write(response.content)
    download_id += 1

print('\ntrack download complete')
