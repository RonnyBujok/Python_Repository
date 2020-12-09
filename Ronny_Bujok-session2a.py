# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 or 3:4 and resized to be all the same size

# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape oriented images

# Steps
# 0. Create a new folder
# 1. Define portrait and landscape images
# 2. Figure out on which side you have to crop the image
# 3. Crop the image
# 4. Resize the image
# 5. Save it to your new folder with the new extension. That's it!


from PIL import Image
from PIL import ImageFilter
import os


# directory
folder = "C:\\Users\\Ronny\\Desktop\\session2a-image\\raw"


# make a new folder
new_folder = "C:\\Users\\Ronny\\Desktop\\processed\\"
#os.mkdir(new_folder)

img_list = os.listdir(folder)

landscape = []
portrait = []


for i in img_list:
    # load an image
    img_path = os.path.join(folder, i)
    img = Image.open(img_path)
    height = img.height
    width = img.width
    # split extension
    filename, extension = os.path.splitext(i)
    #filename now contains the name without the extension

    #checks whether it is landscape or portrait and then crops it in the right ratio and resizes it to the same size
    if width > height:
        landscape.append(i)
        new_width = height/3*4
        difference = width-new_width
        img_crop = img.crop((difference/2,0,width-(difference/2),height))
        img_crop_rsz = img_crop.resize((400, 300))
        img_crop_rsz.show()
    else:
        portrait.append(i)
        new_height = width/3*4
        difference = height-new_height
        img_crop = img.crop((0,difference/2,width,height-(difference/2),))
        img_crop_rsz = img_crop.resize((300, 400))
        img_crop_rsz.show()

# output the edited pictures as png in the new folder
    outfile = new_folder + filename + ".png"  # string concatenation
    print(outfile)

    img_crop_rsz.save(outfile, "PNG")





