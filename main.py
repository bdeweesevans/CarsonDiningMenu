'''Notes:
Run this file to initiate the program.
'''
# Import statements.
import MenuPuller, ImageCreator, FlickrAPI, InstagramAPI

print('---Execution Begin.---')

# Collects menu items using menuPuller.py.
menu_items, menu_titles = MenuPuller.dinner_scraper()

# Creates menu image using imageCreator.py.
ImageCreator.image_creator(menu_items, 1000, 1000)

# Uploads image to Flickr using flickrAPI.py and returns download link.
flickr_image_link, uploaded_image_object = FlickrAPI.uploadToFlickr()

# Uploads image to Instagram using instagramAPI.py.
InstagramAPI.postInstagramImage(flickr_image_link, menu_titles)

# Deletes the image from Flickr cloud storage.
FlickrAPI.removeFromFlickr(uploaded_image_object)

print('---Execution Complete.---')