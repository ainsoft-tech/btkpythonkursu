import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://aintech:u9WMegfp6XNQwPst@cluster0.qr7d2.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one()
for i in mycollection.find({},{"_id":0 ,"name": 1}):
    print(i)

# print(result)
