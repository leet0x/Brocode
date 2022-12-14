# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER

import glob

import numpy as np


# Function to rename multiple files
def main():
    folder = "C:\\Users\\User\\Desktop\\test"
    # print(enumerate(os.listdir(folder)))
    # for count, filename in enumerate(os.listdir(folder)):
    #     print(count)
        # print(filename.index("-"))
        # print(filename[:filename.index("-")])

        # dst = f"Hostel {str(count)}.jpg"
        # src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        # dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        # os.rename(src, dst)
    # extract the file names (with file paths)
    # filez = glob.glob("C:\\Users\\User\\Desktop\\test\\*.mp3")
    filez = glob.glob("D:\\Music\\New Testament\\to be analyzed\\2022\\10\\Magic Island Music for balearic people vol. 2\\*.mp3")
    # print(filez)
    # loop through the mp3 files, extracting the track number,
    # then setting the album, albumartist and track number
    # to the appropriate values
    for i in np.arange(0, len(filez)):
        # extract the length of the directory
        length_directory = len(filez[i].split("/"))
        # print(length_directory)
        # extract the track number from the last element of the file path
        tracknum = filez[i].split("\\")[length_directory - 1][0:2]

        # mp3 name (with directory) from filez
        song = filez[i]
        # turn it into an mp3 object using the mutagen library
        mp3file = MP3(song, ID3=EasyID3)
        # set the album name
        # mp3file['album'] = ['Punk-O-Rama Vol. 1 (1994)']
        # set the albumartist name
        mp3file['albumartist'] = ['Punk-O-Rama Vol. 1']
        # set the track number with the proper format
        mp3file['tracknumber'] = str(tracknum) + '/' + str(len(filez))
        # save the changes that we've made
        mp3file.save()


    # Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
