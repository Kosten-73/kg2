import math
from tkinter import *
from tkinter import ttk
from PIL import Image


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    if mx == mn:
        h = 0
    elif mx == r and g >= b:
        h = (60 * ((g - b) / df) + 0)
    elif mx == r and g < b:
        h = (60 * ((g - b) / df) + 360)
    elif mx == g:
        h = (60 * ((b - r) / df) + 120)
    elif mx == b:
        h = (60 * ((r - g) / df) + 240)

    if mx == 0:
        s = 0
    else:
        s = (1 - mn / mx) * 100
    v = mx * 100
    return round(h), round(s), round(v)

def hsv_to_rgb(hsv_arr):
    h, s, v = hsv_arr[0], hsv_arr[1] / 100, hsv_arr[2] / 100
    i = math.floor(h / 60) % 6
    f = (h / 60) - math.floor(h / 60)
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i)]

    rgb = round(r * 255), round(g * 255), round(b * 255)
    return rgb


def apply_changes():
    h = int(hue_slider.get())
    s = int(saturation_slider.get())
    v = int(value_slider.get())

    for i in range(len(hsv_arr)):
        hsv_arr[i][0] = ((hsv_arr[i][0] + h) % 360)

        hsv_arr[i][1] = max(0, min(100, s + 50))

        new_v = hsv_arr[i][2] + v
        hsv_arr[i][2] = max(0, min(100, new_v))

    new_img = Image.new("RGB", (w, hp))
    cnt = 0
    for x in range(w):
        for y in range(hp):
            new_img.putpixel((x, y), hsv_to_rgb(hsv_arr[cnt]))
            cnt += 1
    new_img.show()


global hsv_arr, w, hp, hue_slider, saturation_slider, value_slider

img = Image.open('picture.jpg')
w, hp = img.size
hsv_arr = []
for x in range(w):
    for y in range(hp):
        r, g, b = img.getpixel((x, y))
        h, s, v = rgb_to_hsv(r, g, b)
        hsv_arr.append([h, s, v])

root = Tk()

frame = Frame(root)
frame.pack(padx=10, pady=10)

hue_label = Label(frame, text="Оттенок (H):")
hue_label.grid(row=0, column=0)
hue_slider = Scale(frame, from_=0, to=360, orient=HORIZONTAL, length=200)
hue_slider.set(0)
hue_slider.grid(row=0, column=1)

saturation_label = Label(frame, text="Насыщенность (S):")
saturation_label.grid(row=1, column=0)
saturation_slider = Scale(frame, from_=-50, to=50, orient=HORIZONTAL, length=200)
saturation_slider.set(0)
saturation_slider.grid(row=1, column=1)

value_label = Label(frame, text="Яркость (V):")
value_label.grid(row=2, column=0)
value_slider = Scale(frame, from_=-50, to=50, orient=HORIZONTAL, length=200)
value_slider.set(0)
value_slider.grid(row=2, column=1)

update_button = Button(frame, text="Обновить", command=apply_changes)
update_button.grid(row=3, columnspan=2)

root.mainloop()


