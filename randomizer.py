#!/usr/bin/env python3
from argparse import ArgumentParser
from os import remove, scandir, symlink
from os.path import exists
from random import choice

# argument parsing
parser = ArgumentParser(description='randomize your beta slot tracks in MX vs. ATV Reflex')
# required
parser.add_argument('database_dir', nargs='+',
                    help='the full path to your MX vs. ATV Reflex database folder')
parser.add_argument('sorted_dir', nargs='+',
                    help='the full path to your sorted Reflex Central archive')
# optional
parser.add_argument('-f', '--favorites', action='store_true',
                    help='only pull tracks from your favorites folder')
args = parser.parse_args()

database_dir = args.database_dir[0].rstrip('/') + '/'
sorted_dir = args.sorted_dir[0].rstrip('/') + '/'

for i in range(1, 9):
    # national
    options = [f.path for f in scandir(sorted_dir + 'National/' + str(i)) if f.is_dir()]
    track = choice(options)
    if exists(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.database"):
        remove(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.database")
    if exists(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.level"):
        remove(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.level")
    if exists(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.package"):
        remove(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.package")
    if exists(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.scene"):
        remove(f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.scene")
    symlink(f"{track}/Beta_Nat_Track_Slot_{str(i)}.dx9.database",
            f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.database")
    symlink(f"{track}/Beta_Nat_Track_Slot_{str(i)}.dx9.level",
            f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.level")
    symlink(f"{track}/Beta_Nat_Track_Slot_{str(i)}.dx9.package",
            f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.package")
    symlink(f"{track}/Beta_Nat_Track_Slot_{str(i)}.dx9.scene",
            f"{database_dir}Beta_Nat_Track_Slot_{str(i)}.dx9.scene")
    # supercross
    options = [f.path for f in scandir(sorted_dir + 'Supercross/' + str(i)) if f.is_dir()]
    track = choice(options)
    if exists(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.database"):
        remove(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.database")
    if exists(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.level"):
        remove(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.level")
    if exists(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.package"):
        remove(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.package")
    if exists(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.scene"):
        remove(f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.scene")
    symlink(f"{track}/Beta_Sx_Track_Slot_{str(i)}.dx9.database",
            f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.database")
    symlink(f"{track}/Beta_Sx_Track_Slot_{str(i)}.dx9.level",
            f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.level")
    symlink(f"{track}/Beta_Sx_Track_Slot_{str(i)}.dx9.package",
            f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.package")
    symlink(f"{track}/Beta_Sx_Track_Slot_{str(i)}.dx9.scene",
            f"{database_dir}Beta_Sx_Track_Slot_{str(i)}.dx9.scene")
    # free ride
    options = [f.path for f in scandir(sorted_dir + 'Free Ride/' + str(i)) if f.is_dir()]
    track = choice(options)
    if exists(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.database"):
        remove(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.database")
    if exists(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.level"):
        remove(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.level")
    if exists(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.package"):
        remove(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.package")
    if exists(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.scene"):
        remove(f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.scene")
    symlink(f"{track}/Beta_Track_Slot_{str(i)}.dx9.database",
            f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.database")
    symlink(f"{track}/Beta_Track_Slot_{str(i)}.dx9.level",
            f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.level")
    symlink(f"{track}/Beta_Track_Slot_{str(i)}.dx9.package",
            f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.package")
    symlink(f"{track}/Beta_Track_Slot_{str(i)}.dx9.scene",
            f"{database_dir}Beta_Track_Slot_{str(i)}.dx9.scene")

