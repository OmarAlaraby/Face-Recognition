'''
P+ = (Pt * P)^-1 * Pt
W = T * P+

'''
import cv2
from PIL import Image, ImageTk
import numpy as np
from utilities import resize_image

p1 = None
t1 = None
p2 = None
t2 = None

img1 = cv2.imread('Images/OmarAlaraby1.png')
img2 = cv2.imread('Images/OmarAlaraby2.png')

def calcPPlus(P) :
    return np.linalg.pinv(P.transpose() @ P) @ P.transpose()

def build() :
    P = np.column_stack((p1, p2))
    T = np.column_stack((t1, t2))

    P_plus = calcPPlus(P)

    W = T @ P_plus
    W = W.flatten()
    return W


def testImage(img, W) :
    img = resize_image(img, 500, 500)
    img = np.array(img.flatten())
    img.resize(len(W))
    type = W @ img

    for i , val in enumerate(type)


    if np.array_equal(type , t1) :
        print("Done")


img1 = resize_image(img1, 300, 300)
img2 = resize_image(img2, 300, 300)

img1 = np.array(img1.flatten())
img2 = np.array(img2.flatten())

p1 = img1
p2 = img2

t1 = np.array([1])
t2 = np.array([0])

# if not np.array_equal(t1, t2) :
#     exit(-1)

W = build()
print(t1)

if not testImage(img1, W) :
    print("ERROR")
    exit(0)




testImg = cv2.imread('Images/OmarAlaraby1.png')
testImage(testImg, W)


