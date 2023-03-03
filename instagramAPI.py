'''Notes:
Handles the uploading of the menu image to Instagram.
'''
import requests, json, time, keys

ig_user_id = keys.keys['ig_user_id']
user_access_token = keys.keys['ig_user_access_token']

def postInstagramImage(flickr_image_link):
    # Creates post object
    image_location_1 = flickr_image_link
    post_url = 'https://graph.facebook.com/v16.0/{}/media'.format(ig_user_id)
    payload = {
        'image_url': image_location_1,
        'caption': f'Dindin!\nToday\'s Date:\n{time.ctime()}\nDeveloped by @bdeweesevans',
        'access_token': user_access_token
    }
    r = requests.post(post_url, data=payload)
    print(f'Instagram Image Bin: {r.text}')
    result = json.loads(r.text)

    # Deliveres post object, uploading.
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v16.0/{}/media_publish'.format(ig_user_id)
        second_payload = {
        'creation_id': creation_id,
        'access_token': user_access_token
        }
        r = requests.post(second_url, data=second_payload)
        print('Instagram Image: Uploaded')
        print(f'Instagram Image Post: {r.text}')
    else:
        print('Instagram Error: HOUSTON we have a problem')