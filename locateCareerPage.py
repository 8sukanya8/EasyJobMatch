import Spider
import config
import urlGenerator
import load_data
import workflow
import urlGenerator
import io
import re
import validators


def locate(url):
    soup = Spider.create_soup(url)
    if soup is not None:
        href_list = []
        tags = soup.find_all('a')
        for tag in tags:
            link = tag.get('href')
            if link is not None:
                if validators.url(link):
                    href_list.append(link)
        for keyword in config.career_keywords:
            for link in href_list:
            #print('Searching ', keyword , ' in ', link)
                if re.search(keyword, link):
                #if urlGenerator.verify_host(link)[link] == 0:
                    return link
                #else:
                #    url = re.compile(r"https?://(www\.)?")
                #    url = url.sub('', link).strip().strip('/')
                #    if urlGenerator.verify_host(url)[url] == 0:
                #        return url
    return None

