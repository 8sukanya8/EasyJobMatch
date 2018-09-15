import re
import config

def generate_url_from_company_name(company_name):
    candidate_url_list = []
    # Rule 1
    name_combinations = get_name_combinations(company_name)
    for prefix in config.prefix_list:
        for suffix in config.suffix_list:
            for name in name_combinations:
                candidate_url = prefix+name+suffix
                print(candidate_url)
                candidate_url_list.append(candidate_url)
    return candidate_url_list

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