import os

CurrentDir_path = os.getcwd()
DirectoryPath = CurrentDir_path[0] + CurrentDir_path[1]

#list of all files in directory to sort through
filesInDir = []

#list of all goPro files
goPro_files = []

#directory path of new sorted folder
sortedDirectory = CurrentDir_path + "\sorted"

#directory path of multiples folder
multipleFolder = CurrentDir_path + "\multiples"

###Function Area

#function to determine how many parts to a clip there are. Only works on the leading file in the list
def check_Multiples(goProList):
    ClipNumber = goProList[0][4:8]
    ClipCount = 0
    print(ClipNumber)
    for i in range(len(goProList)):
        if goProList[i].find(ClipNumber) >= 0:
            ClipCount += 1
    return ClipCount

def popList(goProList, ClipList):
    run = True
    count = 0
    RemoveList = ClipList
    while (len(RemoveList) > 0):
        if goProList[count] == RemoveList[0]:
            os.replace(CurrentDir_path + "\\" + goProList[count] , multipleFolder + "\\"+ goProList[count])
            del goProList[count]
            del RemoveList[0]
        else:
            count += 1

        if count >= len(goProList):
            run = False

def CreateList(goProList):
    ClipNumber = goProList[0][4:8]
    #List of clips with unique ClipNumber ID
    ClipList = []
    for i in range(len(goProList)):
        if goProList[i].find(ClipNumber) >= 0:
            ClipList.append(goProList[i])
    return ClipList

def createMergedFile(VideoClipList):
#creates text file containing list of files
    with open('video.txt', 'w') as f:
        for i in range(len(VideoClipList)):
         f.writelines(['file \'',VideoClipList[i],'\' \n'])
        
    filename = list(goPro_files[0].replace('.MP4','') + "-merged")
    filename[3] = '0'
    filename = "".join(filename)
    
    with open('ffmpegBatch.bat','w') as batchFile:
        batchFile.writelines([DirectoryPath, '\n'])
        batchFile.writelines([CurrentDir_path, '\n'])
        batchFile.writelines(['ffmpeg -f concat -i video.txt -c copy ', filename, '.mp4'])

    os.system('ffmpegBatch.bat')
    os.remove('ffmpegBatch.bat')
    os.remove('video.txt')
    
def CreateMultipleFolder():
    if not os.path.exists(multipleFolder):
     os.makedirs(multipleFolder)
     #print("Multiples directory Created")
    else:
     print("Directory Exists")

###Main loop execution area

#Create list of all files in directory
for path in os.listdir(CurrentDir_path):
    if os.path.isfile(os.path.join(CurrentDir_path, path)):
        filesInDir.append(path)

#search for GX files, creates list of goPro files only
for i in range(len(filesInDir)):
    if filesInDir[i].find('GX') == 0:
        goPro_files.append(filesInDir[i])

#create Sorted directory
if not os.path.exists(sortedDirectory):
     os.makedirs(sortedDirectory)
     #print("Sorted directory Created")
else:
    print("Directory Exists")

#Check if leading file has multiple clips
while len(goPro_files) > 0:
    if check_Multiples(goPro_files) == 1:
        os.replace(CurrentDir_path + "\\" + goPro_files[0] , sortedDirectory + "\\"+ goPro_files[0])
        print(goPro_files)
        goPro_files.pop(0)
        print(goPro_files)
        print("file moved") 
        
    elif check_Multiples(goPro_files) > 1:
        CreateMultipleFolder()
        goProClipList = CreateList(goPro_files)
        createMergedFile(goProClipList)
        filename = list(goPro_files[0].replace('.MP4','') + "-merged")
        filename[3] = '0'
        filename = "".join(filename)

        os.replace(CurrentDir_path + "\\" + filename + ".mp4", sortedDirectory + "\\" + filename + ".mp4")
        print(goPro_files)
        popList(goPro_files, goProClipList)
        print(goPro_files) 
        print("tempHold")
        goProClipList.clear()
        


print("Done")

