import requests # module to make http/https requests 
import html5lib # a small parser package for html-5
from bs4 import BeautifulSoup
import time

while True:
    amazon_url = "https://www.amazon.com/HP-Touchscreen-Computer-Quard-Core-802-11ac/dp/B082PZVZB7/ref=sr_1_1_sspa?keywords=laptop&qid=1579030337&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzS1pXMVRHWlJKNEEwJmVuY3J5cHRlZElkPUEwODExNjU1TVFSVFA4RVNQRFczJmVuY3J5cHRlZEFkSWQ9QTA1MDAxMDAxRkMyWkZMM0lWMzhNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"

    agent_header = {
        "User-Agent" : agent
    }

    amazon_page = requests.get(amazon_url, headers=agent_header)

    #print(type(amazon_page.content))
    soup = BeautifulSoup(amazon_page.content, "html5lib")
    #print(soup.prettify())

    # search for a specific ID in the soup
    price_span = str(soup.find(id="priceblock_ourprice"))
    #print(price_span)

    price = ''
    for char in price_span:
        if char.isdigit() is True:
            price += char
        if char == ".":
            price += char

    #print(price)
    price = float(price)

    max_price = 500
    if price <= max_price:
        print("Yo you can buy it now")
    else:
        print("You can afford it, make more money.")

    time.sleep(86400)


