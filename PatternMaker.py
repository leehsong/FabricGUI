import cv2
import numpy as np
import pickle
import random
import sys
import os
print (sys.argv)

totalpatterns = 16
#defaultsize   = 128
#stepsize = 5
nTrial = 1000
def makepattern(img, mask, index, defaultsize, stepsize, sampling):
    defaultpath = 'images\\patterns\\{}'.format(index)
    print(defaultpath)
    if not os.path.exists(defaultpath):
        os.makedirs(defaultpath)
   ## Start Position Load
    height, width = mask.shape[:2]
    selection_list =np.zeros((height, width))
    count = 0
    for x in range(0, height-defaultsize, stepsize):
        for y in range(0, width-defaultsize, stepsize):
            testmap = mask[x:x+defaultsize, y:y+defaultsize, 2]
            if np.min(testmap) > 254 : ## 255 max
                selection_list[x][y] = 1
                count = count+1
        if divmod(x, 100)[1]==100-stepsize:
            print("Pattern {} process:{} Available Point: {}".format(index, x, count))
    print("Pattern {} Available Point: {}".format(index, count))
    if count > 0:
        positionsX = np.zeros(count)
        positionsY = np.zeros(count)
        cnt = 0
        for x in range(0, height - defaultsize, stepsize):
            for y in range(0, width - defaultsize, stepsize):
                if selection_list[x][y] ==1 :
                    positionsX[cnt]=x
                    positionsY[cnt]=y
                    cnt = cnt + 1
        np.save('images\\selectable_{}X.npy'.format(index), positionsX)
        np.save('images\\selectable_{}Y.npy'.format(index), positionsY)

    minsize = max(defaultsize, 64)
    for i in range(0, sampling) :
        A = random.randrange(0, cnt)
        Xpos = int(positionsX[A])
        Ypos = int(positionsY[A])
        print(Xpos)
        print(Ypos)
        newimg = img[Xpos:Xpos+minsize, Ypos:Ypos+minsize]
        cv2.imwrite('{}//{}.jpg'.format(defaultpath,i), newimg)

if len(sys.argv) >=4:
    default_image = int(sys.argv[1])
    default_size  = int(sys.argv[2])
    default_step  = int(sys.argv[3])
    src = cv2.imread('images\\src_{}.jpg'.format(default_image), cv2.IMREAD_COLOR)
    mask = cv2.imread('images\\mask_{}.jpg'.format(default_image), cv2.IMREAD_COLOR)
    makepattern(src, mask, default_image, default_size, default_step)
else:
    params = [[1,192,5, 100], [3,192,10, 100], [7,192,5,100],  [9,192,5,100], [10,192,5,100], [11,192,5,100]]
#    params = [[8,128,5,100],[12,128,5,100],[13,128,5,100]]
#    params = [[4,32,2,100], [5,32,2, 100], [14,32,2, 100], [15,32,2, 100]]


    for param in params:
#        src = cv2.imread('images\\src_{}.jpg'.format(param[0]), cv2.IMREAD_COLOR)
        src =  cv2.imread('images\\ScanImage1.tif', cv2.IMREAD_COLOR)
        mask = cv2.imread('images\\mask_{}.jpg'.format(param[0]), cv2.IMREAD_COLOR)
        makepattern(src, mask, param[0], param[1], param[2], param[3])
    print( "Need at least 4 argv")




#for i in range(1, totalpatterns):
#    src = cv2.imread('images\\src_{}.jpg'.format(i), cv2.IMREAD_COLOR)
#    mask = cv2.imread('images\\mask_{}.jpg'.format(i), cv2.IMREAD_COLOR)
#    makepattern(src, mask, i)
