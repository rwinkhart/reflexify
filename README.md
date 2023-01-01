# reflexify
Tools for downloading and managing custom tracks for MX vs. ATV Reflex on UNIX-like systems.

Think of it like creating a local Spotify for MX vs. ATV Reflex custom tracks.

This is a small project I made to solve a problem I was having. I understand that making mod tools for a Windows game that only work on UNIX-like systems seems sort of silly.

Do not expect this to be updated in any way unless a Python update breaks it.

# Installation and Usage
Either clone the repository or just download and place the three Python scripts (scrape.py, sort.py, randomize.py) in your intended installation directory.

scrape.py - Interactive script for archiving ALL tracks from [Reflex Central](https://reflex-central.com/), will ask for a "PHPSESSID" - the value of this can be found by logging into [Reflex Central](https://reflex-central.com/) and using inspect element to find your PHPSESSID cookie.

sort.py - Interactive script for sorting your [Reflex Central](https://reflex-central.com/) archive and preparing it to be used by randomize.py.

randomize.py - Non-interactive script that requires two arguments: database_dir (the location of your MX vs. ATV Reflex database folder), sorted_dir (the location of your sorted archive).

This script will randomly fill all of your beta slots with tracks from the provided sorted archive.

Optionally, you can create separate folders in the format of the sorted archive to create playlists, favorites lists, etc.

Additionally, I recommend creating an alias, such as: 

alias reflexify='/path/to/randomize.py "/path/to/MX vs ATV Reflex/Database/" "/path/to/sorted/archive"'