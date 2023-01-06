
import pymongo
client = pymongo.MongoClient("mongodb+srv://Likith422:Likibenki@likith422.mpteby8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database  = client['myinfo']
collection = database['liki']


#data = collection.find({"companyName" : "sriGuru"})
data = collection.find({"courseOffered" : {"$gt" : "E"}})
for i in data :
    print(i)
