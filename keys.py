'''Notes:
Python file contains dictionairy of all keys used in script.
Sole purpose is for privacy when publishing the code.
Same goes for existence of 'auth.txt'.
Instructions for finding keys are below.
'''
keys = {
 'flickr_api_key': '',
 'flickr_api_secret': '',
 'ig_user_id': '',
 'ig_user_access_token': '',
 }

'''
Instructions for getting your keys, written by me, Ben.
[upon getting said keys, paste them into respective locations above.]

Flickr API Key and Flickr API Secret Key:
1. Make a free Flickr account.
2. Apply for a 'non-commercial' API key.
3. Your app will be made. Note the API key and API Secret Key.
*Done*
    [Note that when running application for the first time, you will be prompted to authorize this program by following a link.
    Follow the link and paste the key into the terminal. 
    It will be saved and you will not have to repeat this again unless the key is later rvoked.
    Flickr OAuth keys do not expire.]

For Facebook (much more complicated)(by noting something, I mean write it down):
1. Create and convert a Facebook account to a Facebook Developer account.
2. Make a Facebook business page. (you do not need to verify it as a real business)
3. Create an Instagram Professional account that you would like to make your posts to. Do so by converting a new standard account to professional in account settings.
4. Link the Instagram page to the Facebook page. You must be logged into the FB page. Follow this link: 'https://www.facebook.com/settings?tab=linked_instagram'. Login to the Instagram with the account made in step 3.
5. Create a new App here: 'https://developers.facebook.com/apps/'. (You will need to assign it to the business page you made in step 2)
6. In your app's dashboard, 'setup' the 'Facebook Login' and 'Instagram Graph API' products. (usually this just means clicking 'setup'. Leave FB Login Settings as default.)
7. At the top of the dashboard, turn the 'App Mode' switch from 'Development' to 'Live'.
8. Also at the top of the dashboard, ensure the 'App type' says 'Business'.
9. Note your App ID and App Secret Key from the 'Basic' Settings, found from the app's dashboard.
10. Now, go to 'https://developers.facebook.com/tools/explorer/'
11. In the sidebar, select your Meta App, 'Get User Access Token, and the permissions
    pages_show_list
    instagram_basic
    instagram_manage_comments
    instagram_manage_insights
    instagram_content_publish
    pages_read_engagement
    pages_manage_posts
    public_profile
12. Generate and note the access token. It is a short-life token and lasts only 60 minutes.
13. Open your terminal and paste this and hit enter, after filling in ID, Secret Key & Auth Token information where it asks.
    curl -i -X GET "https://graph.facebook.com/{v16.0}/oauth/access_token?grant_type=fb_exchange_token&client_id={YOUR APP ID}&client_secret={YOUR APP SECRET KEY}&fb_exchange_token={THE SHORT TERM TOKEN YOU JUST GENERATED}"
14. Note your long-term Auth Token from the returned text. This token lasts 60 days. Regerate it by following steps 9-13.
15. You have now found your 'ig_user_access_token'. We aren't done yet.
16. Head over to 'https://business.facebook.com/settings/instagram-account-v2s/'
17. Note your App ID located in the menu path: 
    Business Settings> Accounts> Instagram accounts> [the account you want to post to]> ID: Text
18. Congrats! You now have all you need to authorize and post using the Instagram Graph API.
*Done*
'''