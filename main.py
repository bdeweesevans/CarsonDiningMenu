'''Notes:
Run this file to initiate the program.
'''
# Import statements.
import menuPuller, imageCreator, flickrAPI, instagramAPI

print('---Execution Begin.---')
# Collects menu items using menuPuller.py.
menu_items = menuPuller.dinner_scraper()

# Creates menu image using imageCreator.py.
imageCreator.image_creator(menu_items, 1000, 1000)

# Uploads image to Flickr using flickrAPI.py and returns download link.
flickr_image_link, uploaded_image_object = flickrAPI.uploadToFlickr()

# Uploads image to Instagram using instagramAPI.py.
instagramAPI.postInstagramImage(flickr_image_link)

# Deletes the image from Flickr cloud storage.
flickrAPI.removeFromFlickr(uploaded_image_object)

print('---Execution Complete.---')