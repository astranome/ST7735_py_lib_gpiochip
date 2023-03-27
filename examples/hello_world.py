"""
Author: Vincent Lin
Created on: 2023.03.27
GitHub: https://github.com/vincnttt
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from ST7735 import ST7735

MESSAGE = "Hello World!"

disp = ST7735.ST7735(
    port=0,
    cs=0,
    dc=24,      # dc at pin 24
    rst=25,     # rst at pin 25
    rotation=90,    # set rotation to 90 degrees
    width=128,
    height=160,
    spi_speed_hz=4000000
)

# start display
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
font = ImageFont.load_default()

draw = ImageDraw.Draw(img)

draw.text((0, 0), MESSAGE, font=font, fill=(255, 255, 255))
disp.display(img)
