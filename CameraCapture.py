# import the opencv library
import cv2
import time
import os.path
from datetime import date
# define a video capture object

import sys
print (sys.argv)

default_scanner = 0
open_windows = 1
if len(sys.argv) >=4:
    default_scanner = int(sys.argv[2])
    root_directory_name = sys.argv[1]
    open_windows = int(sys.argv[3])

print( root_directory_name)
print( default_scanner)
vid = cv2.VideoCapture(default_scanner)

#if ~vid.isOpened():
#    print("No Camera: {}".format(default_scanner))
#    exit(-1)
today = date.today()
today_string = today.strftime("%Y%m%d")
print(today_string)
cnt = 0
fullpath = "{}\Scanner\{}\{}_{}".format(root_directory_name, default_scanner, today_string, cnt)
while os.path.isdir(fullpath):
    cnt = cnt+1
    fullpath = "{}\Scanner\{}\{}_{}".format(root_directory_name, default_scanner, today_string, cnt)

f = open('Scanner{}.dir'.format(default_scanner), 'wt')
f.write(fullpath)
f.close()


os.makedirs(fullpath)
print(fullpath)
date = time.time()
count1 = time.time()
cntframe = 0
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    if  open_windows:
        cv2.imshow('Scanner {}'.format(default_scanner), frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if os.path.isdir('stopframe'):
        break
    nowtime = time.time()

    if nowtime > count1 + 1.0:
        count1 = nowtime
        fullpathname = "{}/{}.jpg".format(fullpath, cntframe)
        cntframe = cntframe+1
        cv2.imwrite(fullpathname, frame)

        print('Image Captured')
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
