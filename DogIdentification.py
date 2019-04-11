from PIL import Image
import csv

f  = open("labels.csv")
reader = csv.reader(f)
pixelArrays = []
ImageIDs = []
counter = 0
widths = []
heights = []
for row in reader:
    #print(row)
    if counter > 0:
        im = Image.open("./train/" + row[0] + ".jpg")
        width, height = im.size
        widths.append(width)
        heights.append(height)
        if width < 600 and height < 600:
            ImageIDs.append(row[0])
        if counter % 100 == 0:
            print(counter)
        im.close()
    counter += 1

#print(min(widths), min(heights), max(widths), max(heights))
# numBig = 0
# numSmall = 0
# for i in range(len(widths)):
#     if widths[i] > 600 or heights[i] > 600:
#         numBig += 1
#     if widths[i] < 200 or heights[i] < 200:
#         numSmall += 1

# print(numBig)
# print(numSmall)
#im = Image.open("./train/" + ImageIDs[1] + ".jpg")
#im.show()
#im1 = Image.open("./train/" + ImageIDs[2] + ".jpg")
#im1.show()
#for pixel in iter(im.getdata()):
#    print(pixel)
