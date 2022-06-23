import json
import re
import time

from bs4 import BeautifulSoup
from celery import shared_task

from selenium import webdriver
from selenium.webdriver.common.by import By
from .models import FlipkartDeals
import lxml
import pandas as pd

options = webdriver. ChromeOptions()
options.add_argument("- incognito")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument ("--no-sandbox")

driver = webdriver.Chrome(executable_path=r'E:\SmartComp\Chrome Drivers\chromedriver.exe' ,options=options)


# testing functions
@shared_task(bind=True)
def getData(self): 
    print("Task Completed")
    c = add(2,3)
    return c

@shared_task(bind=True)
def add(self, a, b):
    return a + b
# testing functions end

@shared_task(bind=True)
def get_search_url(self, store, search):
    if store == 'flipkart':
        item = search.replace(" ", "+")
        BASE_SEARCH_URL = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=relevance"
        url = BASE_SEARCH_URL.format(item)
        return url
    elif store == 'amazon':
        item = search.strip()
        url = 'https://www.amazon.in/s?k=' + item
        return url
    elif store == 'snapdeal':
        item = search.strip()
        url = 'https://www.snapdeal.com/search?keyword=' + item
        return url

@shared_task(bind=True)
def get_offers(self):
    offers_available = []
    offers = driver.find_elements(
        By.XPATH,
        "//*[@class='_16eBzU col']"
    )
    for offer in offers:
        offers_available.append(offer.text.strip())
    return offers_available
    
@shared_task(bind=True)
def flipkart_primary_deal(self, search):
    url = get_search_url('flipkart', search)
    driver.get(url)
    top_item_link = driver.find_element(
    By.XPATH,
    "//*[@class='IRpwTa' or @class='s1Q9rs' or @class='_1fQZEK']"
    ).get_attribute('href')
    driver.get(top_item_link)

    deal_data = {}

    deal_data['item_link'] = top_item_link

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

    print(deal_data)

    return deal_data


@shared_task(bind=True)
def flipkart_other_deals(self, search):
    print("ppppppppppppppppppppppppppppppppppppppppppppppppppppp")
    item = search.replace(" ", "+")
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
    
    print(all_deals)
    return all_deals


@shared_task(bind=True)
def search_type_1(self, elements):
    all_deals = []
    for element in elements:
        deal = {}
        try:
            company = element.find_element(
                By.XPATH,
                ".//*[ @class='_2WkVRV' ]"
            ).text.strip()
            deal['company'] = company
        except:
            deal['company'] = None
        try:
            is_assured = element.find_element(
                By.XPATH,
                ".//*[@class='_1a8UBa']"
            )
            deal['assured'] = 'true'
        except:
            deal['assured'] = 'false'
        try:
            title = element.find_element(
                By.XPATH,
                ".//*[@class='IRpwTa' or @class='IRpwTa _2-ICcC']"
            ).text
            deal['title'] = title
        except:
            deal['title'] = None

        try:
            price = element.find_element(
                By.XPATH,
                ".//*[@class='_30jeq3']"
            ).text
            deal['price'] = price
        except:
            deal['price'] = None
        try:
            mrp = element.find_element(
                By.XPATH,
                ".//*[@class='_3I9_wc']"
            ).text
            deal['mrp'] = mrp
        except:
            deal['mrp'] = mrp
        try:
            discount = element.find_element(
                By.XPATH,
                ".//*[@class='_3Ay6Sb']"
            ).text[0:3]
            deal['discount'] = discount
        except:
            deal['discount'] = None
        try:
            img = element.find_element(
                By.XPATH,
                ".//*[@class='_2r_T1I']"
            ).get_attribute('src')
            deal['img'] = img
        except:
            deal['img'] = img
        try:
            item_link = element.find_element(
                By.XPATH,
                ".//*[@class='_2UzuFa']"
            ).get_attribute('href')
            deal['item_link'] = item_link
        except:
            deal['item_link'] = item_link
        deal['rating'] = None
        deal['no_of_rating'] = None
        deal['description'] = None
        all_deals.append(deal)
        print("------------------------------------------------------------------------------------------------")
    return all_deals

