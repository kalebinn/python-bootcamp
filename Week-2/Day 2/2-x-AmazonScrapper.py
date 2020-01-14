import requests
import html5lib
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/Canon-T7-18-55mm-3-5-5-6-Accessory/dp/B07P15K8Q7/ref=sr_1_4?keywords=dslr&qid=1577826246&sr=8-4"

agent_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

amazon_page = requests.get(amazon_url, headers=agent_header)

soup = BeautifulSoup(amazon_page.content, "html5lib")
#print(soup.prettify())
price = soup.find(id="priceblock_ourprice")
price = str(price)
print(price)

price_nums = ''
for char in price:
    if char.isdigit():
        price_nums += char
    if char == ".":
        price_nums += char

print(price_nums)
print(float(price_nums))
price_dollars = float(price_nums)
if (price_dollars < 500):
    print(f"the camera is now less than {price_dollars}")
