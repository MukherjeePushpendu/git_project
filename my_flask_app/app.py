from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']
    client = MongoClient('mongodb://localhost:27017/')
    db = client['todo_db']
    collection = db['items']
    collection.insert_one({'itemName': itemName, 'itemDescription': itemDescription})
    return "Item added!"

if __name__ == '__main__':
    app.run(debug=True)
