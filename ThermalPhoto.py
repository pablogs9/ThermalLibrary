import os,sys
from ThermalLib.ESCPOS import *
from PIL import Image

t = Thermal("/dev/serial/by-id/usb-0d3a_0368-if00")
im = Image.open("p.jpg")
t.printCompleteBitmapCustom(im)

print "Saliendo..."
t.close()
sys.exit(0)

