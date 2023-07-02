from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from config import MONGODB_URI

app = Flask(__name__)


client = MongoClient(MONGODB_URI)
db = client.testfile

@app.route('/data', methods=['GET'])
def get_data():
    collection = db.file1
    data = collection.find()
    data_list = [doc for doc in data]
    for doc in data_list:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return jsonify(data_list)

@app.route('/data_e', methods=['POST'])
def insert_data():
    collection = db.file1
    data = {
        'name': request.form.get('name'),
        'age': request.form.get('age')
    }
    inserted_data = collection.insert_one(data)
    return jsonify(str(inserted_data.inserted_id))

@app.route('/insert', methods=['GET'])
def show_form():
    return render_template('data_form.html')

if __name__ == '__main__':
    app.run(debug=True)

