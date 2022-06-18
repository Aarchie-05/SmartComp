import os
from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from compare.flipkart_deals import *

# Create your views here.

# os.environ['PATH'] += r"C:\Selenium Drivers\chromedriver_win32"
options = webdriver. ChromeOptions()
options.add_argument("- incognito")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument ("--no-sandbox")

driver = webdriver.Chrome(executable_path=r'E:\SmartComp\Chrome Drivers\chromedriver.exe' ,options=options)

def compare(request):
    return render(request, 'compare.html')

def search(request):
    search_item = request.GET['search_item']
    deal2 = flipkart_top_deal(search_item)
    all_deals_flipkart = flipkart_all_deals(driver, search_item)
    deals2_index = list(range(0,len(all_deals_flipkart)))
    return render(request, 'compare.html', {'deal2':deal2, 'deals2':all_deals_flipkart})

def flipkart_top_deal(search_item):
    item = search_item.replace(" ", "+")
    BASE_SEARCH_URL = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=relevance"
    url = BASE_SEARCH_URL.format(item)

    driver.get(url)

    top_item_link = driver.find_element(
    By.XPATH,
    "//*[@class='IRpwTa' or @class='s1Q9rs' or @class='_1fQZEK']"
    ).get_attribute('href')
    driver.get(top_item_link)

    deal_data = {}

    def get_offers():
        offers_available = []
        offers = driver.find_elements(
            By.XPATH,
            "//*[@class='_16eBzU col']"
        )
        for offer in offers:
            offers_available.append(offer.text.strip())
        return offers_available

    try:
        company = driver.find_element(
            By.XPATH,
            "//*[@class='G6XhRU']"
        ).text.strip()
    except:
        company = None
    deal_data['company'] = company
    try:
        title = driver.find_element(
            By.XPATH,
            "//*[@class='B_NuCI']"
        ).text.strip()
    except:
        title = None
    deal_data['title'] = title
    try:
        price = driver.find_element(
            By.XPATH,
            "//*[@class='_30jeq3 _16Jk6d']"
        ).text.strip()
    except:
        price = None
    deal_data['price'] = price
    try:
        mrp = driver.find_element(
            By.XPATH,
            "//*[@class='_3I9_wc _2p6lqe']"
        ).text.strip()
    except:
        mrp = None
    deal_data['mrp'] = mrp
    try:
        discount = driver.find_element(
            By.XPATH,
            "//*[@class='_3Ay6Sb _31Dcoz pZkvcx' or @class='_3Ay6Sb _31Dcoz']"
        ).text.strip()[:4].strip()
    except:
        discount = None
    deal_data['discount'] = discount
    try:
        rating = driver.find_element(
            By.XPATH,
            "//*[@class='_3LWZlK _3uSWvT' or @class='_3LWZlK']"
        ).text.strip()
    except:
        rating = None
    deal_data['rating'] = rating
    try:
        no_of_ratings = driver.find_element(
            By.XPATH,
            "//*[@class='_2_R_DZ']"
        ).text.strip()
        no_of_ratings = no_of_ratings[0:no_of_ratings.index(' ')]
    except:
        no_of_ratings = None
    deal_data['no_of_ratings'] = no_of_ratings
    try:
        isAssured = driver.find_element(
            By.XPATH,
            "//*[@class='b7864- _2Z07dN']"
        )
        isAssured = True
    except:
        isAssured = False
    deal_data['is_assured'] = isAssured
    try:
        img = driver.find_element(
            By.XPATH,
            "//*[@class='_2r_T1I _396QI4' or @class='_396cs4 _2amPTt _3qGmMb  _3exPp9']"
        ).get_attribute('src')
    except:
        img = None  
    deal_data['img'] = img
    try:
        more_offers = driver.find_element(
            By.XPATH,
            "//*[@class='IMZJg1 Okf99z' or @class='IMZJg1']"
        )
        more_offers.click()
        offers = get_offers()
        print("clicked")
    except:
        offers = get_offers()
    deal_data['offers'] = offers
    #deal_data = json.loads(str(deal_data)+'')

    return deal_data
