lat = "36.9848° S"
long = "143.3906° E"

size = 200 #km
b_box = getBoundingBox(Lat, Long, size)
#camera 1 is Nadir
#no repeat 
image = getImageAt(b_box, 1, False)
display(image)
