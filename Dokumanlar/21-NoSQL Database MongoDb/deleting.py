import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://aintech:u9WMegfp6XNQwPst@cluster0.qr7d2.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({"name":"IPhone 8"})
# mycollection.delete_many({"name": {"$regex":"^S"}})
result = mycollection.delete_many({})

print(f'{result.deleted_count} adet kayıt silindi.')

for i in mycollection.find():
    print(i)