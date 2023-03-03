'''Colors
Background: 37, 36, 39
Stats Bar: 30, 31, 31
Box Outlines: 65, 65, 65
Text: 205, 204, 205
Lavender Text: 165, 168, 194
'''
# Import statements.
import time
from PIL import Image, ImageDraw, ImageFont

def image_creator(menu_items, image_width, image_height):
    # Creation of image objects and draw
    img = Image.new('RGB', (image_width, image_height), (37, 36, 39))
    draw = ImageDraw.Draw(img)

    # Data bar (scaled)
    draw.rectangle(
        (0, 0, image_width - 1, image_height * 0.07),
        fill=(30, 31, 31),
        outline=(65, 65, 65))

    # Data stats (scaled)
    unicode_text = u"Stats = "
    statsFont = ImageFont.truetype('assets/fonts/Inter-Regular.ttf', int(image_width * 0.024), encoding="unic")
    text_width, text_height = statsFont.getsize(unicode_text)
    draw.text((3, 2), f"Stats = Time: {time.ctime()}", font=statsFont, fill=(165, 168, 194))    #add stats like followers?
    draw.text((3 + text_width, image_height*0.034), "Code Repo: https://github.com/bdeweesevans/CarsonScraper", font=statsFont, fill=(165, 168, 194))

    # Logo (scaled)
    logo = Image.open('assets/program_images/logo.png')
    newsize = (int(image_width*0.069),int(image_height*0.069))
    logo = logo.resize(newsize)
    logo_width, logo_height = logo.size
    img.paste(logo, (image_width-logo_width, 1))

    # Menu title (scaled)
    unicode_text = u"Today's Menu:"
    titleFont = ImageFont.truetype('assets/fonts/Inter-Bold.ttf', int(image_width * 0.056), encoding="unic")
    text_width, text_height = titleFont.getsize(unicode_text)
    draw.text(((image_width/2)-(text_width/2), image_height * 0.08), "Today's Menu:", font=titleFont, fill=(205, 204, 205))

    # Menu items (unscaled)
    titleFont = ImageFont.truetype('assets/fonts/Inter-Medium.ttf', int(image_width * 0.036), encoding="unic")
    for item in range(len(menu_items)):
        draw.text((20, (item+3.5)*50), f"•{menu_items[item]}", font=titleFont, fill=(205, 204, 205))
                        #item+y: y controls item start pos

    # Shows and saves post image
    img.show()
    img.save("assets/post_images/image.jpg")
    return
