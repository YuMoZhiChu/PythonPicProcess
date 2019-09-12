


















    "Roll an image sideways"
    # 加入简单的噪声
    delta = delta % xsize
    if delta == 0: return image
    image.paste(part1, (xsize-delta, 0, xsize, ysize), mask)
    image.paste(part2, (0, 0, xsize-delta, ysize))
    mask = Image.fromarray(np.uint8(255*(np.random.rand(ysize, delta) > 0.7)))
    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    print(mask)
    return image
    xsize, ysize = image.size
# # gray=img.convert('L')
# # plt.imshow(gray,cmap='gray')
# -*- coding: utf-8 -*-
# box=(0,0,500,500)
# box=(100,100,500,500)
# img.thumbnail((128,128)) 生成一张缩略图
# ljk
# plt.axis('off')
# plt.axis('off')
# plt.figure("beauty")
# plt.figure("test")
# plt.imshow(img)
# plt.imshow(img),plt.axis('off')
# plt.imshow(roi)
# plt.show()
# plt.subplot(1,2,1)
# plt.subplot(1,3,3), plt.title('roi')
# plt.title('origin')
# print(img.size)
# roi.save('../Resource/test1.jpg')
# roi.show()
# roi=img.crop(box)
# roi=img.crop(box)
#img = roll(img, 400)
#img.show()
def roll(image, delta):
from PIL import Image
img = Image.merge("RGB", (b, g, r))
img = Image.open('../Resource/test.jpg')
img.show()
import matplotlib.pyplot as plt
import numpy as np
r, g, b = img.split()