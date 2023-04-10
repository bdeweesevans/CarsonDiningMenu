'''Notes:
Run this file to initiate the program to execute manually. (you will have to call main.)
'''
# Import statements.
import MenuPuller, ImageCreator, FlickrAPI, InstagramAPI, time

def main():
    print('---Execution Begin.---')
    print(f'Data Point #1: {time.ctime()}')

    # Collects menu items using menuPuller.py.
    menu_items, menu_titles, dinner_validity = MenuPuller.dinner_scraper()

    # Creates menu image using imageCreator.py.
    ImageCreator.image_creator(menu_items, dinner_validity, 1000, 1000)

    # Uploads image to Flickr using flickrAPI.py and returns download link.
    flickr_image_link, uploaded_image_object = FlickrAPI.uploadToFlickr()

    # Uploads image to Instagram using instagramAPI.py.
    InstagramAPI.postInstagramImage(flickr_image_link, menu_titles)

    # Deletes the image from Flickr cloud storage.
    FlickrAPI.removeFromFlickr(uploaded_image_object)

    print(f'Data Point #2: {time.ctime()}')
    print('---Execution Complete.---')

# Uncomment this line to run this file manually.
main()