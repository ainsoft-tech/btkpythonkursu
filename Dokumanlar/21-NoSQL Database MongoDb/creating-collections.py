import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://aintech:u9WMegfp6XNQwPst@cluster0.qr7d2.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# product = {"name":"Samsung S5", "price": 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)


productList = [
    {"name":"Samsung S6", "price": 3000, "description":"iyi telefon"},
    {"name":"Samsung S7", "price": 4000, "categories": ['telefon','elektronik']},
    {"name":"Xiaomi Note 12S", "price": 11000, "categories": ['telefon','elektronik']}
]

result = mycollection.insert_many(productList)
print(result.inserted_id)
