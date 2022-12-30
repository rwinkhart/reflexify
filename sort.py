#!/usr/bin/env python3
from os import listdir, scandir
from os.path import getsize
from pathlib import Path
from shutil import move, rmtree
from subprocess import run

archive_dir = input('archive location (full path): ').rstrip('/') + '/'
sorting_dir = input('target (sorted) directory (full path): ').rstrip('/') + '/'

file_list = sorted(listdir(archive_dir))

# ensure sorting locations exist
[Path(sorting_dir + 'Free Ride/' + str(i)).mkdir(mode=0o700, parents=True, exist_ok=True) for i in range(1, 9)]
[Path(sorting_dir + 'National/' + str(i)).mkdir(mode=0o700, parents=True, exist_ok=True) for i in range(1, 9)]
[Path(sorting_dir + 'Supercross/' + str(i)).mkdir(mode=0o700, parents=True, exist_ok=True) for i in range(1, 9)]

for filename in file_list:
    if getsize(archive_dir + filename) > 4718592:
        file_details = filename.split(' -\x1f- ')
        temp_folder = sorting_dir + '/temp/' + file_details[0] + ' - ' + file_details[1]
        run(['7z', 'x', '-o' + temp_folder, archive_dir + filename])
        sub_folders = [f.path for f in scandir(temp_folder) if f.is_dir()]
        for subfolder in sub_folders:
            sub_files = [f for f in listdir(subfolder)]
            for file in sub_files:
                if file.endswith('.database') or file.endswith('.level') or file.endswith('.package') or \
                        file.endswith('.scene'):
                    beta_slot_folder = sorting_dir + file_details[-1] + '/' + file.split('.')[0][-1] + '/' +\
                        file_details[0] + ' - ' + file_details[1] + '/'
                    Path(beta_slot_folder).mkdir(mode=0o700, parents=True, exist_ok=True)
                    move(subfolder + '/' + file, beta_slot_folder)
        files = [f for f in listdir(temp_folder)]
        for file in files:
            if file.endswith('.database') or file.endswith('.level') or file.endswith('.package') or \
                    file.endswith('.scene'):
                beta_slot_folder = sorting_dir + file_details[-1] + '/' + file.split('.')[0][-1] + '/' + \
                               file_details[0] + ' - ' + file_details[1] + '/'
                Path(beta_slot_folder).mkdir(mode=0o700, parents=True, exist_ok=True)
                move(temp_folder + '/' + file, beta_slot_folder)
        rmtree(temp_folder)
