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
img = cv2.imread('./lena.png',0)
arr = np.array(int2bitarray(img))
arr = arr.reshape(img.shape)
plane = np.zeros((8,img.shape[0],img.shape[1]), dtype=int)

for k in range(0,8):
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			plane[k,i,j]=int(arr[i,j][k])
	# save individual bit planes:
	# cv2.imwrite('./Bitplane'+str(7-k)+'.png',plane[k]*255)
	# print('\nbit plane '+str(7-k)+' done!')
# print(plane)
temp = np.zeros((plane.shape[1],plane.shape[2]))


for k in range(1,plane.shape[0]):
	# print(k)
	for i in range(plane.shape[1]):
		for j in range(plane.shape[2]):

			if k==1:
				# bitplanes 7 and 6
				temp[i,j] = plane[k-1,i,j]<<7|plane[k,i,j]<<6
			elif k ==2:
				# bitplanes 7, 6, and 5
				temp[i,j] = plane[k-2,i,j]<<7|plane[k-1,i,j]<<6|plane[k,i,j]<<5
			elif k ==3:
				# bitplanes 7, 6, 5 and 4
				temp[i,j] = plane[k-3,i,j]<<7|plane[k-2,i,j]<<6|plane[k-1,i,j]<<5|plane[k,i,j]<<4
			elif k ==4:
				# bitplanes 7,6,5,4, and 3
				temp[i,j] = plane[k-4,i,j]<<7|plane[k-3,i,j]<<6|plane[k-2,i,j]<<5|plane[k-1,i,j]<<4|plane[k,i,j]<<3
			elif k ==5:
				# bitplanes 7, 6, 5, 4, 3, and 2
				temp[i,j] = plane[k-5,i,j]<<7|plane[k-4,i,j]<<6|plane[k-3,i,j]<<5|plane[k-2,i,j]<<4|plane[k-1,i,j]<<3|plane[k,i,j]<<2
			elif k ==6:
				# bitplanes 7, 6, 5, 4, 3, 2, and 1
				temp[i,j] = plane[k-6,i,j]<<7|plane[k-5,i,j]<<6|plane[k-4,i,j]<<5|plane[k-3,i,j]<<4|plane[k-2,i,j]<<3|plane[k-1,i,j]<<2|plane[k,i,j]<<1
			elif k ==2:
				# bitplanes 7, 6, 5, 4, 3, 2, 1, and 0s
				temp[i,j] = plane[k-7,i,j]<<7|plane[k-6,i,j]<<6|plane[k-6,i,j]<<5|plane[k-4,i,j]<<4|plane[k-3,i,j]<<3|plane[k-2,i,j]<<2|plane[k-1,i,j]<<1|plane[k,i,j]

	cv2.imwrite('./Bitplanes'+''.join([str(7-x) for x in range(k+1)])+'.png', temp)


