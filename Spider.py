from processing import noise_removal
from bs4 import BeautifulSoup
from urllib.request import urlopen, HTTPError, URLError
import requests
import config
import re
import validators
# from Spider import create_soup, find_urls_in_str, find_tag_subtag, get_url_response

def get_url_response(url):
    """
    This function gets response from a url
    :param url:
    :return:
    """
    try:
        if validators.url(url):
            r = requests.get(url)
            if r.status_code == 200:
                return r
    except HTTPError as err:
        raise HTTPError("HTTP error with status", err.code)
    except TypeError as err2:
        raise TypeError("Type of arg ", url, " is ",type(url))
        return None

def create_soup(url, parser = 'lxml'):
    """
    This function uses the library Beautiful soup to create and return a Soup from a url.
    In case the url is not valid, nothing is returned.
    :param url: the url from which soup is desired
    :param parser: type of parser (lxml/html.parser)
    :return:
    """
    response = get_url_response(url)
    if(response is not None):
        soup = BeautifulSoup(response.text.encode('utf8'), features= parser) #html.parser
        return soup


def find_urls_in_str(s, context_path = None):
    """
    This function helps to find urls present in a string s. In the case when a fragment of a url is present,
    context_path is to be supplied. A context_path when prepended to s is expected to yield a valid url.
    :param s:
    :param context_path:
    :return:
    """
    url_list =[]
    try:
        if s is not None:
            url = re.search('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})', s) # not perfect, needs testing
            if url is not None :
                urls = url.groups()
                for entry in urls:
                    new_url = re.sub('\'|\"|,', '', entry)
                    if new_url is not None and new_url not in url_list and validators.url(new_url):
                        url_list.append(new_url)
            else:
                if(context_path is not None):
                    new_url = context_path+s
                    if new_url is not None and new_url not in url_list and validators.url(new_url):
                        url_list.append(new_url)

        return url_list
    except TypeError as err:
        raise TypeError("Type of arg ", s, " is ",type(s))

def find_tag_subtag(soup,tag, subtag, context_path= None):
    """
    This functions returns links in a soup according to a given tag and subtag.
    :param soup:
    :param tag:
    :param subtag:
    :return:
    """
    url_list = []
    if(soup is not None):
        for tag in soup.find_all(tag):
            link = tag.get(subtag)
            urls = find_urls_in_str(link, context_path)
            for url in urls:
                if (url is not None and url not in url_list):
                    url_list.append(url)
    return(url_list)



class Spider(object):

    def __init__(self):
        self.url_list = []

    def crawl(self, url_tuple_list):
        """
        This function searches the spider object's url_list and yields valid urls.
        The new urls are then appended to the object's url_list for further processing
        :return:
        """

        for tuple in url_tuple_list:
            url = tuple[1]
            context_path = tuple[2]
            soup = create_soup(url)
            for entry in config.links_tags_subtags:
                tag = entry[0]
                subtag = entry[1]
                url_list = find_tag_subtag(soup, tag, subtag, context_path)
                if url_list.__len__() >0:
                    self.url_list = self.url_list + url_list
            self.url_list = [item for item in self.url_list if item not in [url]] # removing url when processed

    def get_job_description(self, url):
        soup = create_soup(url)
        if soup is not None:
            job_tuple = ()
            title = soup.title
            if title is not None:
                title = soup.title.text
            date_of_posting_SRE = re.search('[0-9]{2,4}/[0-9]{2,4}/[0-9]{2,4}|[0-9]{2,4}-[0-9]{2,4}-[0-9]{2,4}|[0-9]{2,4}\.[0-9]{2,4}\.[0-9]{2,4}',
            soup.text)
            date_of_posting = ""
            if(date_of_posting_SRE is not None):
                date_of_posting = date_of_posting_SRE.group()
            for func_key in config.job_description_functions.keys():
                accessor = config.job_description_functions[func_key]
                description = accessor(soup)
                descr_is_useless = description is None or description.length == 0
                if not descr_is_useless:
                    #if(job_tuple.__len__() > 0):
                    #    if job_tuple[4].contents() < description.attrs['content'].__len__():
                    job_tuple = (url,soup.text, title, date_of_posting, description) # if job tuple exists, select one with the largest description length
                    #else:
                    #    job_tuple = (url, soup.text, title, date_of_posting, description) # if job_tuple does not exist, create one
                    return job_tuple
        return None

    def get_job_description_all(self):
        for url in self.url_list:
            print(url)
            job = self.get_job_description(url)
            if job is not None:
                url= job[0]
                raw_text = job[1]
                title = job[2]
                date = job[3]
                description = job[4]
                if description is not None :
                    if description.attrs['content']!= "":
                        config.raw_data[url] = raw_text
                        print(url, " : ", config.raw_data[url])
                        config.structured_data[url] = (url, title, date, description.attrs['content'])
                        print(url, " : ", config.structured_data[url])
                    else:
                        self.url_list.remove(url)
            else:
                self.url_list.remove(url)

            #soup.find_all('TAG', string = re.compile("whatever"))





'''r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

for link in soup.find_all('iframe'):
    print(link.get('src'))

url2 = "https://sbb2.prospective.ch/?sprCd=de" 


url_list = []
for tag in soup.find_all('a'):
    link = tag.get('onclick')
    if(link is not None):
        url = re.search('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})',link).group()
        url = re.sub('\'|\"|,','',url)
        if(url not in url_list):
            url_list.append(url)
print(url_list) 

s = "window.open(\'http://direktlink.prospective.ch?view=611a7e8c-26cf-466e-affb-f625e1b32774\', \'_blank\', \'width=668,height=710,location=yes,scrollbars=yes,left=100,top=200,resizable=yes\')"
'''