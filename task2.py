from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
plt.figure(num='График 2 задания')
def bloki(width, height, im):
    r_m = [0] * 256
    g_m = [0] * 256
    b_m = [0] * 256
    for i in range(width):
        for j in range(height):
            # получаем яркость текущего пикселя
            r, g, b = im.getpixel((i, j))
            loc = 0
            for now in r, g, b:
                if loc == 0:
                    r_m[now] += 1
                if loc == 1:
                    g_m[now] += 1
                if loc == 2:
                    b_m[now] += 1
                loc += 1

    plt.plot(r_m, color='red', label='R')
    plt.plot(g_m, color='green', label='G')
    plt.plot(b_m, color='blue', label='B')
    plt.xlabel("оттенок")
    plt.ylabel("количество")
    plt.legend()
    plt.show()




im = Image.open("pic.jpg")
# конвертируем в RGB
im = im.convert("RGB")

# получаем размеры картинок
width, height = im.size

bloki(width, height, im)
