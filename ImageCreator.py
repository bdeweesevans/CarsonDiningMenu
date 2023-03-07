'''Notes:
Handles the creation of the menu image.

Colors =
Background: 37, 36, 39
Stats Bar: 30, 31, 31
Box Outlines: 65, 65, 65
Text: 205, 204, 205
Lavender Text: 165, 168, 194
Icon Red: 228,36,52
Icon Yellow: 244, 196, 44
'''
# Import statements.
import time, datetime
from PIL import Image, ImageDraw, ImageFont

# Declarations for day of the week.
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dt = datetime.datetime.now()
day = dt.weekday()

# Declarations for words we have images for.
basic_food_words = ['Waffle', 'Egg', 'Beans','Beef','Broccoli','Chicken','Corn','Gnocci','Mushrooms',
                    'Noodles','Pollo','Bacon','Rice','Shrimp','Sweet','Tamales','Tofu',
                    'Vegetables','Verde']
selected_image_words = []

def image_creator(menu_items, dinner_validity, image_width, image_height):
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
    draw.text((3 + text_width, image_height*0.034), "Codebase: https://github.com/bdeweesevans/CarsonDiningMenu", font=statsFont, fill=(165, 168, 194))

    # Icon (scaled)
    icon = Image.open('assets/program_images/icon.png')
    newsize = (int(image_width*0.069),int(image_height*0.069))
    icon = icon.resize(newsize)
    icon_width, icon_height = icon.size
    img.paste(icon, (image_width-icon_width, 1))

    # Menu title (scaled)
    unicode_text = u"Today's Menu:"
    titleFont = ImageFont.truetype('assets/fonts/Inter-Bold.ttf', int(image_width * 0.07), encoding="unic")
    title_width, title_height = titleFont.getsize(unicode_text)
    draw.text(((image_width/2)-(title_width/2), image_height * 0.085), "Today's Menu:", font=titleFont, fill=(244, 196, 44))

    # Day of the week title (scaled)
    unicode_text = f'{days[day]}'
    dayFont = ImageFont.truetype('assets/fonts/Inter-Bold.ttf', int(image_width * 0.0675), encoding="unic")
    day_width, day_height = dayFont.getsize(unicode_text)
    draw.text(((image_width/2)-(day_width/2), image_height * 0.17), f"{days[day]}", font=dayFont, fill=(244, 196, 44))

    # Checks if there even is dinner that day.
    if(dinner_validity == True):
        # Creates image of no food if Dinner header exists but there's no data.
        if (len(menu_items) == 0):
            # No Data text (Scaled)
            unicode_text = u"No menu data provided by university :("
            noDataFont = ImageFont.truetype('assets/fonts/Inter-Medium.ttf', int(image_width * 0.04), encoding="unic")
            noData_width, noData_height = noDataFont.getsize(unicode_text)
            draw.text(((image_width/2)-(noData_width/2), image_height * 0.25), "No menu data provided by university :(", font=noDataFont, fill=(205, 204, 205))

            # No Data null image (Scaled)
            nullImage = Image.open('assets/program_images/unknown.jpg')
            newsize = (int(image_width*0.6),int(image_height*0.6))
            nullImage = nullImage.resize(newsize)
            nullImage_width, nullImage_height = nullImage.size
            img.paste(nullImage, (int((image_width/2)-(nullImage_width/2)), int(image_height * 0.305)))
        
        # Adds the food pictures and text
        else:
            # for loops find the words that we have photos for
            for i in range(len(menu_items)):
                for j in basic_food_words:
                    if j in menu_items[i]:
                        selected_image_words.append(j)

            # Menu items (Scaled)
            itemFont = ImageFont.truetype('assets/fonts/Inter-Medium.ttf', int(image_width * 0.036), encoding="unic")
            for i in range(8):
                if (i < len(menu_items)):
                    unicode_text = f'{menu_items[i]}'
                    item_width, item_height = itemFont.getsize(unicode_text)
                    draw.text(((image_width/2)-(item_width/2), (i+11.2)*50), f"{menu_items[i]}", font=itemFont, fill=(205, 204, 205))

            # Food image selectors.
            unknown = Image.open(f'assets/food_images/noimage.jpg')
            if (len(selected_image_words)>=3):
                foodImage1 = Image.open(f'assets/food_images/{selected_image_words[1].lower()}.jpg')
                foodImage2 = Image.open(f'assets/food_images/{selected_image_words[0].lower()}.jpg')
                foodImage3 = Image.open(f'assets/food_images/{selected_image_words[2].lower()}.jpg')
            elif (len(selected_image_words)==2):
                foodImage1 = Image.open(f'assets/food_images/{selected_image_words[1].lower()}.jpg')
                foodImage2 = Image.open(f'assets/food_images/{selected_image_words[0].lower()}.jpg')
                foodImage3 = unknown
            elif (len(selected_image_words)==1):
                foodImage1 = unknown
                foodImage2 = Image.open(f'assets/food_images/{selected_image_words[0].lower()}.jpg')
                foodImage3 = unknown
            else:
                foodImage1 = unknown
                foodImage2 = unknown
                foodImage3 = unknown
            newsize = (int(image_width*0.25),int(image_height*0.25))  

            # Food Image Left image (Scaled)
            foodImage1 = foodImage1.resize(newsize)
            foodImage1_width, foodImage1_height = foodImage1.size
            img.paste(foodImage1, (int((image_width/10)*1), int(image_height * 0.285)))

            # Food Image Middle image (Scaled)
            foodImage2 = foodImage2.resize(newsize)
            foodImage2_width, foodImage2_height = foodImage2.size
            img.paste(foodImage2, (int((image_width/2)-(foodImage2_width/2)), int(image_height * 0.285)))

            # Food Image Right image (Scaled)
            foodImage3 = foodImage3.resize(newsize)
            foodImage3_width, foodImage3_height = foodImage3.size
            img.paste(foodImage3, (int((image_width/10)*6.5), int(image_height * 0.285)))
    
    #triggers if there is no dinner that day
    else:
        # No Data text (Scaled)
        unicode_text = u"There is no dinner today at Carson."
        noDataFont = ImageFont.truetype('assets/fonts/Inter-Medium.ttf', int(image_width * 0.04), encoding="unic")
        noData_width, noData_height = noDataFont.getsize(unicode_text)
        draw.text(((image_width/2)-(noData_width/2), image_height * 0.25), "There is no dinner today at Carson", font=noDataFont, fill=(205, 204, 205))

        # No Data null image (Scaled)
        nullImage = Image.open('assets/program_images/fridge.jpg')
        newsize = (int(image_width*0.6),int(image_height*0.6))
        nullImage = nullImage.resize(newsize)
        nullImage_width, nullImage_height = nullImage.size
        img.paste(nullImage, (int((image_width/2)-(nullImage_width/2)), int(image_height * 0.305)))
    
    # Shows and saves post image
    #img.show()
    img.save("assets/post_images/image.jpg")
    return
