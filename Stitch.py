from PIL import Image
import PIL

#Place two PNGs named "left" and "right" into the folder that this python file is in.
#This script will combine the files in respective order into an output image called "Stitched.png"


left = Image.open('left.png') #initializes left and right images
right = Image.open('right.png')

width, height = left.size #sets left and right width + height values
width2, height2 = right.size
combindedWidth = width+width2 #combines width values

#sets the final image height to be the greater of the two heights
if height < height2: 
    trueHeight = height2
else:
    trueHeight = height
stitchedSize = combindedWidth, trueHeight

#creates blank image of dimensions: W = combinedleft+right width, H = greater of the two source image heights
stitched = PIL.Image.new(mode="RGBA", size=stitchedSize, color=0) 

#pastes the two images onto the final image in order
stitched.paste(left, box=None, mask=None)
stitched.paste(right, box=(width, 0) ,mask=None)


stitched.save("Stitched.png")
stitched.show()
