import cv2
import numpy as np

#to read image
img=cv2.imread('img20.......................................................................jpg',0)
h,w=img.shape
#resizing image with 200 width
r=200/w
img=cv2.resize(img,(200,np.int(h*r)))
origh,origw=img.shape
cv2.imshow('image',img )
cv2.waitKey(0)
#normalizing the gray scale matrix
img3=np.int64(img)+127
img3=np.minimum(img3,255)
img2=img3[:,100:200]
img4=img[:,100:200]
h,w=img2.shape
#finding the position of eyeball
maxdif = 0
for i in range(0,int(h/2)):
    for j in range(1,w):
        if (abs(np.int64(img2[i][j - 1]) - np.int64(img2[i][j])) >= maxdif):
            maxdif = abs(np.int64(img2[i][j - 1]) - np.int64(img2[i][j]))
            eye_r = i
            eye_c=j

h,w=img.shape

#predicting the position of nose using geometric model
#eye_r contains row index of the position of eyeball
x1=int(eye_r-(0.15*w))
y1=int(0.32*w)
x2=int(x1+(0.55*w))
y2=int(y1+0.4*w)
img2=img[x1:x2,y1:y2]
up=x1
cv2.imshow('image',img2)
cv2.waitKey(0)
#removing the upper part of the predicted nose region

ret,th1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
hi,lo=np.unravel_index(th1.argmin(), th1.shape)
up=up+hi
img2=img2[hi:,:]
th1=th1[hi:,:]
h,w=th1.shape

#extracting the lower one third part of the nose where nosetrils are present

h=int(2*h/3)
up=up+h
img2=img2[h:,:]
img3=np.int64(img2)+127
th1=np.minimum(img3,255)

#finding the position of nosetrills

hi,lo=np.unravel_index(th1.argmin(), th1.shape)
up=up+hi

#extracting the lower part of face

up=int(up+0.05*origw)
img2=img[up:origh,:]
h2,w2=img2.shape
img3=np.int64(img2)+127
img3=np.minimum(img3,255)
h,w=img3.shape

#removing the background using histogram approach in vertical direction

maxdif=0
for i in range(int(h/2)-15,int(h/2)+5):
    for j in range(1,40):
        if (abs(np.int64(img3[i][j - 1]) - np.int64(img3[i][j])) > maxdif):
            maxdif = abs(np.int64(img3[i][j - 1]) - np.int64(img3[i][j]))
            ans = i
            ans1=j
        if (abs(np.int64(img3[i-1][j]) - np.int64(img3[i][j])) > maxdif):
            maxdif = abs(np.int64(img3[i-1][j]) - np.int64(img3[i][j]))
            ans = i
            ans1=j
img2=img2[:,ans1:]
img3=np.int64(img2)+127
img3=np.minimum(img3,255)
h,w=img3.shape
maxdif=0
for i in range(int(h/2)-15,int(h/2)+5):
    for j in range(w-40,w):
        if (abs(np.int64(img3[i][j - 1]) - np.int64(img3[i][j])) >= maxdif):
            maxdif = abs(np.int64(img3[i][j - 1]) - np.int64(img3[i][j]))
            ans = i
            ans1=j
        if (abs(np.int64(img3[i-1][j]) - np.int64(img3[i][j])) > maxdif):
            maxdif = abs(np.int64(img3[i-1][j]) - np.int64(img3[i][j]))
            ans = i
            ans1=j
img2=img2[:,:ans1]

#final image of the lower face

cv2.imshow('image',img2)
cv2.waitKey(0)
