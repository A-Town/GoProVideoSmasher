# GoProVideoSmasher
GoPro cameras split up individual video takes when they exceed a certain file size. Using python and ffmpeg, this attempts to combine any split up videos into one video file and sort them accordingly. This is a non-destructive script and so all original files will remain just sorted accordingly. The beauty with this script is that it uses FFMPEG to combine the files. Meaning it doesnt re-render aynthing. Hardware dependent, you can have 10-100's of GB's worth of files combined and sorted in a matter of minutes. For example my Ryzen 7 3800x working on files stored on a NVME (PCIe 3.0) drive was able to combine videos at a >2000fps rate. Storing videos on HDD drives or operating over a network will effect your experience.
 
## Usage
Script is designed around usage in Windows.  
Requirements:
- Python 3
- FFMPEG (in executable form)

## How it works
Script must be placed in folder with all video files looking to be combined and sorted. Script creates a list of all video files it sees within the same directory. From there it creates a batch file containing the command prompt instructions to combine the specific video files in question. Once the batch file is created, the python script executes the batch file and runs FFMPEG accordingly to combine the video files. 
