import cv2

source="img.png"
destination='newimg.png'
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)


scale_percent = int(input("enter the percent u want the photo to be:"))

#calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)
