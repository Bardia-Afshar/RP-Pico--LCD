######################################################################################
#Title   :  HD44780 LCD Library(4Bit) Test for Raspberry pi Pico
#Author  :  Bardia Alikhan Afshar <bardia.a.afshar@gmail.com>
#Language:  Python
#Hardware:  Raspberry pi pico
#####################################################################################
from machine import Pin, Timer
import time
from lcd import *


#LCD Object and pin definition
LCD=lcd(RS=0, RW=1, EN=2, D4=3, D5=4, D6=5,D7=6,COL=16, ROW=2)
#LCD Initializing
LCD.init()
#LCD Clear
LCD.clrscr()
#Writes "Hello World!" on position 2,0
LCD.pos_puts(2,0,"Hello World!")
#Delay for 3 Seconds
time.sleep(3)
#LCD Clear
LCD.clrscr()
# Slides some name on LCD :P
while True:
    for i in range(0, 11, 1):
        LCD.pos_puts(i,0,"Bardia")
        LCD.pos_puts(10-i,1,"Bardia")
        time.sleep(0.3)
        LCD.clrscr()
    
    for i in range(9, 0, -1):
        LCD.pos_puts(i,0,"Bardia")
        LCD.pos_puts(10-i,1,"Bardia")
        time.sleep(0.3)
        LCD.clrscr()
