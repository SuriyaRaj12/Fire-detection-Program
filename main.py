Import serial #import serial package
from time import sleep #import package for opening link in browser
import sys #import system package
from picamera import PiCamera
import webbrowser
import Rpi.GPIO as GPIO
from gpiozero import LED
import smtplib
from gpiozero import MCP3008
import serial
import requests
import numpy as np
import argparse
import cv2
import pygame
camera = PiCamera()
camera.resolution = (320, 240)
buzzer = LED(26)
motor = LED(6)
fan = LED(27)
camera.start_preview()
sleep(10)
camera.capture(„fire.png‟,format = „png‟)
camera.stop_preview()
image = cv2.imread(“fire.png”)
 # find the colors within the specified boundaries and apply
 # the mask
mask = cv2.inRange(image, lower, upper)
contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,v2.CHAIN_APPROX_
NONE)
 #print(mask)
 output = cv2.bitwise_and(image, image, mask = mask)
 for contour in contours:
 cv2.drawContours(image, contour, -1, (0, 255, 0), 1)
 #print(boundaries[j])
 j=j+1
 print(j)
 for pic, contour in enumerate(contours):
 area = cv2.contourArea(contour)
 if area>0 :
 #print(„Area=‟)
 #print(area)
 #print(j)
 if j == 1:
 area1=area1+area
 print(area1)
 if area1 > 800:
 print(“fire”)
 ser.write(„‟‟AT+CMGS=”‟‟‟.encode()+recipient.encode()+ \r‟‟‟.encode())
 sleep(1)
 ser.write(“Fire Detected”.encode())
 sleep(1)
 ser.write(chr(26).encode())
 sleep(1)
 buzzer.on()
 sleep(2)
 buzzer.off()
 break
 #cv2.imshow(“Frame”, image)
 b, g, r = cv2.split(output)
#cv2.imshow(„B‟,b)
#cv2.imshow(„G‟,g)
#cv2.imshow(„R‟,r)
cv2.imshow(“images”, np.hstack([image, output]))
cv2.waitKey(0)
buzzer.on()
sleep(1)
buzzer.off()
while True:
 temp = MCP3008(0)
 Temp = temp.value * 10
 print(„Temp=‟ + str(Temp))
 fire = MCP3008(1)
 Fire = fire.value * 10
 print(„fire=‟ + str(Fire))
 r =requests.get(„http://www.iotclouddata.com/20log/200/iot20.php?A=Temp=‟ +
str(Temp) +‟_Fire=‟+ str(Fire))
 if Temp > 0.6:
 fan.on()
 motor.on()
 pygame.mixer.init()
 pygame.mixer.music.load(„firefire.mp3‟)
 pygame.mixer.music.play()
 sleep(5)
 fan.off()
 motor.off()
 „‟‟if Fire > 3:
 r=requests.get(„http://www.iotclouddata.com/20log/map001/iot20.php?A=‟+
lat_in_degrees +‟_‟+ long_in_degrees)
 pygame.mixer.init()
 pygame.mixer.music.load(„firefire.mp3‟)
 pygame.mixer.music.play()
 sleep(5)
 motor.off()‟‟‟
