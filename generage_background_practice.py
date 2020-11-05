'''
generate_stripey_backgrounds.py: create 16:9 background for posting to twitter
3 November 2020
Vicki Langer (@vicki_langer) (heavily influenced by @alexwlchan) https://alexwlchan.net/2020/03/stripey-flag-wallpapers/
'''

from PIL import Image, ImageDraw, ImageFont


def create_background(colors):

    # image dimensions 16:9
    box_width = 1600
    box_height = 900

    # create blank image for twitter post
    box = Image.new("RGB", size=(box_width, box_height), color="#ffffff")  # test color
    draw = ImageDraw.Draw(box)

    # write in the twitter handle watermark thingy
    chosen_font = ImageFont.truetype('assets/Nunito-SemiBold.ttf', 60)
    twitter_handle = "@LGBTQotd"
    draw = ImageDraw.Draw(box)
    draw.text((28, 800), text=twitter_handle, fill=("#444"), font=chosen_font)

    # add transparent mask thingy to lighten image to help with a11y
    # TODO: add mask
    border_width = 100  # 100 works well with the text
    blank_area = (border_width, border_width, box_width-border_width, box_height-border_width)
    draw.rectangle(blank_area, fill="#ffffff")

    

    # give the box
    return box

# TODO: add function call to get_img_for_tweet.py
# TODO: add function to get_img_for_tweet.py to check contrast w/ WCAG standards




if __name__ == '__main__':
    for label, pride_colors in [
        # colors from schemecolor.com/tag/gender-flags
        ("progress", ["#ffffff", "#f7a8b8", "#55cdfc", "#603815", "#000000", "#d20605", "#ef9c00", "#ffe500", "#119f0b", "#031a9a", "#78028c"]),
        '''
        ("genderfluid", ["#F996B9", "#FFFFFF", "#CA28E3", "#333333", "#5861CD"]),
        ("aromantic", ["#5BBD60", "#BAD897", "#ffffff", "#BABABA", "#333333"]),
        ("asexual", ["#000000", "#a4a4a4", "#ffffff", "#810081"]),
        ("pansexual", ["#ff1b8d", "#ffda00", "#1bb3ff"]),
        ("trans", ["#55cdfc", "#f7a8b8", "#ffffff", "#f7a8b8", "#55cdfc"]),
        ("intersex", ["#ffda00", "#7a00ac"]),
        ("non-binary", ["#fff430", "#ffffff", "#9c59d1", "#000000"]),
        ("bear", ["#633800", "#d76300", "#ffde58", "#ffe7b5", "#555555", "#000000"]),
        ("genderqueer", ["#b77fdd", "#ffffff", "#48821e"]),
        ("polysexual", ["#f714ba", "#01d66a", "#1594f6"]),
        '''
    ]:
        box = create_background(colors=pride_colors)
        box.save(f"img_bg/practice_bg_{label}.jpg")
