import pymongo
client = pymongo.MongoClient("mongodb+srv://mumtaz:mohammadi@cluster0.esas7nu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d = {"name":"mumtaz",
            "email":"mumtaz@gmail.com",
            "surname":"mohammadi"    }

db1  = client['mongotest']
coll = db1['test']
coll.insert_one(d)