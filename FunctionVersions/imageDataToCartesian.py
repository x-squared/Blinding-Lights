# Blinding Lights Image to Cartesian Coordinates [Python 3.8.2]
if __name__ == "__main__": print('Module imageDataToCartesian.py')
# Created by Ayush Nayak in 2020
from PIL import Image # TODO CANNOT IMPORT 
#CorePackages
def rgbToHex(RGBtuple):
    return '#%02x%02x%02x' % (RGBtuple[0], RGBtuple[1], RGBtuple[2])

def rbgToRaster(RGBtuple):

    return "Almost Written"

#Functions
def imagetoCartesian(path, notflipped=False): #DEPRECATED PACKAGE

    try:
        im = Image.open(path, 'r').convert('RGB')
    except FileNotFoundError:
        print('Not Running, Image Path Incorrect!')
        print('Exiting...')
        exit(1)
    redPix = list(im.getdata(0))
    greenPix = list(im.getdata(1))
    bluePix = list(im.getdata(2))
    pixArr = []
    for l in range(0, len(redPix)):
        pixArr.append((redPix[l], greenPix[l], bluePix[l]))



    hexArr = []

    for m in range(0, len(pixArr)):
        hexArr.append(rgbToHex(pixArr[m]))

# now everything has been converted into a list with the hex values, but its not in xy form YET...

    width, height = im.size

    countx = 0
    county = 0

    output = []
    if notflipped:
        countHex = 0

        while county < height:
            list1 = []
            while countx < width:
                list1.append(hexArr[countHex])
                countHex+=1
                countx+=1
            #now countx = 100
            output.append(list1)
            countx = 0
            county += 1
        return output
    else:

        countX = 0
        countY = 0

        while countx < width:
            list1 = []
            while county/100 < height:
                list1.append(hexArr[countY + countx])
                countY += 100
            output.append(list1)
            countX += 1




if __name__ == "__main__":
    print("Imported Successfully") # import message


def PILImageToRaster(path):
    try:
        im = Image.open(path, 'r').convert('RGB')
    except FileNotFoundError:
        print('Not Running, Image Path Incorrect!')
        print('Exiting...')
        exit(1)
    redPix = list(im.getdata(0))
    greenPix = list(im.getdata(1))
    bluePix = list(im.getdata(2))
    pixArr = []
    for l in range(0, len(redPix)):
        pixArr.append((redPix[l], greenPix[l], bluePix[l]))


    hexArr = []

    for m in range(0, len(pixArr)):
        hexArr.append(rgbToHex(pixArr[m]))

    width, height = im.size

    countx = 0
    county = 0

    output = []

    countHex = 0

    while county < height:
        list1 = []
        while countx < width:

            list1.append(hexArr[countHex])
            countHex+=1
            countx+=1
        #now countx = 100
        output.append(list1)
        countx = 0
        county += 1
    return output


imagetoCartesian("/TestData/b.png")
