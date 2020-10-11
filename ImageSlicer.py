import cv2
import numpy as np

mask = cv2.imread('images\\ScanImage_Matching.png', cv2.IMREAD_COLOR)
src = cv2.imread('images\\ScanImage1.tif', cv2.IMREAD_COLOR)

mask_hsv  = mask # cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
height, width = mask_hsv.shape[:2]
colors_list = {}
print(mask_hsv[0,0])
for x in range(0,height):
    for y in range(0, width):
        key = "{}_{}_{}".format(mask_hsv[x,y][0],mask_hsv[x,y][1],mask_hsv[x,y][2] )
        colors_list[key] = np.array(mask_hsv[x,y])

print(colors_list)
num = 0
for colors1 in colors_list:
    lower_color = colors_list[colors1]
#    lower_color[0] = max(0, lower_color[0] - 1)
#    lower_color[1] = max(0, lower_color[1] - 1)
#    lower_color[2] = max(0, lower_color[2] - 1)
    upper_color = colors_list[colors1]
#    upper_color[0] = min(180, upper_color[0] + 1)
#    upper_color[1] = min(255, upper_color[1] + 1)
#    upper_color[2] = min(255, upper_color[2] + 1)
    img_mask = cv2.inRange(mask, lower_color, upper_color )
    img_result = cv2.bitwise_and(src, src, mask=img_mask)
    num = num + 1
    cv2.imwrite("images\\mask_{}.jpg".format(num), img_mask)
    cv2.imwrite("images\\src_{}.jpg".format(num), img_result)


#for colors in colors_list:
#img_result = cv2.bitwise_and(src, src, mask=img_mask)

#cv2.imshow('img_mask', img_mask)
#cv2.imshow('img_color', img_result)

#cv2.waitKey(0)
#cv2.destroyAllWindows()