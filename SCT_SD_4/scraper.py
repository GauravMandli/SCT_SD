import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    products = []

    for product in soup.select('.product_pod'):
        name = product.h3.a['title']
        price = product.select_one('.price_color').text
        rating = product.p['class'][1]

        products.append([name,price,rating])
    
    return products