from typing import List

from config import Config


class MercadoLivre(Config):
    def __init__(self):
        super().__init__()

    def get_categories(self) -> List:
        page = self.get_html('https://www.mercadolivre.com.br/mais-vendidos')
        categories_links = page.find_all("a", {"class": "dynamic__carousel-link"})
        links = [link.get('href') for link in categories_links]
        return links

    def get_products(self):
        all_products = []
        all_categories = self.get_categories()

        for link in all_categories:
            page = self.get_html(link)
            page_title = page.find("h1", {"class": "seller-title"}).get_text()
            title_container = page.find_all("p", {"class": "promotion-item__title"})
            price_container = page.find_all("span", {"class": "promotion-item__price"})

            product_title = [product_title.get_text() for product_title in title_container]
            product_price = [price.contents[0] for price in price_container]
            product_value = [value.get_text() for value in product_price]

            products = []

            for title, value in zip(product_title, product_value):
                products.append({'name': title, 'price': value.split('R$ ')[1]})

            data = {'category': page_title, 'products': products}
            print(data)
            all_products.append(data)

    def build(self):
        self.get_products()
        self.driver.close()