@shared_task(bind=True)
def search_type_2(self, elements):
    all_deals = []
    for element in elements:
        deal = {}
        deal['company'] = None
        try:
            is_assured = element.find_element(
                By.XPATH,
                ".//*[@class='_13J9qT']"
            )
            deal['assured'] = 'true'
        except:
            deal['assured'] = 'false'
        try:
            title = element.find_element(
                By.XPATH,
                ".//*[@class='_4rR01T']"
            ).text.strip()
            deal['title'] = title
        except:
            deal['title'] = title
        try:
            price = element.find_element(
                By.XPATH,
                ".//*[@class='_30jeq3 _1_WHN1']"
            ).text.strip()
            deal['price'] = price
        except:
            deal['price']  = None
        try:
            mrp = element.find_element(
                By.XPATH,
                ".//*[@class='_3I9_wc _27UcVY']"
            ).text.strip()
            deal['mrp'] = mrp
        except:
            deal['mrp'] = mrp
        try:
            discount = element.find_element(
                By.XPATH,
                ".//*[@class='_3Ay6Sb']"
            ).text[0:3].strip()
            deal['discount'] = discount
        except:
            deal['discount'] = None
        try:
            img = element.find_element(
                By.XPATH,
                ".//*[@class='_396cs4 _3exPp9']"
            ).get_attribute('src')
            deal['img'] = img
        except:
            deal['img'] = img
        try:
            item_link = element.find_element(
                By.XPATH,
                ".//*[@class='_1fQZEK']"
            ).get_attribute('href')
            deal['item_link'] = item_link
        except:
            deal['item_link'] = item_link
        try:
            rating = element.find_element(
                By.XPATH,
                ".//*[@class='_3LWZlK']"
            ).text.strip()
            deal['rating'] = rating
        except:
            deal['rating'] = None
        try:
            count = element.find_element(
                By.XPATH,
                ".//*[@class='_2_R_DZ']"
            ).text
            deal['no_of_rating'] = count
        except:
            deal['no_of_rating'] = None
        try:
            i = 1
            description = []
            while i < 6:
                desc = element.find_element(
                    By.XPATH,
                    f".//*[@class='rgWa7D'][{i}]"
                ).text.strip()
                i = i + 1
                description.append(desc)
            deal['description'] = desc
        except:
            deal['description'] = None
        all_deals.append(deal)
        print("------------------------------------------------------------------------------------------------")
    return all_deals

@shared_task(bind=True)
def search_type_3(self, elements):
    print("okokok")
    all_deals = []
    for element in elements:
        deal = {}
        deal['company'] = None
        try:
            is_assured = element.find_element(
                By.XPATH,
                ".//*[@class='_32g5_j']"
            )
            deal['assured'] = 'true'
        except:
            deal['assured'] = 'false'
        try:
            title = element.find_element(
                By.XPATH,
                ".//*[@class='s1Q9rs']"
            ).text.strip()
            deal['title'] = title
        except:
            deal['title'] = None
        try:
            price = element.find_element(
                By.XPATH,
                ".//*[@class='_30jeq3']"
            ).text.strip()
            deal['price'] = price
        except:
            deal['price'] = None
        try:
            mrp = element.find_element(
                By.XPATH,
                ".//*[@class='_3I9_wc']"
            ).text.strip()
            deal['mrp'] = mrp
        except:
            deal['mrp'] = mrp
        try:
            discount = element.find_element(
                By.XPATH,
                ".//*[@class='_3Ay6Sb']"
            ).text.strip()
            deal['discount'] = discount
        except:
            deal['discount'] = None
        try:
            img = element.find_element(
                By.XPATH,
                ".//*[@class='_396cs4 _3exPp9']"
            ).get_attribute('src')
            deal['img'] = img
        except:
            deal['img'] = img
        try:
            item_link = element.find_element(
                By.XPATH,
                ".//*[@class='s1Q9rs']"
            ).get_attribute('href')
            deal['item_link'] = item_link
        except:
            deal['item_link'] = item_link
        try:
            rating = element.find_element(
                By.XPATH,
                ".//*[@class='_3LWZlK']"
            ).text.strip()
            deal['rating'] = rating
        except:
            deal['rating'] = None
        try:
            no_of_rating = element.find_element(
                By.XPATH,
                ".//*[@class='_2_R_DZ']"
            ).text.strip()
            deal['no_of_rating'] = no_of_rating
        except:
            deal['no_of_rating'] = None
        all_deals.append(deal)
        print("------------------------------------------------------------------------------------------------")
    return all_deals

