#oled device imports
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

#oled display setup
serial = i2c(port=0, address=0x3C)
device = ssd1306(serial, rotate=0)

device.hide()
