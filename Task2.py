######### Task #########

# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

#---------------------draw function-----------------------
#this will draw a red square around the spot that was clicked with left mouse button (within the image boundaries)
#it will also change the area within the square to YUV
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:#If left mouse button pressed
        I=cv2.imread(f)
        h = I.shape[0] #YUV image height(Y axis) in pixels
        w = I.shape[1] #YUV image width(X axis) in pixels
        YUV=cv2.cvtColor(I,cv2.COLOR_BGR2YUV)
        if x<100:
            x=100
        if y<100:
            y=100 
        if x>w-100:
            x=w-100
        if y>h-100:
            y=h-100
        I[y-100:y+100,x-100:x+100]=YUV[y-100:y+100,x-100:x+100]#I area selected = YUV area selected
        cv2.rectangle(img=I, pt1=(x-100,y-100), pt2=(x+100,y+100),color=(0,0,255),thickness=10) #Draw Rectangle
        cv2.imshow("image",I) #Show the image after 
#--------------------------------------------------------  
     
#1.Open a user selected image
f = easygui.fileopenbox()
I = cv2.imread(f)
Original=I.copy()

#2.Show this image on screen & call draw function
cv2.namedWindow("image")#Create window image
cv2.imshow("image",I)#show image before function
cv2.setMouseCallback("image",draw)#activates the callback
key =cv2.waitKey(0)#waits for a keypress before closing