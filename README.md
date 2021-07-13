# osu_oszloader
A basic script I use for autoloading in .osz files downloaded to osu!.

# Usage

## GUI
Download osuimport_GUI.py and creds.json

Edit creds.json with a text editor, songs are the /osu/Songs directory and source is the Download directory.

Launch it via python3. (python3 osuimport_GUI.py) It will carry the osz files to the songs folder
at which, the osu app can load it in with a beatmap list refresh.

Hit the "Prefill" key to load the variables in the creds.json file.
Hit "Run" key to start the program.

(Known Issues: The program cannot be stopped via buttons)


## Command Line: 
Download osuimport.py

Edit it with a text editor. Input your osu songs folder and downloads folder in their specific locations.

After that, you can launch it via python3 (through command line: python3 osuimport.py) It will carry the osz files to the songs folder
at which, the osu app can load it in with a beatmap list refresh.



There's a commented out section that makes it work with browsers that write data to the file as it downloads. Active section works for downloading via Firefox/Chrome

I made this because it felt like a hassle to open each osz file.

Use this code at whatever you want. I permit it

