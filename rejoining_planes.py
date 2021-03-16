import cv2
import numpy as np
# Function to convert unit8 image to bitstream array
def int2bitarray(img):
    arr = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            arr.append(np.binary_repr(img[i][j], width=8))
    return arr
# read image convert to bit stream
img0 = cv2.imread('./Bitplane0.png',0)//255
img1 = cv2.imread('./Bitplane1.png',0)//255
img2 = cv2.imread('./Bitplane2.png',0)//255
img3 = cv2.imread('./Bitplane3.png',0)//255
img4 = cv2.imread('./Bitplane4.png',0)//255
img5 = cv2.imread('./Bitplane5.png',0)//255
img6 = cv2.imread('./Bitplane6.png',0)//255
img7 = cv2.imread('./Bitplane7.png',0)//255
res67 = np.zeros((img0.shape))
res567 = np.zeros((img0.shape))
res4567 = np.zeros((img0.shape))
res34567 = np.zeros((img0.shape))
res234567 = np.zeros((img0.shape))
res1234567 = np.zeros((img0.shape))
res01234567 = np.zeros((img0.shape))
# save grayscale
for i in range(img0.shape[0]):
    for j in range(img0.shape[1]):

        res67[i,j] = img6[i,j]<<6|img7[i,j]<<7
        res567[i,j] = img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res4567[i,j] = img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res34567[i,j] = img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res234567[i,j] = img2[i,j]<<2|img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res1234567[i,j] = img1[i,j]<<1|img2[i,j]<<2|img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res01234567[i,j] = img0[i,j]|img1[i,j]<<1|img2[i,j]<<2|img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7

cv2.imwrite('./res67.png',res67)
cv2.imwrite('./res567.png',res567)
cv2.imwrite('./res4567.png',res4567)
cv2.imwrite('./res34567.png',res34567)
cv2.imwrite('./res234567.png',res234567)
cv2.imwrite('./res1234567.png',res1234567)
cv2.imwrite('./res01234567.png',res01234567)
print('done!')



'''
arr = np.array(int2bitarray(img))
arr = arr.reshape(img.shape)

plane = np.zeros((img.shape))
for k in range(0,8):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            plane[i,j]=int(arr[i,j][k])
            # print(plane)
    if k==0:
        p0 = plane
    elif k==1:
        p1 = plane
    elif k==2:
        p2 = plane
    elif k==3:
        p3 = plane
    elif k==4:
        p4 = plane
    elif k==5:
        p5 = plane
    elif k==6:
        p6 = plane
    elif k==7:
        p7 = plane

p01 = np.zeros((img.shape))
p012 = np.zeros((img.shape))
p0123 = np.zeros((img.shape))
p01234 = np.zeros((img.shape))
p012345 = np.zeros((img.shape))
p0123456 = np.zeros((img.shape))
p01234567 = np.zeros((img.shape))

for i in range(p01.shape[0]):
    for j in range(p01.shape[1]):
        p01[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)
        p012[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)|(int(p2[i,j])<<2)
        p0123[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)|(int(p2[i,j])<<2)|(int(p3[i,j])<<3)
        p01234[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)|(int(p2[i,j])<<2)|(int(p3[i,j])<<3)|(int(p4[i,j])<<4)
        p012345[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)|(int(p2[i,j])<<2)|(int(p3[i,j])<<3)|(int(p4[i,j])<<4)|(int(p5[i,j])<<5)
        p0123456[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)|(int(p2[i,j])<<2)|(int(p3[i,j])<<3)|(int(p4[i,j])<<4)|(int(p5[i,j])<<5)|(int(p6[i,j])<<6)
        p01234567[i,j] = int(p0[i,j])|(int(p1[i,j])<<1)|(int(p2[i,j])<<2)|(int(p3[i,j])<<3)|(int(p4[i,j])<<4)|(int(p5[i,j])<<5)|(int(p6[i,j])<<6)|(int(p7[i,j])<<7)

print(p01234567)
cv2.imwrite('./Bitplanes01.png',p01)
cv2.imwrite('./Bitplanes012.png',p012)
cv2.imwrite('./Bitplanes0123.png',p0123)
cv2.imwrite('./Bitplanes01234.png',p01234)
cv2.imwrite('./Bitplanes012345.png',p012345)
cv2.imwrite('./Bitplanes012345.png',p0123456)
cv2.imwrite('./Bitplanes01234567.png',p01234567)
'''
print(' done!')
