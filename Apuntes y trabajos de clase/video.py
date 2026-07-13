import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)


while(True):
    ret, img = cap.read()
    if(ret):
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        unb=(0,60,60)
        una=(10,255, 255)
        #img2 = np.zeros((img.shape[:2]), np.uint8  )
        #print(img.shape[:2])
        #b,g,r=cv.split(img)

        #rojo=cv.merge([r,b,g])
        #verde= cv.merge([img2,g,img2])
        #azul = cv.merge([img2,img2,b])
        
        #cv.imshow('img', img2)
        #cv.imshow('r', r)
        #cv.imshow('g',g)
        #cv.imshow('b',b)
        #cv.imshow('rojo', rojo)
        #cv.imshow('verde',verde)
        #cv.imshow('azul',azul)
        cv.imshow('hsv', hsv)
    
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('No se encontro camara')
    
cap.release()
cv.destroyAllWindows()