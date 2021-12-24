# ASCII IMAGE CONVERTER:

## DESCRIPTION

ita.py (Image to Ascii) is a python script that takes in any image and prints it out to the terminal in Ascii Art.
The image that gets printed will be **resized** to the full size of the **terminal window**.

**NOTE:**
    You can see the image more clearly by zooming out in the termininal.
    It is also reccomended to set your terminal window's transparency to 0.
        
        Zoom out 
        ` Crtl + - `
        
        Zoom in
        ` Crtl + Shift + + `

The program works by taking in an image file as a command line argument and converting it to a 2D array of pixels. 
Each pixel is then analyzed and converted to a brightness value using one of three methods: average, lightness, luminosity.
Then the program assigns each pixel's brightness value to a corresponding ascii value depending on how much space it takes up as a character.
In other words, since the terminal is has a black background the brightness to ascii conversion depends on how much white light each character gives 
out by how much space it takes up in the character's box. Finally, the 2D array of characters is printed. 

## INSTALLATION:

After the repository is downloaded, just type in the following to download the program's dependancies:

` pip install -r requirements.txt `

## BRIGHTNESS METHODS:

This program consists of 3 different brightness methods. A list as well as a quick description and how they are calulated is listed below:

* average: The average simply takes each RGB value and sums them up and divides them by 3. 
    ` (R + B + G) / 3 `
* lightness: The lightness takes the Maximum and the Minimum values of the RGB for a pixel then sums the two up and divides it by 2.
    ` (max(R, G, B) + min(R, G, B)) / 2 `
* luminosity: The Luminosity takes a weighted average of the RGB values.
    ` 0.21 R + 0.72 G + 0.07 B `


