import time
import pandas as pd
from celery import shared_task
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("- incognito")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument ("--no-sandbox")

@shared_task(bind=True)
def amazon_best_deals(self):

    driver = webdriver.Chrome(executable_path=r'E:\SmartComp\Chrome Drivers\chromedriver.exe' ,options=options)
    driver.maximize_window()

    driver.get('https://www.amazon.in/gp/goldbox')
    
    all_deals = driver.find_elements(by=By.XPATH, value='//div[@aria-label="Deals grid"]//div[@data-testid="deal-card"]')

    title = []
    img = []
    discount = []
    deal_url = []
    for deal in all_deals:
        try:
            deal_url.append(deal.find_element(by=By.XPATH, value='.//a').get_attribute('href'))
        except:
            continue
        try:
            img.append(deal.find_element(by=By.XPATH, value='.//img').get_attribute('src'))
        except:
            img.append(None)
        try:
            title.append(deal.find_element(by=By.XPATH, value=".//div[contains(@class, 'DealContent')]").text)
        except:
            title.append(None)
        try:
            discount.append(deal.find_element(by=By.XPATH,
                                            value='.//a[not(.//img) and not(.//div[contains(@class, "DealContent")])]').text.split(
                '\n')[0].strip())
        except:
            discount.append(None)

    driver.quit()

    data = {
        'Product Title': title,
        'Offer': discount,
        'Image Link': img,
        'Deal Link': deal_url
    }

    json_data = pd.DataFrame(data).to_json()
    print(json_data)
    return json_data


@shared_task(bind=True)
def snapdeal_best_deals(self):

    driver = webdriver.Chrome(executable_path=r'E:\SmartComp\Chrome Drivers\chromedriver.exe' ,options=options)
    driver.maximize_window()
        
    driver.get('https://www.snapdeal.com/offers/half_price_store')

    all_deals = driver.find_elements(by=By.XPATH, value="//div[normalize-space(@class)='cardRow']/div[contains(@class, 'cardProd')]")

    title = []
    img = []
    mrp = []
    sp = []
    discount = []
    deal_url = []
    for deal in all_deals:
        try:
            deal_url.append(deal.find_element(by=By.XPATH, value=".//a").get_attribute('href'))
        except:
            continue

        try:
            img.append(deal.find_element(by=By.XPATH, value=".//img").get_attribute('src'))
        except:
            img.append(None)

        try:
            mrp.append(deal.find_element(by=By.XPATH, value=".//span[contains(@class, 'price_disc')]").text)
        except:
            mrp.append(None)

        try:
            sp.append(deal.find_element(by=By.XPATH, value=".//span[contains(@class, 'price_actl')]").text)
        except:
            sp.append(None)

        try:
            discount.append(deal.find_element(by=By.XPATH, value=".//div[contains(@class, 'cardProductTagDisc')]").text)
        except:
            discount.append(None)

        try:
            title.append(deal.find_element(by=By.XPATH, value=".//div[contains(@class, 'cardProd_name')]").text)
        except:
            title.append(None)

    driver.quit()

    data = {
        'Product Title': title,
        'MRP': mrp,
        'Price': sp,
        'Discount': discount,
        'Image Link': img,
        'Deal Link': deal_url
    }
    
    json_data = pd.DataFrame(data).to_json()
    print(json_data)
    return json_data
