import cv2
import glob
import os

for file_path in glob.glob(os.path.join('img', '*.jpg')):
    orig_img = cv2.imread(file_path)
    orig_img = cv2.resize(orig_img, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LINEAR)

    img = orig_img.copy()
    img = cv2.GaussianBlur(img, (9, 9), 5)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    area_confidence_interval = (2700, 30000)

    coin_count = 0
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area_confidence_interval[0] < area < area_confidence_interval[1]:
            coin_count += 1
            orig_img = cv2.drawContours(orig_img, contours, i, (0, 255, 0), 3)

    orig_img = cv2.putText(orig_img, f'Detected {coin_count} coins',
                           (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (20, 205, 215), 10)
    cv2.imshow('img', orig_img)
    cv2.waitKey(0)
