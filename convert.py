import os
from PIL import Image

folder = "hummingbird"

try:
    os.mkdir(folder + "-ppm")
except OSError:
    print ("Creation of the directory %s failed" % path)

counter = 0
with os.scandir(folder) as it:
    for entry in it:
        image = Image.open(folder+"/"+entry.name)
        image.save(folder + "-ppm/" + str(counter) + ".ppm")
        counter += 1