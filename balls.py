import cv2
import numpy as np
import structures
import timeit

global red
global coloured
global white
global pots
global lower_bound
global upper_bound
red=[]
coloured=[]
white=[]
pots=[]
lower_bound=np.array([0,140,100])
upper_bound=np.array([15,255,255])

def blue(image):
	global coloured
	lower_bound=np.array([98,132,101])
	upper_bound=np.array([104,232,255])
	operated_image=cv2.inRange(image,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	coloured.append(circles_list[0][0])

def green(image):
	global coloured
	lower_bound=np.array([73,99,47])
	upper_bound=np.array([76,228,152])
	operated_image=cv2.inRange(image,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	coloured.append(circles_list[0][0])
	
def yellow(image):
	global coloured
	lower_bound=np.array([22,100,210])
	upper_bound=np.array([34,211,255])
	operated_image=cv2.inRange(image,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	coloured.append(circles_list[0][0])

def brown(image):
	global coloured
	lower_bound=np.array([15,100,20])
	upper_bound=np.array([20,228,150])
	operated_image=cv2.inRange(image,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	coloured.append(circles_list[0][0])

def pink(image):	
	global coloured
	lower_bound=np.array([0,0,50])
	upper_bound=np.array([10,100,255])
	operated_image=cv2.inRange(image,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	coloured.append(circles_list[0][0])

def red_balls(image):	
	global red
	lower_bound=np.array([0,140,100])
	upper_bound=np.array([20,255,255])
	operated_image=cv2.inRange(image,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	#print 'Amadeus',circles_list[0][1]
	for i in xrange(0,len(circles_list[0])):
		red.append(circles_list[0][i])
	
def black(image):
	global coloured
	lower_bound=np.array([0])
	upper_bound=np.array([50])
	value=cv2.split(image)[2]
	operated_image=cv2.inRange(value,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	coloured.append(circles_list[0][0])	

def white_ball(image):
	global white
	lower_bound=np.array([0])
	upper_bound=np.array([40])
	saturation=cv2.split(image)[1]
	operated_image=cv2.inRange(saturation,lower_bound,upper_bound)
	masked=mask_image(operated_image,image)
	circle=cv2.HoughCircles(masked,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=300,param2=7,minRadius=6,maxRadius=8)
	circles_list=list(circle)
	white.append(circles_list[0][0])	

	
def mask_image(image1,image2):
	lower=np.array([38,150,40])
	upper=np.array([75,255,150])
	table_mask=cv2.inRange(image2,lower,upper)
	element=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(45,45))
	res=cv2.morphologyEx(table_mask,cv2.MORPH_CLOSE,element)
	image=cv2.bitwise_and(image1,res)
	return image
	
def detect_balls(image):
	global lower_bound
	global upper_bound
	global coloured
	global red
	blue(image)
	green(image)
	yellow(image)
	brown(image)	
	pink(image)
 	black(image)
	white_ball(image)
	red_balls(image)	
	
def draw_balls(image,list):
	circles=np.array(list)
	for i in circles:
		cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),1)
		cv2.circle(image,(i[0],i[1]),2,(0,255,0),3)
		
def main():
	global red
	global white
	global coloured
	global pots
	img=cv2.imread('C:\\ASK\\Major\\image\\5.jpg')
	copy1=img
	start=timeit.default_timer()									
	cv2.imshow('Image',img)											
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	hsv=cv2.cvtColor(img,cv2.cv.CV_BGR2HSV)							
	lower_bound=np.array([38,150,40])
	upper_bound=np.array([75,255,200])
	masked=cv2.inRange(hsv,lower_bound,upper_bound)
	contour=structures.detect_table(masked)
	pots=structures.detect_pots(img,contour)
	cv2.drawContours(img,contour,contourIdx=-1,color=[0,0,255])
	cv2.imshow('Detected table',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	detect_balls(hsv)
	draw_balls(img,coloured)
	draw_balls(img,red)
	draw_balls(img,white)
	cv2.imshow('Detected balls and table',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return (white,pots,coloured,red)
