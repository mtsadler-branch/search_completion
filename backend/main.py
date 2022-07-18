from flask import *
from flask_cors import CORS

from helpers import get_results


app = Flask(__name__)
CORS(app)

@app.route("/prefix/<prefix>")
def get_words(prefix):
    results = get_results(prefix=prefix)
    return results

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=7000)