@shared_task(bind=True)
def amazon_primary_deals(self, search):
    url = get_search_url('flipkart', search)
    driver.get(url)
    # soup = BeautifulSoup(driver.page_source, 'lxml').prettify()
    # with open('page_source.html', 'wb') as f:
    #     f.write(soup.encode('utf8'))
    try:
        top_item_link = driver.find_element(
            by=By.XPATH,
            value='//div[@data-component-type="s-search-result"]//div[contains(@class, "product-image")]//a'
        ).get_attribute('href')
        driver.get(top_item_link)
    except:
        return "No deal found"

    deal_data = {}

    deal_data['item_link'] = top_item_link
    deal_data['company'] = None

    title = driver.find_element(
        by=By.XPATH, value="//span[@id='productTitle']"
    ).text.strip()
    deal_data['title'] = title

    try:
        price = '.'.join(driver.find_element(
            by=By.XPATH,
            value="//div[contains(@id, 'corePriceDisplay')]//span[contains(@class, 'priceToPay')]"
        ).text.strip().split('\n'))
    except:
        try:
            formats = driver.find_elements(
                by=By.XPATH, value="//div[@id='tmmSwatches']//li[not(contains(@style, 'display: none'))]//a[contains(@class, 'button-text')]"
            )
            price = {}
            for format in formats:
                price.update({format.find_element(by=By.XPATH, value=".//span[1]").text :
                            format.find_element(by=By.XPATH, value=".//span[2]").text})
        except:
            price = None
    deal_data['price'] = price
    
    try:
        mrp = driver.find_element(
            by=By.XPATH,
            value="//div[contains(@id, 'corePriceDisplay')]//span[@data-a-strike='true']"
        ).text.strip()
    except:
       mrp = None  
    deal_data['mrp'] = mrp

    try:
        discount = driver.find_element(
            by=By.XPATH,
            value="//div[contains(@id, 'corePriceDisplay')]//span[contains(@class, 'savingsPercentage')]"
        ).text.strip()
    except:
        discount = None
    deal_data['discount'] = discount

    try:
        rating = driver.find_element(
            by=By.XPATH,
            value="//div[@id='averageCustomerReviews']//span[@id='acrPopover']"
            ).get_attribute('title')
    except:
        rating = None
    deal_data['rating'] = rating

    try:
        reviews_count = driver.find_element(
            by=By.XPATH,
            value="//div[@id='averageCustomerReviews']//span[@id='acrCustomerReviewText']"
        ).text.strip()
    except:
        reviews_count = None
    deal_data['no_of_ratings'] = reviews_count

    try:
        image = driver.find_element(
            by=By.XPATH, 
            value="//div[@id='main-image-container']//img"
        ).get_attribute('src')
    except:
        image = None
    deal_data['img'] = image

    try:  # See More Offers
        driver.find_element(
            by=By.XPATH,
            value="//div[@id='sopp-primary-ingress']//span[contains(@class, 'a-expander-prompt')]"
        ).click()
    except:
        pass

    offers = {}

    offer_wrappers = driver.find_elements(
        by=By.XPATH, 
        value="//div[@id='sopp-primary-ingress']//span[@aria-hidden='true']"
    )
    for offer_wrapper in offer_wrappers:
        offers.update({offer_wrapper.find_element(by=By.XPATH, value=".//span[@class='sopp-offer-title']").get_attribute(
            'innerText').replace(':','') : offer_wrapper.find_element(by=By.XPATH, value="//span[@class='description']").get_attribute(
            'innerText')})
    if len(offer_wrappers) == 0:
        offers = [re.sub(r'(<a[^<]*>.+</a>)|(<[^>]+>)', '', li.get_attribute('innerHTML')).strip() for li in driver.find_elements(by=By.XPATH, value="//div[@id='quickPromoBucketContent']//li")]
    deal_data['offers'] = offers

    print(deal_data)

    return deal_data

