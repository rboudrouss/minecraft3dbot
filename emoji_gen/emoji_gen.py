import numpy as np
import cv2

"""
infos :
    emoji_resolution = 32x32
    size < 256 kb
    depth 1 : the depth things = 25% => 8px
    depth 2 : 4px
    depth 3 : 2px
    depth 4 : 1px
    discord_background_color = rgb(54,57,63)
    bloc_background_color = rgb(53,56,61)

goal :
    generate images in 32x32 with bloc_background_color with some weid depth things left and right
    (still don't know how to do the weird depth things)
        - just copie from the image (objectif.png) and past ?
        - idea 
            left and right : dégradé de rgb(19,20,22) to bloc_background_color
            up down : (don't freaking know)
"""
img = cv2.imread("objectif.jpg", 1)
print(img)
