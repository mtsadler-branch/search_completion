from flask import *
from flask_cors import CORS

from helpers import get_results


app = Flask(__name__)
CORS(app)

@app.route("/prefix/<prefix>/")
@app.route('/prefix/<prefix>/<limit>')
def get_words(prefix, limit=None):
    if limit:
        results = get_results(prefix=prefix, limit=limit)
    else:
        results = get_results(prefix=prefix)
    return results

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
