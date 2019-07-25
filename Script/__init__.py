# -*- coding: utf-8 -*-
# ljk

import numpy as np

def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    # 加入简单的噪声
    mask = Image.fromarray(np.uint8(255*(np.random.rand(ysize, delta) > 0.7)))
    print(mask)
    image.paste(part1, (xsize-delta, 0, xsize, ysize), mask)

    return image

from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('../Resource/test.jpg')
# img.thumbnail((128,128)) 生成一张缩略图
#img.show()

#img = roll(img, 400)

r, g, b = img.split()
img = Image.merge("RGB", (b, g, r))

img.show()

# box=(100,100,500,500)
# roi=img.crop(box)
# roi.show()
# roi.save('../Resource/test1.jpg')

# plt.figure("test")
# plt.imshow(img)
# plt.axis('off')

# print(img.size)

# # gray=img.convert('L')
# # plt.imshow(gray,cmap='gray')
# plt.figure("beauty")
# plt.subplot(1,2,1)
# plt.title('origin')
# plt.imshow(img),plt.axis('off')

# box=(0,0,500,500)
# roi=img.crop(box)
# plt.subplot(1,3,3), plt.title('roi')
# plt.imshow(roi)
# plt.axis('off')



# plt.show()

