#!/usr/bin/env python3
from os import listdir, scandir
from os.path import getsize
from pathlib import Path
from shutil import move, rmtree
from subprocess import run


def type_sort():
    if file.__contains__('_Nat_'):
        _type_folder = 'National/'
        _type_identifier = '_Nat'
    elif file.__contains__('_Sx_'):
        _type_folder = 'Supercross/'
        _type_identifier = '_Sx'
    else:
        _type_folder = 'Free Ride/'
        _type_identifier = ''
    _beta_slot_folder = sorting_dir + _type_folder + file.split('.')[0][-1] + '/' + \
        file_details[0] + ' - ' + file_details[1] + '/'
    Path(_beta_slot_folder).mkdir(mode=0o700, parents=True, exist_ok=True)
    return _beta_slot_folder, _type_identifier


archive_dir = input('archive location (full path): ').rstrip('/') + '/'
sorting_dir = input('target (sorted) directory (full path): ').rstrip('/') + '/'

file_list = sorted(listdir(archive_dir))

# ensure sorting location exists
Path(sorting_dir).mkdir(mode=0o700, parents=True, exist_ok=True)

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
                    beta_slot_folder, type_identifier = type_sort()
                    move(subfolder + '/' + file, beta_slot_folder +
                         f"Beta{type_identifier}_Track_Slot_{file.split('.')[0][-1]}.dx9.{file.split('.')[-1]}")
        files = [f for f in listdir(temp_folder)]
        for file in files:
            if file.endswith('.database') or file.endswith('.level') or file.endswith('.package') or \
                    file.endswith('.scene'):
                beta_slot_folder, type_identifier = type_sort()
                move(temp_folder + '/' + file, beta_slot_folder +
                     f"Beta{type_identifier}_Track_Slot_{file.split('.')[0][-1]}.dx9.{file.split('.')[-1]}")
        rmtree(temp_folder)
