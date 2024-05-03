import cv2
import glob
import os

for file_path in glob.glob(os.path.join('img', '*.jpg')):
    orig_img = cv2.imread(file_path)
    orig_img = cv2.resize(orig_img, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LINEAR)

    img = orig_img.copy()
    img = cv2.GaussianBlur(img, (9, 9), 5)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        orig_img = cv2.drawContours(orig_img, contours, i, (0, 255, 0), 3)

    cv2.imshow('img', orig_img)
    cv2.waitKey(0)
