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
    else:
        return (255, 255, 255)