'''
'''
# Import statements.
import dinner, imager#, sandbox

# Beginning of script.
menu_items = dinner.dinner_scraper()
imager.image_creator(menu_items, 1000, 1000)
