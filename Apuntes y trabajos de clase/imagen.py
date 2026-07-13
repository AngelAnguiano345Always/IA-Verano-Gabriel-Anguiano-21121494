import cv2 as cv
img = cv.imread('Sandrome.jpg', 0)

print(img.shape)
x,y = img.shape

for i in range(x):
    
    for j in range(y):
        
        if (img[i,j]<155):
            img[i,j]=0
            
        else:
            img[i,j]=255
            
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()