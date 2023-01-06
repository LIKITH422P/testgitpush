
import pymongo
client = pymongo.MongoClient("mongodb+srv://Likith422:Likibenki@likith422.mpteby8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "likithtn" ,
     "email": "likithtn@gmail.com" ,
     "surname" : "kumar"
}
db1 = client['mongotest']
collection = db1['test']
collection.insert_one(d )