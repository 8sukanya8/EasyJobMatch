import re
from urllib3.exceptions import NewConnectionError
from urllib.request import HTTPError
import config
import validators, requests
import os
import subprocess

def generate_url_from_company_name(company_name):
    candidate_url = []
    name_combinations = get_name_combinations(company_name)
    for prefix in config.prefix_list:
        for suffix in config.suffix_list:
            for name in name_combinations:
                candidate_url.append(prefix + name + suffix)
    return candidate_url


def select_valid_url(url_list):
    for url in url_list:
        if validators.url(url):
            #print(url)
            if verify_host(url)[url] == 0:
                return url
    return None


def get_name_combinations(company_name):
    name_combination = []
    company_name = umlaut_replacement(company_name)
    company_name = company_name.lower()
    list_of_str = re.split(';|,| |\*|\n', company_name)
    # rule 1: only firstname or lastname (or heck even middle name!)
    for str1 in list_of_str:
        name_combination.append(str1)
        for str2 in list_of_str:
            if(str1 != str2):
                name_combination.append(str1 + str2) # rule 2 firstnamelastname
                name_combination.append(str1 + "-" + str2)  # rule 3 firstname-lastname
    return name_combination

def umlaut_replacement(string):
    umlauts = {'ä': 'ae',
               'ö': 'oe',
               'Ä': 'Ae',
               'Ö': 'Oe',
               'ü': 'ue',
               'Ü': 'Ue'}
    for key in umlauts.keys():
        string = re.sub(key, umlauts[key], string)
    return string



def ping_return_code(hostname):
    """Use the ping utility to attempt to reach the host. We send 5 packets
    ('-c 5') and wait 3 milliseconds ('-W 3') for a response. The function
    returns the return code from the ping utility.
    """
    ret_code = subprocess.call(['ping', '-c', '5', '-W', '3', hostname],
                               stdout=open(os.devnull, 'w'),
                               stderr=open(os.devnull, 'w'))
    return ret_code

def verify_host(hostname):
    """For each hostname in the list, attempt to reach it using ping. Returns a
    dict in which the keys are the hostnames, and the values are the return
    codes from ping. Assumes that the hostnames are valid.
    """
    return_codes = dict()
    return_codes[hostname] = ping_return_code(hostname)
    return return_codes
