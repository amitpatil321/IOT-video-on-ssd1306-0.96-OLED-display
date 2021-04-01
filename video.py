
import time
import sys
import os 

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# initialise 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# folder = "bahubali-ppm"
# folder = "sunrise-ppm"
# folder = "animation-ppm"
# folder = "white-animation-ppm"
# folder = "fire-effect-ppm"
# folder = "circle-animation-ppm"
# folder = "circle-animation-big-ppm"
folder = "hummingbird-ppm"


# get nuber of files in folder
total_files = len(os.listdir(folder))

for i in range(0, total_files):
  print(folder +"/" + str(i)+'.ppm')
  image = Image.open( folder +"/"+ str(i)+'.ppm').convert('1')

  disp.image(image)
  disp.display()

# Clear the display
disp.clear()
disp.display()