import argparse
from flask import *
from flask_cors import CORS

from helpers import get_results, get_word_details


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


@app.route("/details/<word>")
def get_details(word):
    return jsonify(get_word_details(word=word, api_key=api_key))


if __name__ == '__main__':
    # Argument Parser
    parser = argparse.ArgumentParser(
        description="Params for passing API key and other params."
    )
    parser.add_argument(
        "--api_key",
        dest="api_key",
        help="API Key for dicionaryapi.com",
    )

    # Parse Arguments
    args = parser.parse_args()
    api_key = args.api_key
    app.debug = False
    app.run(host='0.0.0.0', port=5001)
