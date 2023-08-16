from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def get_student_by_body():
    print("aaa")
    data = request.get_json()  # Get data from request body
    search_text = data.get("searchText")
    if search_text:
        print(search_text)


if __name__ == '__main__':
    app.run(debug=True)
