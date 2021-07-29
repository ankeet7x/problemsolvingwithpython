import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thehipstore.co.uk/mens/footwear/shoes/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

productList = soup.find_all(class_="productListItem")

# imageLinks = [ productList.find(class_="").get_text() for product in productList]

scraped_product_name = [product.find(class_="itemTitle").get_text() for product in productList]
scraped_product_description = [product.find(class_="product-description").get_text() for product in productList]
scraped_product_price = [product.find(class_="itemPrice").get_text() for product in productList]

formatted_product_name = [product.replace("\n", "") for product in scraped_product_name]
formatted_product_description = scraped_product_description
formatted_product_price = [product.replace("\n", "") for product in scraped_product_price]

product_data = pd.DataFrame({
	'Product Name': formatted_product_name,
	'Product price': formatted_product_price,
	'Product description': formatted_product_description
	})

product_data.to_csv('products.csv', header=True, index=False, encoding='utf-8')