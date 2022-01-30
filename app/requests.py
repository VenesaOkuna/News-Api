import urllib.request
import json
from .models import Source, Article

# getting api key
api_key = ''

# getting news base url for the sources
base_url_source = None

# getting news articles base url from the source id
base_url_articles = None


def configure_request(app):
    global api_key, base_url_source, base_url_articles
    base_url_source = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']