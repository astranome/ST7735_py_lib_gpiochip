"""
Author: Vincent Lin
Created on: 2023.03.27
GitHub: https://github.com/vincnttt
Ported for ZYNQ7000: Andrew Kobelev. 2024.07.21
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from ST7735 import ST7735

MESSAGE = "Hello Bamboock!"
#spi = spidev.SpiDev() #https://github.com/doceme/py-spidev

disp = ST7735(
    port=0,
    cs=1,		# cs at Ground
    dc=5,      # dc at pin 5
    rst=15,     # rst at pin 15
    rotation=270,    # set rotation to 90 degrees
    width=128,
    height=160,
    spi_speed_hz=4000000
)

# start display
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 0, 0))
font = ImageFont.load_default()

draw = ImageDraw.Draw(img)

draw.text((0, 0), MESSAGE, font=font, fill=(90, 255, 255))
disp.display(img)
