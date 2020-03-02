#!/usr/bin/env python3
from cv2 import cv2
import numpy as np
import os
from pylsd.lsd import lsd

fullName = 'car.jpg'

folder, imgName = os.path.split(fullName)
src = cv2.imread(fullName, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
lines = lsd(gray)
print(lines[0])
for line in lines:
    pt0 = (int(line.pt0.x), int(line.pt0.y))
    pt1 = (int(line.pt1.x), int(line.pt1.y))
    width = line.width
    cv2.line(src, pt0, pt1, (0, 0, 255), int(np.ceil(width / 2)))
cv2.imwrite(os.path.join(folder, 'cv2_' + imgName.split('.')[0] + '.jpg'), src)
cv2.imshow("lsd_car", src)
cv2.waitKey()
