# File Organiser
# Scan a directory, group files by extension, 
# move them into categorised subdirectories (Images/, Documents/, Videos/ etc.), log all operations.

# print(os.getcwd())
# print(os.listdir())

# files = ["sample.txt", "art.png", "cat.mp4", "tune.mp3", "index.html", "server.log"]

import os

# Data and Definitions

txt_files = ["txt", "docx", "json", "log", "pdf"]
image_files = ["png", "jpg", "jpeg", "webp"]
video_files = ["mp4", "ogg"]
music_files = ["mp3"]
programming_files = ["html", "css", "js", "cpp", "py", "c"]
dirNames = ["TextFiles", "Images", "Vids", "Music", "Programming", "main.py"]

def checkDir():
    [os.makedirs(dirName) for dirName in dirNames if (os.path.exists(dirName) == False and fileName != "main.py")]

def replacementChecker(fullName):
    newName = input("Enter a new replacement name for current file: ")
    while(newName == fullName):
        newName = input(f"{fullName} already exists! Enter a new replacement name for current file: ")
    return newName

def checkFileAndMove(fullName):
    fileName = fullName.split(".")[1]
    num = 0
    flag = 0
    for files in [txt_files, image_files, video_files, music_files, programming_files]:
        num += 1
        if fileName in files:
            flag = num
            break
    
    if flag == 0:
        return
    elif os.path.exists(f"{dirNames[flag-1]}/{fullName}"):
        print(f"{fullName} already exists at {dirNames[flag-1]}!")
        newName = replacementChecker(fullName)
        os.rename(f"{fullName}", f"{dirNames[flag-1]}/{newName}.{fileName}")
    else:
        os.rename(f"{fullName}", f"{dirNames[flag-1]}/{fullName}")


# Code

listFiles = [fileName for fileName in os.listdir() if fileName not in dirNames]
checkDir()

for fileName in listFiles:
    checkFileAndMove(fileName)

