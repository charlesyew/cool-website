import logging
import os

from flask import Flask, render_template_string, Markup
from flask_sqlalchemy import SQLAlchemy
# from flask_blogging import SQLAStorage, BloggingEngine
from flask_flatpages import FlatPages, pygmented_markdown
from flask_frozen import Freezer

import requests

app = Flask(__name__)

# Database
app.config['SECRET_KEY'] = '75eefb333b680448f15a0de4cd5af7a5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Blog Pages
def my_renderer(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

# FLATPAGES_AUTO_RELOAD = DEBUG
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_HTML_RENDERER'] = my_renderer
pages = FlatPages(app)

# Blog Pages Static
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']
freezer = Freezer(app)

#Set environment variable 
os.environ['GA_TRACKING_ID'] = 'UA-207145136-1'

# Environment variables are defined in app.yaml.
GA_TRACKING_ID = os.getenv('GA_TRACKING_ID')


def track_event(category, action, label=None, value=0):
    data = {
        'v': '1',  # API Version.
        'tid': GA_TRACKING_ID,  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        'cid': '555',
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
        'ua': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
    }

    response = requests.post(
        'https://www.google-analytics.com/collect', data=data)

    # If the request fails, this will raise a RequestException. Depending
    # on your application's needs, this may be a non-error and can be caught
    # by the caller.
    response.raise_for_status()


# @app.route('/')
# def track_example():
#     track_event(
#         category='Example',
#         action='test action')
#     return 'Event tracked.'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

from script import routes