#!/usr/bin/env python3

from PIL import Image, ImageDraw
import numpy as np
import os
from pylsd import lsd


fullName = 'house.png'

folder, imgName = os.path.split(fullName)
img = Image.open(fullName)
gray = np.asarray(img.convert('L'))
lines = lsd(gray)
draw = ImageDraw.Draw(img)
for i in range(lines.shape[0]):
    pt0 = (int(line.pt0.x), int(line.pt0.y))
    pt1 = (int(line.pt1.x), int(line.pt1.y))
    width = line.width
    draw.line((pt1, pt2), fill=(0, 0, 255), width=int(np.ceil(width / 2)))
img.save(os.path.join(folder, 'PIL_' + imgName.split('.')[0] + '.jpg'))
