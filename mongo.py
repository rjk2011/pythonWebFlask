import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsai"]
mycol = mydb["articles"]
x = mycol.find_one()

# print(x)


myquery = {"id":"1accf727-82a0-4412-ba05-a2139bec4705"}

mydoc = mycol.find(myquery)
print(mydoc.count())
for x in mydoc:
  print(x)