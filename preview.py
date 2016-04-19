from PIL import Image
import sys
from math import ceil
from math import floor



im = Image.open("in.jpg")
t = int(raw_input("Tamano de la foto en tiras de papel: "))
w, h = im.size
print "Original size: " + str(w) + " " + str(h)
print "Ratio: " +str(float(t*256)/w)
print "Calculated size: " + str(t*256) + " " + str(int(h*(float(t*256)/w)))
im = im.resize((t*256,int(h*(float(t*256)/w))),Image.ANTIALIAS)
w, h = im.size
print "Actual size: " + str(w) + " " + str(h)
print "Actual paper size: " + str(w/256) + " tiras, " + str(h/256) + " cuadrados de alto"

im = im.crop((0,0,int(floor(w/256.0))*256,h))

w, h = im.size
wc = int(ceil(w/256.0))
hc = int(ceil(h/256.0))
im = im.convert('1')

marginh = 30
marginv = 2
canvas = Image.new('1',(wc*256+(wc+1)*marginh,h+hc*marginv),1)

##IMPRESION
for i in range(wc):
    hAux = h
    for j in range(hc):
            if hAux > 256:
                print "Imprimiendo " + str(j) + "/" + str(i)
                #print str(i*256) + "," + str(j*256) + " " + str(i*256+256) + "," + str(j*256+256)
                imaux = im.crop((i*256,j*256,i*256+256,j*256+256))
                hAux = hAux - 256
            else:
                print "Imprimiendo " + str(j) + "/" + str(i)
                #print str(i*256) + "," + str(j*256) + " " + str(i*256+256) + "," + str(j*256+hAux)
                imaux = im.crop((i*256,j*256,i*256+256,j*256+hAux))
                hAux = 0
            canvas.paste(imaux,(i*256+(i+1)*marginh,j*256+(j+1)*marginv))
canvas.show()
    #raw_input("Continue")
    #self.printBitmap(imaux,1)
canvas.save("out.jpeg")
print "Saliendo..."
sys.exit(0)
