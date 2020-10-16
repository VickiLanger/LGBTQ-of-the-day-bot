# This code assume the current naming convention of files which is:
# # [1,1a,2,2a,3,3a,........,100,100a].

# Let's start ;)
import os
import os.path
import random

from get_tweet import get_tweet

from PIL import Image, ImageDraw, ImageFont
# This is a function returns a list of all images names
# Args:DIR (directory which holds the images) rtype:lst, containing strings of files name.


def images_list(DIR):
    return list([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

# This function choose a random image from the directory.
# Args:images (lst of file names), rtype:string (str file name)


def random_image(images):
    if(images == []):
        return ''
    return random.choice(images)
# Test:
# print(random_image(images))
# print(f'{DIR}/{random_image(images)}')


def write_centre(image, text):
    draw = ImageDraw.Draw(image)
    draw.text(xy=(450, 325), text=text, fill=(11, 60, 73), font=font_type2)


def write_line(image, text, x, y):
    draw = ImageDraw.Draw(image)
    draw.text(xy=(x, y), text=text, fill=(11, 60, 73), font=font_type)
    draw.text(xy=(x, y+35), text=" ", fill=(11, 60, 73), font=font_type)
    draw.text(xy=(x, y+35), text=" ", fill=(11, 60, 73), font=font_type)


# Args:text/tweet , rtype:lst[imageObject,filenam(str)]
def write_on_image(text):
    file = random_image(images)
    image = Image.open(f'{DIR}/{file}')
    i = 0

    # changed default x, y values so that the else part shows up in center

    x = (image.width/2) - 260
    y = 380

    if(len(text) > 286):
        return [image, file]
    elif(len(text) < 20):
        write_centre(image, text)
    else:
        divisions = len(text)//35
        remainder = len(text)-divisions*35
        start_index = 0
        for i in range(divisions+1):
            line = text[:35]
            if i == divisions:
                write_line(image, text[:], x, y)
            write_line(image, line[:line.rfind(' ')], x, y)
            text = text.replace(line[:line.rfind(' ')+1], "")
            y += 35
    return [image, file]

# Now we have an aray contain an image object returned so we can pass it into a function to tweet or to save locally with
# the returned file name arr[1]

# Driver program to test all above functions:


DIR = 'img_bg'
OUT_DIR = 'img_post'

images = images_list(DIR)
font_type = ImageFont.truetype('assets/Nunito-Regular.ttf', 40)
font_type2 = ImageFont.truetype('assets/Nunito-Regular.ttf', 40*2)


def get_img_for_tweet(tweet_text):
    image = Image.open(f'{DIR}/{random_image(images)}')
    new_image = write_on_image(tweet_text)
    new_image_path = f'{OUT_DIR}/post_{new_image[1]}'
    new_image[0].save(f'{new_image_path}')
    return new_image_path
