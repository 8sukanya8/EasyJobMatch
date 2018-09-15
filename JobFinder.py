import Spider
import config
import load_data
import workflow

spidy = Spider.Spider()
spidy.crawl(config.employer_links)
spidy.get_job_description_all()

db = workflow.connect_to_database()
table_clean = workflow.create_table_clean(db)
table_raw= workflow.create_table_raw(db)

#workflow.update_table_clean(table_clean)

load_data.save_list_to_file(spidy.url_list, "clean_job_urls.txt")
#load_data.save_dict_to_file(config.structured_data, "structured_data.txt")
#load_data.save_dict_to_file(config.raw_data, "raw_data.txt")

