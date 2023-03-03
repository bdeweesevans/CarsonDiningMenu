'''Notes:
Handles the downloading and parsing of website HTML. 
Returns the dinner menu items as a list.
'''
# Import statements.
import bs4, requests, lxml

def dinner_scraper():
    # HTML is downloaded and validity of download is checked
    res = requests.get('https://housing.uoregon.edu/carson-dining#dinner')
    res.raise_for_status()

    # lxml is called on the html file.
    tree = lxml.etree.HTML(res.text)

    # Feeds parser the path.
    divs = tree.xpath('/html/body/div[2]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/ul/child::*')
    
    # Finds number of children at path's location.
    counter = 0
    for div in divs:
        x = div.xpath('child::*')
        counter += 1    # counter variable referenced in navigating menu path.

    # bs4 is called on the html file.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Feeds parser the path.
    dinner_menu = soup.select(f'#block-views-fe66ae869509158158420587268374be > div > div > div.view-content > div:nth-child({counter})')
    rawHTML = str(dinner_menu[0])

    # Splits and isolates title names.
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
    
    # Final lines
    return foods