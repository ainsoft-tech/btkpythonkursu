import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://aintech:u9WMegfp6XNQwPst@cluster0.qr7d2.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one({"name": "Samsung S5"})
# result = mycollection.find_one({"_id": ObjectId("5d6a54e42afaa1169e4b9a0c")})

# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"]
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gt": 2000 # Belirtilen sayıdan büyük
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gte": 2000 # Belirtilen sayıdan büyük veya eşit, gt:büyük olan
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$eq": 2000 #eşittir
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$lte": 2000 : # verilen sayıdan küçük ve eşit
#     }
# })

# result = mycollection.find({
#     "name": { "$regex": "^S" } # verilen karaktere göre
# })


for i in result:
    print(i)



