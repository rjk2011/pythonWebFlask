from flask import Flask, render_template,jsonify
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/a')
def a():
    return jsonify({"about":"something"})

@app.route('/multi/<int:num>',methods=['GET'])
def multi(num):
    return jsonify({'result' : num*10 })



def makeStructure(title, source):
    return jsonify({'source' : source, 
                    'title':title
     })


@app.route('/mongo/read/<id>',methods=['GET'])
def read(id):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["newsai"]
    mycol = mydb["articles"]

    myquery = {"id":id}
    x = mycol.find_one(myquery)
    y = makeStructure(x["title"],x["source"])
    return y


if (__name__ == "__main__"):
    print("Running...")
    app.run(debug=True)
    