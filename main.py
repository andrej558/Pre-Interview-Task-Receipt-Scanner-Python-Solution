import requests
import json
from types import SimpleNamespace


class Product:

    def __init__(self, name, domestic, price, weight=None, description=None):
        self.name = name
        self.domestic = domestic
        self.price = price
        self.weight = weight
        self.description = description

    @classmethod
    def from_json(cls, json_string):


        return cls(**json_string)

intent = "   "

def print_product(product):
    print('...', end="")
    print(product.name)
    print(intent + 'Price: $' + str(prod.price))
    print(intent + product.description)
    print(intent + 'Weight: ', end="")
    print(str(product.weight) + 'g' if product.weight else 'N/A')


if __name__ == '__main__':

    products = []
    prod_domestic = []
    prod_imported = []

    response = requests.get("https://interview-task-api.mca.dev/qr-scanner-codes/alpha-qr-gFpwhsQ8fkY1")

    for t in response.json():
        prod = Product.from_json(t)


        if(prod.domestic):
            prod_domestic.append(prod)
        else:
            prod_imported.append(prod)


    prod_domestic.sort(key=lambda x: x.name)
    prod_imported.sort(key=lambda x: x.name)



    print('.Domestic')
    for product in prod_domestic:
        print_product(product)
    print('.Imported')

    for product in prod_imported:
        print_product(product)