@shared_task(bind=True)
def amazon_other_deals(self, search):
    url = get_search_url('amazon', search)
    driver.get(url)

    result_items_divs = driver.find_elements(by=By.XPATH, value='//div[@data-component-type="s-search-result"]')

    title = []
    company = []
    image = []
    rating = []
    reviews_count = []
    mrp = []
    discount = []
    sp = []
    fresh = []
    prime = []
    item_url = []

    for item_div in result_items_divs:
        try:
            price_div = item_div.find_element(by=By.XPATH, value=".//div[contains(@class,'s-price-instructions-style')]")
        except:
            continue
        try:
            discount.append(price_div.find_element(by=By.XPATH, value=".//span[contains(@class, 's-color-discount') or contains(text(), '%')]").text)
        except:
            discount.append(None)
        try:
            sp.append(price_div.find_element(by=By.XPATH, value='.//span[not(@data-a-strike="true")  and (@data-a-color="price" or @data-a-color="base")]').text) # /span[1]
        except:
            sp.append(None)
        try:
            mrp.append(price_div.find_element(by=By.XPATH, value='.//span[@data-a-strike="true"]').text) # /span[1]
        except:
            mrp.append(None)
        try:
            title.append(item_div.find_element(by=By.XPATH, value='.//h2//span').text)
        except:
            title.append(None)
        try:
            company.append(item_div.find_element(by=By.XPATH, value='.//h5//span').text)
        except:
            company.append(None)
        try:
            image.append(item_div.find_element(by=By.XPATH, value='.//div[contains(@class, "product-image")]//img').get_attribute('src'))
        except:
            image.append(None)
        try:
            item_url.append(item_div.find_element(by=By.XPATH, value='.//div[contains(@class, "product-image")]//a').get_attribute('href'))
        except:
            item_url.append(None)
        try:
            rating.append(item_div.find_element(by=By.XPATH, value=".//span[contains(@aria-label, 'out of') and contains(@aria-label, 'stars')]").get_attribute('aria-label'))
        except:
            rating.append(None)
        try:
            reviews_count.append(item_div.find_element(by=By.XPATH, value=".//span[contains(@aria-label, 'out of') and contains(@aria-label, 'stars')]/following-sibling::span").get_attribute('aria-label'))
        except:
            reviews_count.append(None)
        try:
            item_div.find_element(by=By.XPATH, value='.//i[@aria-label="Amazon Prime"]')
            prime.append(True)
        except:
            prime.append(False)
        try:
            item_div.find_element(by=By.XPATH, value='.//img[@alt="Amazon Fresh"]')
            fresh.append(True)
        except:
            fresh.append(False)

    print(title, company, image, mrp, sp, discount, rating, reviews_count, fresh, prime, item_url, sep='\n')

    data = {
        'Product Title' : title,
        'Product Company' : company,
        'Image Link' : image,
        'MRP' : mrp,
        'Price' : sp,
        'Discount %age' : discount,
        'Rating' : rating,
        'Reviews Count' : reviews_count,
        'Is_fresh' : fresh,
        'Is_prime' : prime,
        'Item URL' : item_url
    }

    print('\n\nConverting to DataFrame and printing it.\n\n')
    df = pd.DataFrame(data)
    return df.to_json()


