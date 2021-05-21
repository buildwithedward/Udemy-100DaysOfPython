###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram


rgb_colors = []
colors = colorgram.extract(
    '/home/edward/Documents/learn.code.repeat/Udemy - 100DaysOfPython/Day-18/hirst-painting-start/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
