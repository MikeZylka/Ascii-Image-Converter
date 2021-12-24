import PIL
import numpy as np
from PIL import Image
import sys
import os

# function that takes an image object in as a parameter and returns
# a 2D list representing the rgb values of each pixel
#   im: image object
def processImage(im):
    imArray = np.asarray(im)
    return imArray

def resizeImage(im):
    size = os.get_terminal_size()
    im = im.resize((size.columns, size.lines))
    return im

# Confirms that the image loaded successfully and prints the size
# of the image.  
#   imName:     image Name
#   imArray:    2D array of pixels
def printImageData(imName, imArray):
    print("Sucessfully loaded image '{0}'.".format(imName))
    print("Image size: {0} x {1}".format(len(imArray[0]), len(imArray)))
    print("Processing Image...")

# Converts a 2D array of pixles into a 2d array of brightness values
#   imArray:    2D array of pixels
#   type:       type of brightness conversion
#               0 -> Average
#               1 -> Lightness
#               2 -> Luminosity
def convertToBright(imArray, bType):
    imBrightArray = []
    i = 0
    for x in imArray:
        imBrightArray.append([])
        for y in x:
            brightVal = 0
            if bType == 0:
                for pixVals in y:
                    brightVal += pixVals
                brightVal = brightVal / 3
            elif bType == 1:
                brightVal = (max(y[0], y[1], y[2]) + min(y[0], y[1], y[2])) / 2
            elif bType == 2:
                brightVal = ((0.21 * y[0]) + (0.72 * y[1]) + (0.07 * y[2]))
            imBrightArray[i].append(brightVal)
        i += 1
    return imBrightArray

# Converts a 2D array of pixel brightness to ascii chracters and 
# returns a 2D array of characters
#   imBright:   2D array of pixel brightness
def brightnessToAscii(imBrightArray):
    asciiArray = []
    asciiChars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    i = 0
    for x in imBrightArray:
        asciiArray.append([])
        for y in x:
            stringIndex = int((y / 255) * (len(asciiChars) - 1))
            asciiArray[i].append(asciiChars[stringIndex])
        i += 1
    return asciiArray


# Takes a 2D array of ascii characters and prints it to the terminal
#   asciiArray: 2D array of ascii characters
def printAsciiImage(asciiArray):
    for x in asciiArray:
        for y in x:
            print(y, end="")
        print()

# Prints information to know how to run the program 
def printHelp():
    print("Usage: python3 ita.py [file] [arguments]")
    print("  -b: specifies the pixel to brightness conversion type. Valid options are 0:average, 1:Lightness, 2:Luminosity")

def main(argv):
    #argument handling
    if len(argv) == 0 :
        printHelp()
        return
    
    fileIndex = 0
    brightnessType = 0
    inc = 0
    for i in range(0, len(argv)):
        i += inc
        if i >= len(argv):
            break
        elif argv[i] == "-b":
            brightnessType = int(argv[i + 1])
            if brightnessType < 0 or brightnessType > 2:
                print("Please select 0-2 for brightness conversion type. Use -h for more information.")
                return
            inc = inc+1
        elif argv[i] == "-h":
            printHelp()
            return
        elif argv[i][0] == "-":
            print("Error: {0} is not a valid option".format(argv[i]))
            return
        else: 
            fileIndex = i 

        
    
    #file checking handling
    im = None
    try:
        im = Image.open(fp=argv[fileIndex], mode="r", formats=None)
    except FileNotFoundError:
        print("Could not find file '{0}'.".format(argv[fileIndex]))
        return
    except PIL.UnidentifiedImageError:
        print("Could not read file '{0}'. Please make sure it is a .jpg.".format(argv[fileIndex]))
        return
    
    #function calls
    im = resizeImage(im)
    imArray = processImage(im)
    printImageData(argv[fileIndex], imArray)
    imBrightArray = convertToBright(imArray, brightnessType)
    asciiArray = brightnessToAscii(imBrightArray)
    printAsciiImage(asciiArray)


if __name__ == "__main__":
    main(sys.argv[1:])