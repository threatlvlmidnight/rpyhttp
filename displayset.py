from sense_hat import SenseHat # hardware library
import utils #local module

sense = SenseHat()
sense.set_rotation(270)

# Convert text color inputs to rgb value tuples

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
    #else:
        #return (255, 255, 255)
    
    
    
def setRotation(rotation):
    rotation = utils.postParser(rotation)
    sense.set_rotation(int(rotation))
    
    
    
    
# Sets the SenseHat matrix to a solid color
def showColor(color, power):
    if power == "On":
        sense.clear(displayset.returnRGB(color))
    elif power == "Off":
        sense.clear()

# Shows a message on the SenseHat matrix
def showMessage(message, color, power):
    if utils.postParser(power) == "On":
        sense.show_message(utils.postParser(message), 0.075, returnRGB(utils.postParser(color)))
        #print(returnRGB(color))
    elif utils.postParser(power) == "Off":
        sense.clear()