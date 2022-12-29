#!/usr/bin/env python3
from os import listdir
from os.path import expanduser
from pathlib import Path

# external dependencies
from requests import get

download_dir = input('download location (full path): ').rstrip('\\').rstrip('/')

if download_dir == '' or download_dir == ' ':
    download_dir = expanduser('~/Downloads/reflexTracks')

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

# create database of pre-existing files
file_list, file_list_ids = sorted(listdir(download_dir)), []
for file in file_list:
    file_list_ids.append(file[:4])

# track download loop
download_id = start
while download_id < stop + 1:
    print(f"\rprogress: {str('{:04d}'.format(download_id))}/{str('{:04d}'.format(stop))}", end='')
    if str('{:04d}'.format(download_id)) not in file_list_ids:
        skip = False
        response = get(f"https://reflex-central.com/download.php?track_id={str(download_id)}", cookies=cookies)
        try:
            html = get(f"https://reflex-central.com/track_profile.php?track_id={str(download_id)}").text.split('\n')
            track_name = html[71].split('b>')[1][:-3].strip()
            track_type = html[95].replace('		</font>', '').strip()
        except IndexError:
            track_name, track_type, skip = '', '', True
        if not skip:
            with open(f"{download_dir}/{str('{:04d}'.format(download_id))} -\x1f- {track_name} -\x1f- "
                      f"{track_type}", "wb") as f:
                f.write(response.content)
    download_id += 1

print('\n\ntrack download complete')
