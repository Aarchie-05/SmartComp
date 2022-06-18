from selenium import webdriver
from selenium.webdriver.common.by import By
from compare.models import FlipkartDeals


def flipkart_all_deals(driver, search_item):
    item = search_item.replace(" ", "+")
    BASE_SEARCH_URL = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=relevance"
    url = BASE_SEARCH_URL.format(item)

    driver.get(url)

    elements_type1 = driver.find_elements(
        By.XPATH,
        "//*[ @class='_1xHGtK _373qXS' ]"
    )
    elements_type2 = driver.find_elements(
        By.XPATH,
        "//*[ @class = '_2kHMtA' ]"
    )
    elements_type3 = driver.find_elements(
        By.XPATH,
        "//*[@class='_4ddWXP']"
    )

    if elements_type1:
        all_deals = search_type_1(elements_type1)
    if elements_type2:
        all_deals = search_type_2(elements_type2)
    if elements_type3:
        all_deals = search_type_3(elements_type3)
    return all_deals

def search_type_1(elements):
    all_deals = []
    for element in elements:
        deal = FlipkartDeals()
        try:
            company = element.find_element(
                By.XPATH,
                ".//*[ @class='_2WkVRV' ]"
            ).text.strip()
            deal.company = company
        except:
            deal.company = None
        try:
            is_assured = element.find_element(
                By.XPATH,
                ".//*[@class='_1a8UBa']"
            )
            deal.assured = True
        except:
            deal.assured = False
        try:
            title = element.find_element(
                By.XPATH,
                ".//*[@class='IRpwTa' or @class='IRpwTa _2-ICcC']"
            ).text
            deal.title = title
        except:
            deal.title = None

        try:
            price = element.find_element(
                By.XPATH,
                ".//*[@class='_30jeq3']"
            ).text
            deal.price = price
        except:
            deal.price = None  
        try:
            mrp = element.find_element(
                By.XPATH,
                ".//*[@class='_3I9_wc']"
            ).text
            deal.mrp = mrp  
        except:
            deal.mrp = None 
        try:
            discount = element.find_element(
                By.XPATH,
                ".//*[@class='_3Ay6Sb']"
            ).text[0:3]
            deal.discount = discount
        except:
            deal.discount = None
        try:
            img = element.find_element(
                By.XPATH,
                ".//*[@class='_2r_T1I']"
            ).get_attribute('src')
            deal.img = img
        except:
            deal.img = None
        try:
            item_link = element.find_element(
                By.XPATH,
                ".//*[@class='_2UzuFa']"
            ).get_attribute('href')
            deal.item_link = item_link
        except:
            deal.item_link = None 
        all_deals.append(deal)
    return all_deals

def search_type_2(elements):
    pass

def search_type_3(driver, elements):
    pass