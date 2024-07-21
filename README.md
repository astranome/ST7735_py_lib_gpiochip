# ST7735 PYLib

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/vincnttt/ST7735_pylib/blob/master/LICENSE)
![device](https://img.shields.io/badge/raspberrypi-4b-red)
![python](https://img.shields.io/badge/python-3.9-blue)

Python library to control an ST7735 TFT LCD display.  Allows simple drawing on the display without installing a kernel module. 

Designed specifically to work with a ST7735 1.8inch (128x160 pixel) TFT SPI display.

## Installation

### Python 3

Install required dependencies

```commandline
sudo pip install numpy spidev gpiod
```

## Usages

At present, this repository still not available to install using `pip`, so its recommended to copy the file `/ST7735/ST7735.py` into your project directory. 

Then to use, import the library like showed below.

```python
import ST7735
```

**Tested and work on Zynq 7010, Python 3.10**

## License

This library is a modification of a modification of code originally written by Tony DiCola for Adafruit Industries [repo](https://github.com/adafruit/Adafruit_Python_ILI9341), 
and modified to work with the ST7735 by Clement Skau [repo](https://github.com/cskau/Python_ST7735).

Now this library has been modified by Vincent Lin to support ST7735 1.8inch (128x160 pixel), 
originally this modification was motivate by Pimoroni to include support for their 160x80 SPI LCD breakout [repo](https://github.com/pimoroni/st7735-python)

MIT license, all text above must be included in any redistribution

## History and Modification

Adafruit invests time and resources providing this open source code, 
please support Adafruit and open-source hardware by purchasing products from Adafruit!

Modified from 'Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries.' written by Clement Skau.

Pimoroni invests time and resources forking and modifying this open source code, 
please support Pimoroni and open-source software by purchasing products from us, too!

Vincent Lin was modified this repo based on the three repository's ideas that introduced on [Licensing](https://github.com/vincnttt/ST7735_pylib#license) part above, 
mixing the methods to make it work with ST7735 1.8inch (128x160 pixel) TFT SPI, 
with some features that introduced in [Modification](https://github.com/vincnttt/ST7735_pylib#modification) part below.

### Modification

* Set value of `width=128` and `height=160`
* Support screen rotation `rotation`
* Dependencies `Adafruit_GPIO` replaced with `RPi.GPIO` and `spidev`

## Examples

See example of usage in the `/examples/` folder.

## Thanks

Thanks to Tony DiCola for Adafruit Industries, Clement Skau and Pimoroni :clap:, to make this project open-source till now :smiley:
