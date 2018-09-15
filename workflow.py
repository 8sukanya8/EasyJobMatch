import dataset, config
from datetime import datetime

def connect_to_database(dbname = 'sqlite:///data.db'):
    db = dataset.connect('sqlite:///data.db')
    return db

def create_table_raw(db):
    table_raw = db['data_raw']
    return table_raw

def create_table_clean(db):
    table_clean = db['data_clean']
    return table_clean


def update_table_clean(table_clean, tag = 'url'):
    for key in config.structured_data.keys():
        table_clean.upsert(config.structured_data[key], [tag])

def read_table_db(db, table_name = 'table_clean'):
    return db[table_name] # url, title, date, description


#for entry in db['data_clean']:
#    print(entry)


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
