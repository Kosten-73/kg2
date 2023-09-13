import cv2
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
def H():
    image = cv2.imread('pic.jpg')
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    b, g, r = cv2.split(image)

    max_r = np.max(r)
    max_g = np.max(g)
    max_b = np.max(b)

    max_res = max(max_r, max_g, max_b)
    min_res = min(max_r, max_g, max_b)

    for y in range(height):
        for x in range(width):
            pixel_color = image[y, x]
            b, g, r = pixel_color
            loc = 0
            if loc % 3 == 0:
                if (max_r == max_res and g >= b):
                    image_hsv.append(60 * (g - b) / (max_res - min_res))
                if (max_r == max_res and g < b):
                    image_hsv.append(60 * (g - b) / (max_res - max_res) + 360)
                if (max_g == max_res):
                    image_hsv.append(60 * (b - r) / (max_res - max_res) + 120)
                if (max_b == max_res):
                    image_hsv.append(60 * (r - g) / (max_res - max_res) + 240)
            if loc % 3 == 1:
                if (max_res == 0):
                    image_hsv.append(0)
                else:
                    image_hsv.append(1-min_res/max_res)
            if loc % 3 == 2:
                image_hsv.append(max_res)
            loc += 1
    image_hsv.save("test.jpg")


im = Image.open("pic.jpg")
# конвертируем в RGB
im = im.convert("RGB")

# получаем размеры картинок
width, height = im.size

print(H())