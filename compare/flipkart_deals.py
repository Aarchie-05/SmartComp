def flipkart_all_deals(driver, search_item):
    item = search_item.replace(" ", "+")
    BASE_SEARCH_URL = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=relevance"
    url = BASE_SEARCH_URL.format(item)

    driver.get(url)