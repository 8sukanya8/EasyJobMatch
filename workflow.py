import dataset
from datetime import datetime

db          = dataset.connect('sqlite:///data.db')
table_raw   = db['data_raw']
table_clean = db['data_clean']


def main(url):
    '''
    '''
    raw = fetch_pagedata(url)
    table_raw.upsert(raw, ['source'])
    print(f'fetched&saved raw data for {url}')

    clean = parse_data(raw)
    table_clean.insert(clean)
    print(f'parsed&saved clean data for {url}')


def fetch_pagedata(url):
    '''
    '''

    raw = {
        'source': url,
        'page_content': '',
        'fetched_on': datetime.now(),
    }

    return raw


def parse_data(raw_data):
    '''
    '''

    clean = {
        'source': raw_data['source'],
        'title': '',
        'tags': '',
    }

    return clean
