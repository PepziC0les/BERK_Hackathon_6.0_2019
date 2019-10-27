import cv2
import numpy as np

def read_file(img: str):
    img_color = cv2.imread(img)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    threshold = 0.99
    fi, wa, ea, wi = 0, 0, 0, 0
    
    guide = cv2.imread("fire.png",0)
    res = cv2.matchTemplate(img_gray, guide, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res>=threshold)
    for pt in zip(*loc[::-1]):
        fi += 1
    
    guide = cv2.imread("water.png",0)
    res = cv2.matchTemplate(img_gray, guide, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res>=threshold)
    for pt in zip(*loc[::-1]):
        wa += 1
    
    guide = cv2.imread("earth.png",0)
    res = cv2.matchTemplate(img_gray, guide, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res>=threshold)
    for pt in zip(*loc[::-1]):
        ea += 1
    
    guide = cv2.imread("wind.png",0)
    res = cv2.matchTemplate(img_gray, guide, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res>=threshold)
    for pt in zip(*loc[::-1]):
        wi += 1
    
    maximum = max(fi, wa, ea, wi)
    if maximum == fi:
        return "fire"
    if maximum == wa:
        return "water"
    if maximum == ea:
        return "earth"
    return "wind"
        