#!/usr/bin/python

import urllib
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(0)

project = "http://www.kickstarter.com/projects/1458134548/arkyd-a-space-telescope-for-everyone-0"
goal = 1000000.0

def parse_project():
    f=urllib.urlopen(project)
    s=f.read()
    i=s.find("itemprop=\"Project[pledged]\" value=")
    value=float(s[i+35:i+42])
    return value

f=open("lastvalue.txt","r")
prev = float(f.readline())
f.close()

parsed = parse_project()

lcd.clear()
lcd.message(prev)
lcd.message("\n"+str(goal))

if(parsed>prev):
	lcd.backlight(lcd.GREEN)
	sleep(2)
elif(parsed<prev):
	lcd.backlight(lcd.RED)
	sleep(2)

f=open("lastvalue.txt","w")
f.write(str(parsed))
f.close()

lcd.backlight(lcd.BLUE)		
lcd.clear()
lcd.message(parsed)
lcd.message("\n"+str(goal))