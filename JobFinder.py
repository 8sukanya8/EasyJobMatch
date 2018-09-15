import Spider
import config
import load_data

spidy = Spider.Spider()
spidy.crawl(config.employer_links)

spidy.get_job_description_all()
load_data.save_list_to_file(spidy.url_list, "clean_job_urls.txt")
load_data.save_dict_to_file(config.structured_data, "structured_data.txt")
load_data.save_dict_to_file(config.raw_data, "raw_data.txt")

