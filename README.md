# GoProVideoSmasher
GoPro cameras split up individual video takes when they exceed a certain file size. Using python and ffmpeg, this attempts to combine any split up videos into one video file and sort them accordingly. This is a non-destructive script and so all original files will remain just sorted accordingly. The beauty with this script is that it uses FFMPEG to combine the files. Meaning it doesnt re-render aynthing. Hardware dependent, you can have 10-100's of GB's worth of files combined and sorted in a matter of minutes. For example my Ryzen 7 3800x working on files stored on a NVME (PCIe 3.0) drive was able to combine videos at a ~>10000fps rate. Storing videos on HDD drives or operating over a network will effect your experience.

Tested on:
- GoPro Hero 8
- GoPro Hero 11
 
## Usage
Script is designed to be used in Windows. Could be developed to also work in linux but havent gotten around to it.    
Requirements:
- Python 3
- FFMPEG (in executable form. Can be found at [FFMPEG](https://www.ffmpeg.org/download.html))

Place the phython script and ffmpeg.exe file into the base folder with all your videos needing to be sorted and combined. Using command prompt, navigate to this folder (easiest way on win10/11 is to right click in the folder and select "Open in Terminal".<br/> From there you can type "python VideoSorter.py". The script will execute and sort the files accordingly. Video takes that produce one file will get placed into the "sorted" folder. Combined videos will have the segment identifier stripped from the file name and left with the unique take ID. "-merged" will also be added to the end of this filename and the video will be placed into the "sorted" folder. The multiple segmented files will be placed into "multiples" in the event something happens to the combined video or further work is required. 

