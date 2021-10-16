import sys
from flask import url_for
from script import app, freezer, pages

@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('article', path=page.path)

if __name__ == '__main__': 
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='127.0.0.1', port=8080, debug=True)