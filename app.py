from flask import Flask, render_template,jsonify
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


if (__name__ == "__main__"):
    print("Running...")
    app.run(debug=True)
    