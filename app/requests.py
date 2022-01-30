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


# # Getting the sources

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = 'https://newsapi.org/v2/sources?apiKey=2139fab7afd24744980d5c0ed96ad40a'

  
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
            print(source_results_list)

    return source_results

    #processing the source results
def process_results(source_list):
    '''
    Function  that processes the source results and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name= source_item.get('name')
        description= source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        
        
        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

    return  source_results