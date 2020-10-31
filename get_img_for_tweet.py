# This code assume the current naming convention of files which is:
# # [1,1a,2,2a,3,3a,........,100,100a].

# Let's start ;)
import os
import os.path
import random
import textwrap

from get_tweet import get_tweet

from PIL import Image, ImageDraw, ImageFont  # type: ignore
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
    # use the text size to determine the x and y axis
    x, y = font_type2.getsize(text)
    draw.text(((1600-x)/2, (900-y)/2), text=text, fill=(11, 60, 73), font=font_type2)


def write_line(image, text, x, y):
    draw = ImageDraw.Draw(image)
    draw.text(((1600-x)/2, (900-y)/2), text=text, fill=(11, 60, 73), font=font_type)


# Args:text/tweet , rtype:lst[imageObject,filenam(str)]
def write_on_image(text):
    file = random_image(images)
    image = Image.open(f'{DIR}/{file}')

    if(len(text) > 286):
        return [image, file]
    elif(len(text) < 20):
        write_centre(image, text)
    else:
        # use the python wrap text function to wrap text by words on maximum of 35 charaters.
        wrapped_lines = textwrap.wrap(text, 35)

        x, y = font_type.getsize(wrapped_lines[0])
        # offset y for the number of lines in the list
        y = y + len(wrapped_lines)*80
        for line in wrapped_lines:
            x, h = font_type.getsize(line)
            write_line(image, line, x, y)
            y -= 160
    return [image, file]

# Now we have an array contain an image object returned so we can pass it into a function to tweet or to save locally with
# the returned file name arr[1]

# Driver program to test all above functions:


DIR = 'img_bg'
OUT_DIR = 'img_post'

images = images_list(DIR)

fonts = (os.listdir('assets'))  # list of all fonts in asset folder

font_type = ImageFont.truetype('assets/'+random.choice(fonts), 80)
font_type2 = ImageFont.truetype('assets/'+random.choice(fonts), 80*2)


def get_img_for_tweet(tweet_text):
    image = Image.open(f'{DIR}/{random_image(images)}')
    new_image = write_on_image(tweet_text)
    new_image_path = f'{OUT_DIR}/post_{new_image[1]}'
    new_image[0].save(f'{new_image_path}')
    return new_image_path
