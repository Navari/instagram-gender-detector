from flask import Flask, jsonify
from detector import main

app = Flask(__name__, static_url_path='/static')


@app.route('/<username>')
def hello_world(username):
    response = main.run(username)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
