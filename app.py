from flask import Flask, request
import pymongo

import mongo_operator

app = Flask(__name__)


db = "dev-partner"


@app.route('/api/search', methods=['GET'])
def get_student_by_body():
    data = request.get_json()  # Get data from request body
    # search_text = data.get("searchText")
    # if search_text:
    #     print(search_text)
    client = mongo_operator.mongo_client()
    collection = client[db]["env_question"]
    results = collection.find()
    for doc in results:
        print(doc)
    return {"name":"hello"}


if __name__ == '__main__':
    app.run(debug=True)
