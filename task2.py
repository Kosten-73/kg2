from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

def bloki(width, height, im):
    mas = []
    for i in range(width):
        for j in range(height):
            # получаем яркость текущего пикселя
            r, g, b = im.getpixel((i, j))
            for now in r, g, b:
                mas.append(now)
    # plt.legend()
    # plt.show()
    return mas


im = Image.open("pic.jpg")
# конвертируем в RGB
im = im.convert("RGB")

# получаем размеры картинок
width, height = im.size

print(bloki(width, height, im))