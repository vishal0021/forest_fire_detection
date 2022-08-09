lat = "36.9848° S"
long = "143.3906° E"

size = 200 #km
bb = getBoundingBox(Lat, Long, size)
image = getImageAt(Bounding box, camera, repeat_state)
display(image)