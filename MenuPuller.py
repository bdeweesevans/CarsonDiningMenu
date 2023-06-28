'''Notes:
Handles the downloading and parsing of website HTML. 
Returns the dinner menu items as a list.
'''
# Import statements.
import bs4, requests, lxml, MenuTitles

def dinner_scraper():
    # HTML is downloaded and validity of download is checked
    res = requests.get('https://housing.uoregon.edu/carson-dining#dinner')
    res.raise_for_status()

    # bs4 is called on the html file.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # lxml is called on the html file.
    tree = lxml.etree.HTML(res.text)

    # Feeds parser the path.
    divs = tree.xpath('/html/body/div[2]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/ul/child::*')
    
    # Finds number of children at path's location.
    counter = 0
    for div in divs:
        x = div.xpath('child::*')
        counter += 1    # counter variable referenced in navigating menu path.

    # if statement to ensure dinner category exists
    last_category = tree.xpath(f'/html/body/div[2]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/ul/li[{counter}]/a/text()')
    if len(last_category)==1:
        if ((last_category[0]) == 'Dinner'):
            # Feeds parser the path.
            dinner_menu = soup.select(f'#block-views-fe66ae869509158158420587268374be > div > div > div.view-content > div:nth-child({counter})')
            rawHTML = str(dinner_menu[0])

            # Splits and isolates title names. (Unused)
            splitTitles = rawHTML.split("</p>")
            titles = []
            for splitTitle in splitTitles:
                arr = splitTitle.split(">")
                elem = arr[len(arr) - 1]
                if (len(elem) > 0):
                    titles.append(elem)

            # Splits and isolates food names.
            splitFoods = rawHTML.split("</strong>")
            foods = []
            for splitFood in splitFoods:
                arr = splitFood.split(">")
                elem = arr[len(arr) - 1]
                if (len(elem) > 0):
                    foods.append(elem)
            
            # Resolves '&amp;', '\n', and '\t' issue.
            for i in range(len(foods)):
                foods[i] = foods[i].replace('amp;','')
                foods[i] = foods[i].replace('\n','')
                foods[i] = foods[i].replace('\t','')
                
            for i in range(len(titles)):
                titles[i] = titles[i].replace('amp;','')

            #========================================================
            # Grossly Fixes New Issues with Carsons HTML Updates. 
            # dont have time to do this properly, works for now.
            # Removes titles from foods list and other stuff.
            removal_list = []
            for i in range(len(foods)):
                for elem in range(len(MenuTitles.titles)):
                    if (MenuTitles.titles[elem] in foods[i].lower()):
                        titles.append(foods[i])
                        removal_list.append(foods[i])

            for i in range(len(removal_list)):
                foods.remove(removal_list[i])
            
            while 'contains soy' in foods:
                foods.remove('contains soy')
            while 'contains milk' in foods:
                foods.remove('contains milk')
            
            # Removes the random stuff before the real titles. This is disgusting. I hate this code.
            #print(titles)
            titles.pop(0)
            titles.pop(0)
            #print(titles)
            #========================================================

            # Final lines
            dinner_validity = True
            return foods, titles, dinner_validity
        
        else:
            foods, titles = [], []
            dinner_validity = False
            return foods, titles, dinner_validity
    else:
        foods, titles = [], []
        dinner_validity = False
        return foods, titles, dinner_validity