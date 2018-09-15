import Spider
import config
import load_data
import workflow
import urlGenerator
import io

spidy = Spider.Spider()
spidy.crawl(config.employer_links)
spidy.get_job_description_all()

db = workflow.connect_to_database('sqlite:///data.db')
table_clean = workflow.create_table_clean(db)
table_raw= workflow.create_table_raw(db)

#workflow.update_table_clean(table_clean)

load_data.save_list_to_file(spidy.url_list, "clean_job_urls.txt")

db_company = workflow.connect_to_database('sqlite:///data_company_name.db')
table_companies = db_company['companies']
company_names = workflow.get_column_from_table(table_companies, 'name', True)

data = []
f = open('site_blacklist.csv','r')
data=f.read()
f.close()

blacklist_company_names = []
blacklist_company_url = []
with io.open("site_blacklist.csv", "r", encoding="utf-8") as file:
     blacklist = file.read().split("\n")

for entry in blacklist:
    split_entry = entry.split(",")
    blacklist_company_url.append(split_entry[0])
    blacklist_company_names.append(split_entry[1])


for entry in table_companies:
    new_entry = entry
    name = entry['name']
    id = entry['id']
    status = entry['status']
    if status == 'aktiv':
        valid_url = urlGenerator.select_valid_url(urlGenerator.generate_url_from_company_name(name))
        if valid_url is not None and not (blacklist_company_url.__contains__(valid_url) or blacklist_company_names.__contains__(name)):
            new_entry['url'] = valid_url
            config.company_names_url_dict[id] = new_entry
            print(id, ", ",name, ",", valid_url)

company_url_table = db_company['company_url']
workflow.update_table(company_url_table, config.company_names_url_dict, ['id'])


company_url_expanded = db_company['company_url_expanded']

for entry in company_url_expanded:
    id = entry['id']
    url = entry['url']
    career_page = locateCareerPage.locate(locate_career_page)
#load_data.save_dict_to_file(config.structured_data, "structured_data.txt")
#load_data.save_dict_to_file(config.raw_data, "raw_data.txt")

