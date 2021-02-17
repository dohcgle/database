from tinydb import TinyDB

def insert_db(data_csv):
    return 0


db = TinyDB('smartphone/db.json')

products = open('smartphone/products.csv').read().split('\n')
# print(products)

db.truncate()
products_db = []

for row in products[1:]:
    cat, company=row.split(',')[1:]
    products_db.append({'category': cat, 'company': company})

db.insert_multiple(products_db)