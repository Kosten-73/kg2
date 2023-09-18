import cv2

def on_h_change(value):
    image = cv2.imread('picture.jpg')
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h = value

    image_hsv[:, :, 0] = h

    modified_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Image', modified_image)

    cv2.imwrite('modified_image.jpg', modified_image)


def on_s_change(value):
    image = cv2.imread('picture.jpg')
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    s = value

    image_hsv[:, :, 1] = s

    modified_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Image', modified_image)

    cv2.imwrite('modified_image.jpg', modified_image)


def on_v_change(value):
    image = cv2.imread('picture.jpg')
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    v = value

    image_hsv[:, :, 2] = value

    modified_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Image', modified_image)

    cv2.imwrite('modified_image.jpg', modified_image)


cv2.namedWindow('Image')
cv2.createTrackbar('H', 'Image', 0, 179, on_h_change)
cv2.createTrackbar('S', 'Image', 0, 255, on_s_change)
cv2.createTrackbar('V', 'Image', 0, 255, on_v_change)

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
