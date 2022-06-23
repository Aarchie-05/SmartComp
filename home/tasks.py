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


@shared_task(bind=True)
def flipkart_best_deals(self):

    driver = webdriver.Chrome(executable_path=r'E:\SmartComp\Chrome Drivers\chromedriver.exe' ,options=options)
    driver.maximize_window()
     
    driver.get("https://www.flipkart.com/offers-list/top-offers?screen=dynamic&pk=themeViews%3DEvents-Topoffers%3ADeal"
           "-card~widgetType%3DdealCard~contentType%3Dneo&wid=4.dealCard.OMU_4&otracker=hp_omu_Top%2BOffers_4"
           "&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_wc_view-all_4")
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    items = driver.find_elements(
        By.XPATH,
        "//*[@class='_1FNrEw']"
    )
    titles = []
    discounts = []
    imgs = []
    links = []

    for item in items:
        try:
            title = item.find_element(
                By.XPATH,
                ".//*[@class='_3LU4EM']"
            ).text.strip()
            titles.append(title)
        except:
            titles.append(None)
        try:
            discount = item.find_element(
                By.XPATH,
                ".//*[@class='_2tDhp2']"
            ).text.strip()
            discounts.append(discount)
        except:
            discounts.append(None)
        try:
            img = item.find_element(
                By.XPATH,
                ".//*[@class='_396cs4 _3exPp9']"
            ).get_attribute('src')
            imgs.append(img)
        except:
            imgs.append(None)
        try:
            link = item.find_element(
                By.XPATH,
                ".//*[@class='_6WQwDJ']"
            ).get_attribute('href')
            links.append(link)
        except:
            links.append(None)

    driver.quit()

    data = {
        "Product Title": titles,
        "Offer": discounts,
        "Image Link": imgs,
        "Deal Link": links
    }

    json_data = pd.DataFrame(data).to_json()
    print(json_data)
    return json_data