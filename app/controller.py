import flask

from flask import Flask, request, render_template, Response, redirect
from data import ContentManager
from myutils import get_logger, get_limiter

app = Flask(__name__)
cm = ContentManager(app)
logger = get_logger(app)
limiter = get_limiter(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

@app.route('/content')
def get_content():
    contentKey = request.args.get('contentKey', default='Default')
    logger.info('content loaded')
    return Response(cm.get_content(contentKey), status=200)

@app.route('/content', methods=['PUT'])
@limiter.limit("3 per second")
def put_content():
    contentKey = request.form['contentKey']
    contentValue = request.form['contentValue']

    # internal check. Currently with a mock to randomly throw an exception
    _internal_check(contentKey)

    cm.set_content(contentKey, contentValue)
    logger.info('rquest to load content')
    return Response(status=200)

def _internal_check(contentKey):
    if contentKey == "test_key":
        return
    import random
    random.randint(1, 10) == 1
    raise Exception("Cannot pass internal check")

if __name__ == '__main__':
    import os
    port = os.environ.get("PORT", "8080")
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)
