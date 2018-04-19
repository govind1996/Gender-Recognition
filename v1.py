import cv2
import numpy as np
import skimage.feature
import skimage.exposure
import math
img=cv2.imread('img10.jpg',0)
#print(img)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
h,w=img.shape
#print(h,w)
r=200/w
img=cv2.resize(img,(200,np.int(h*r)))
origh,origw=img.shape
#cv2.imshow('image',img )
#cv2.waitKey(0)
#print(h,w)
img3=np.int64(img)+127
img3=np.minimum(img3,255)
img2=img3[:,100:200]
#cv2.imshow('image',img2)
#cv2.waitKey(0)
img4=img[:,100:200]
#cv2.imshow('image',img4 )
#cv2.waitKey(0)
h,w=img2.shape
#print(h,w)
maxdif = 0
for i in range(0,int(h/2)):
    for j in range(1,w):
        if (abs(np.int64(img2[i][j - 1]) - np.int64(img2[i][j])) >= maxdif):
            maxdif = abs(np.int64(img2[i][j - 1]) - np.int64(img2[i][j]))
            ans = i
            ans1=j

       # print(img2[i][j],end=' ')
   # print('\n')

#print(ans,ans1,maxdif)
#print(img2)
#img2[ans][ans1]=0
#cv2.imshow('image',img2)
#cv2.waitKey(0)
h,w=img.shape
#print(h,w)
x1=int(ans-(0.15*w))
y1=int(0.32*w)
x2=int(x1+(0.55*w))
y2=int(y1+0.4*w)
#print(x1,y1,x2,y2)
#img[ans1][ans]=0
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.imshow('image',img)
#cv2.waitKey(0)
img2=img[x1:x2,y1:y2]
#cv2.imshow('image',img2)
#cv2.waitKey(0)
up=x1
ret,th1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
hi,lo=np.unravel_index(th1.argmin(), th1.shape)
up=up+hi
img2=img2[hi:,:]
#cv2.imshow('image',img2)
#cv2.waitKey(0)
#print(hi,lo,th1[hi][lo])
th1=th1[hi:,:]
#cv2.imshow('image',th1)
#cv2.waitKey(0)
h,w=th1.shape
#print(h,w)
h=int(2*h/3)
up=up+h
img2=img2[h:,:]
img3=np.int64(img2)+127
th1=np.minimum(img3,255)
#for i in range(h):
    #for j in range(w):
        #print(th1[i][j],end=' ')
    #print('\n ')
#cv2.imshow('image',th1)
#cv2.waitKey(0)
hi,lo=np.unravel_index(th1.argmin(), th1.shape)
#cv2.imshow('image',img2)
#cv2.waitKey(0)
up=up+hi
up=int(up+0.05*origw)
#print(hi,lo,origh,origw)
#print(up,origh)
img2=img[up:origh,:]
h2,w2=img2.shape
#cv2.imshow('image',img2)
#cv2.waitKey(0)
#### canny edge to remove background
# filter=cv2.Canny(img2,w2,h2)
# cv2.imshow('edge',filter)
# cv2.waitKey(0)
# maxj=0
# for i in range(0,h2):
#     for j in range(0,w2):
#        #print(filter[i][j],end=' ')
#        if filter[i][j]==255:
#            if(j>maxj):
#                maxj=j
#            break
#
#     #print('\n')
# print(maxj)
# img2=img2
# img2=img2[:,maxj:]
# cv2.imshow('img',img2)
# cv2.waitKey(0)
# h2,w2=img2.shape
# filter=cv2.Canny(img2,w2,h2)
# maxj=0
# for i in range(0,h2):
#     for j in range(0,w2):
#        #print(filter[i][j],end=' ')
#        if filter[i][j]==255:
#            if(j>maxj):
#                maxj=j
#
#
#     #print('\n')
# print(maxj)
# img2=img2
# img2=img2[:,:maxj]
# cv2.imshow('img',img2)
# cv2.waitKey(0)

