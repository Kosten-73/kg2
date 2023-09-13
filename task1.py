from PIL import Image
from matplotlib import pyplot as plt

im = Image.open('picture.jpg')
im2 = Image.open('picture.jpg')
im3 = Image.open('picture.jpg')
pix = im.load()
print(type(pix))
pix1 = im.load()
pix2 = im2.load()
pix_diff = im3.load()

pic_x, pic_y = im.size

arr_im1 = [0] * 256
arr_im2 = [0] * 256

for x in range(pic_x):
    for y in range(pic_y):
        t1 = int(0.299 * pix[x, y][0]) + int(0.587 * pix[x, y][1]) + int(0.114 * pix[x, y][2])
        t2 = int(0.2126 * pix[x, y][0]) + int(0.7152 * pix[x, y][1]) + int(0.0722 * pix[x, y][2])
        t3 = abs(t1 - t2)

        arr_im1[t1] += 1
        arr_im2[t2] += 1

        pix1[x, y] = (t1, t1, t1)
        pix2[x, y] = (t2, t2, t2)
        pix_diff[x, y] = (t3, t3, t3)
im.save('pic_grey1.jpg')
im2.save('pic_grey2.jpg')
im3.save('pic_grey_diff.jpg')

plt.plot(arr_im1, color='orange')
plt.plot(arr_im2, color='green')
plt.show()
