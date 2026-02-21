# GoProVideoSmasher
GoPro cameras split up individual video takes when they exceed a certain file size. Using python and ffmpeg, this attempts to combine any split up videos into one video file and sort them accordingly. This is a non-destructive script and so all original files will remain just sorted accordingly.

## Usage
Script is designed around usage in Windows.  
Requirements:
- Python 3
- FFMPEG (in executable form)

## How it works
Script must be placed in folder with all video files looking to be combined and sorted. Script creates a list of all video files it sees within the same directory. From there it creates a batch file containing the command prompt instructions to combine the specific video files in question. Once the batch file is created, the python script executes the batch file and runs FFMPEG accordingly to combine the video files. 
