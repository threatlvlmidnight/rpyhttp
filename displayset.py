import time
import sys
import utils #local module

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# Matrix configuration
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)


def returnRGB(color):
    colorx = color.casefold()
    if colorx == "red":
        return (255, 0, 0)
    elif colorx == "green":
        return (0, 255, 0)
    elif colorx == "blue":
        return (0, 0, 255)
    elif colorx == "blue":
        return (255, 255, 255)
    elif colorx == "lavender":
        return (215, 215, 235)
    else:
        return (255, 255, 255)
    
#def showText(text):
    #offscreen_canvas = matrix.CreateFrameCanvas()
    #font = graphics.Font()
    #font.LoadFont("../../../fonts/7x13.bdf")
    #textColor = graphics.color(255, 255, 255)
    #text = "Hello world"
    
    #while True:
        #offscreen_canvas.Clear()
            
    
#def setRotation(rotation):
    
    
    
    
    
# Sets the SenseHat matrix to a solid color
#def showColor(color, power):
    

# Shows a message on the SenseHat matrix
#def showMessage(post_body):
    