#### histogram approach
# img3=np.int64(img2)+127
# th1=np.minimum(img3,255)
# hi,lo=np.unravel_index(th1.argmin(), th1.shape)
# #print(hi,lo)
# img2=img2[:,hi:]
# #cv2.imshow('image',img2)
# #cv2.waitKey(0)
# h1,w1=img2.shape
# img4=img2
# rot_mat=cv2.getRotationMatrix2D((math.floor(w1/2),math.floor(h1/2)),180,1)
# img4=cv2.warpAffine(img4,rot_mat,(w1,h1))
# cv2.imshow('image',img4)
# cv2.waitKey(0)
# img3=np.int64(img4)+127
# th1=np.minimum(img3,255)
# hi,lo=np.unravel_index(th1.argmin(), th1.shape)
# print(hi,lo,th1[hi][lo])
# img2=img4[:,hi:]
# cv2.imshow('image',img2)
# cv2.waitKey(0)

##histogram without rotation
img3=np.int64(img2)+127
img3=np.minimum(img3,255)
h,w=img3.shape
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
#print(ans,ans1,maxdif,h,w)
img2=img2[:,ans1:]
#cv2.imshow('image',img2)
#cv2.waitKey(0)
img3=np.int64(img2)+127
img3=np.minimum(img3,255)
h,w=img3.shape
maxdif=0
for i in range(int(h/2)-15,int(h/2)+10):
    for j in range(w-40,w):
        if (abs(np.int64(img3[i][j - 1]) - np.int64(img3[i][j])) >= maxdif):
            maxdif = abs(np.int64(img3[i][j - 1]) - np.int64(img3[i][j]))
            ans = i
            ans1=j
        if (abs(np.int64(img3[i-1][j]) - np.int64(img3[i][j])) > maxdif):
            maxdif = abs(np.int64(img3[i-1][j]) - np.int64(img3[i][j]))
            ans = i
            ans1=j
#print(ans,ans1,maxdif,h,w)
img2=img2[:,:ans1]
cv2.imshow('image',img2)
cv2.waitKey(0)
### canny part 2
# h2,w2=img2.shape
# img3=np.int64(img2)+127
# img3=np.minimum(img3,255)
# filter=cv2.Canny(img3,w2,h2)
# maxj=w2
# for i in range(h2-1,-1,-1):
#     for j in range(w2-1,-1,-1):
#        #print(filter[i][j],end=' ')
#        if filter[i][j]==255:
#            if(j<maxj):
#                maxj=j
#            break
#
#     #print('\n')
# print(maxj)
# img2=img2
# img2=img2[:,:maxj]
# cv2.imshow('img',img2)
# cv2.waitKey(0)
#img2=skimage.img_as_ubyte(img2)
#img2=np.uint8(img2/32)
img2=skimage.exposure.rescale_intensity(img2,in_range='image',out_range=(0,7))
# #print(img2)
# g=skimage.feature.greycomatrix(img2,[1],[0],levels=8,symmetric=False,normed=False)
# g=g[:,:,0,0]
# print(g)
# mean=(np.sum(g))/64
# print(mean)
g=skimage.feature.greycomatrix(img2,[1],[0],levels=8,symmetric=False,normed=True)
# for i in range(0,8):
#     for j in range(0,8):
#         print(g[i][j][0][0],end=' ')
#     print('\n')
#converting 4d GLCM matrix into 2D matrix
img2=g[:,:,0,0]
#print(img2)

#calculating contrast
contrast=0
for i in range(0,8):
    for j in range(0,8):
        contrast+=(i-j)**2*img2[i][j]
#print(contrast)
#g=g/sum
#contrast1=skimage.feature.greycoprops(g,prop='contrast')
#print(contrast1)

#calculating dissimilarity
dissimilarity=0
for i in range(0,8):
    for j in range(0,8):
        dissimilarity+=img2[i][j]*abs(i-j)
#print(dissimilarity)
#dissimilarity1=skimage.feature.greycoprops(g,prop='dissimilarity')
#print(dissimilarity1)

meanl=0
meanr=0
for i in range(0,8):
    for j in range(0,8):
        meanl+=i*img2[i][j]
        meanr+=j*img2[i][j]
#print(meanl)
#print(meanr)
#calculating variance
#print(img2)
variance=0
for i in range(0,8):
    for j in range(0,8):
        variance+=((i-meanl)**2)*img2[i][j]
print(contrast,dissimilarity,variance)