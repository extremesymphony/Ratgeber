import cv2
import numpy as np
global lower_bound
global upper_bound
lower_bound=np.array([38,150,40])
upper_bound=np.array([75,255,150])

def detect_table(image):
	element=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
	morphed_image=cv2.morphologyEx(image,cv2.MORPH_CLOSE,element)
	a,b=cv2.findContours(morphed_image,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	contours=np.array(a)
	contour_area=[]
	for i in contours:
		contour_area.append(cv2.contourArea(i))
	contour=contours[contour_area.index(max(contour_area))]
	return contour
def detect_pots(image,contours):
	pots=[]
	x,y,w,h=cv2.boundingRect(contours)
	x1=x+w
	y1=y+h
	xm1=x+w/2
	x2=x+10
	y2=y+10
	x3=x1-10
	y3=y1-10
	pots.append((x3,y2))
	pots.append((x3,y3))
	pots.append((x2,y2))
	pots.append((x2,y3))
	pots.append((xm1,y))
	pots.append((xm1,y1))
	cv2.line(image,(x3,y2),(x3,y3),(255,0,0))
	cv2.line(image,(x2,y2),(x2,y3),(255,0,0))
	cv2.line(image,(x2,y2),(x3,y2),(255,0,0))
	cv2.line(image,(x2,y3),(x3,y3),(255,0,0))	
	return pots
	