@shared_task(bind=True)
def snapdeal_primary_deal(self, search):
    url = get_search_url('snapdeal', search)
    driver.get(url)

    top_item_link = driver.find_element(
        by=By.XPATH, 
        value="//section[.//div[contains(@class,'product-tuple-listing')]]//div[contains(@class,'product-tuple-listing')]//a"
        ).get_attribute('href')
    driver.get(top_item_link)

    deal_data = {}

    deal_data['item_link'] = top_item_link
    deal_data['company'] = None

    try:
        title = driver.find_element(by=By.XPATH, value="//h1").text
    except:
        title = None
    deal_data['title'] = title

    try:
        sp = driver.find_element(by=By.XPATH, value="//span[@class='pdp-final-price']").text
    except:
        sp = None
    deal_data['price'] = sp

    try:
        mrp = driver.find_element(
            by=By.XPATH, value="//div[normalize-space(@class)='pdpCutPrice']"
        ).text
        children_text = [child.text for child in driver.find_elements(by=By.XPATH, value="//div[normalize-space(@class)='pdpCutPrice']/*")]
        for child_text in children_text:
            mrp = mrp.replace(child_text, '').strip()
    except:
        mrp = None
    deal_data['mrp'] = mrp

    try:
        discount = driver.find_element(by=By.XPATH, value="//span[normalize-space(@class)='pdpDiscount']").text
    except:
        discount = None
    deal_data['discount'] = discount

    try:
        rating = driver.find_element(by=By.XPATH, value=".//div[normalize-space(@class)='filled-stars']").get_attribute(
                    'style')
        rating = rating[rating.find('width:') + 6:rating.find('%;')].strip()
    except:
        rating = None
    deal_data['rating'] = rating

    try:
        reviews_count = driver.find_element(by=By.XPATH, value="//span[contains(@class, 'total-rating')]").text
    except:
        reviews_count = None
    deal_data['no_of_ratings'] = reviews_count

    try:
        image = driver.find_element(by=By.XPATH, value='//*[@id="bx-slider-left-image-panel"]//img').get_attribute('src')
    except:
        image = None
    deal_data['img'] = image

    offers = []
    offers_containers = driver.find_elements(by=By.XPATH, value="//div[contains(@class, 'pdp-e-i-alloffers')]")
    for offer in offers_containers:
        text = offer.find_element(by=By.XPATH, value="//div[contains(@class, 'genericOfferClass')]").text
        children_text = [child.text for child in driver.find_elements(by=By.XPATH, value="//div[contains(@class, 'genericOfferClass')]/*")]
        for child_text in children_text:
            text = text.replace(child_text, '').strip()
        offers.append(text)
    deal_data['offers'] = offers

    print(deal_data)

    return deal_data


@shared_task(bind=True)
def snapdeal_other_deals(self, search):
    url = get_search_url('snapdeal', search)
    driver.get(url)
    rows = driver.find_elements(by=By.XPATH, value="//section[.//div[contains(@class,'product-tuple-listing')]]")

    title = []
    image = []
    rating = []
    reviews_count = []
    mrp = []
    discount = []
    sp = []
    item_url = []

    for row in rows:
        items = row.find_elements(by=By.XPATH, value=".//div[contains(@class,'product-tuple-listing')]")
        for item in items:

            try:
                item_url.append(item.find_element(by=By.XPATH, value=".//a").get_attribute('href'))
            except:
                continue

            img = item.find_element(by=By.XPATH, value=".//img")
            img_link = img.get_attribute('src')
            if img_link is None:
                img_link = img.get_attribute('data-src')
            image.append(img_link)

            try:
                title.append(item.find_element(by=By.XPATH, value=".//p[normalize-space(@class) ='product-title']").text)
            except:
                title.append(None)

            try:
                mrp.append(
                    item.find_element(by=By.XPATH, value=".//span[contains(@class, 'product-desc-price strike')]").text)
            except:
                mrp.append(None)

            try:
                sp.append(item.find_element(by=By.XPATH, value=".//span[contains(@class, 'product-price')]").text)
            except:
                sp.append(None)

            try:
                discount.append(
                    item.find_element(by=By.XPATH, value=".//div[normalize-space(@class)='product-discount']").text)
            except:
                discount.append(None)

            try:
                reviews_count.append(
                    item.find_element(by=By.XPATH, value=".//p[normalize-space(@class)='product-rating-count']").text)
            except:
                reviews_count.append(None)

            try:
                r = item.find_element(by=By.XPATH, value=".//div[normalize-space(@class)='filled-stars']").get_attribute(
                    'style')
                rating.append(r[r.find('width:') + 6:r.find('%;')].strip())
            except:
                rating.append(None)

    print(title, image, mrp, sp, discount, rating, reviews_count, item_url, sep='\n')

    data = {
        'Product Title': title,
        'Image Link': image,
        'MRP': mrp,
        'Price': sp,
        'Discount %age': discount,
        'Rating': rating,
        'Reviews Count': reviews_count,
        'Item URL': item_url
    }

    print('\n\nConverting to DataFrame and printing it.\n\n')
    df = pd.DataFrame(data)
    return df.to_json()