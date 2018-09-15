'''
tags_subtags store the paired Tags and subtags for extraction of links by the spider class
'''
links_tags_subtags = [('a','href'),
                ('iframe', 'src'),
                ('a', 'onclick'),
                ('input', 'value')]
'''
employer_links stores the names of the employers, the urls to their respective career pages and a third optional value - context path
A context path is specified for some employers when the links in their career pages pointing to jobs are partial urls. 
'''
employer_links = [('SwissRe', 'https://careers.swissre.com/search/?q=&q2=&locationsearch=&title=&location=CH&date=', 'https://careers.swissre.com'),
                  ('IBM', 'https://careers.ibm.com/ListJobs/All/Search/Country/CH//?lang=en', 'https://careers.ibm.com'),
                  ('Randstad', 'https://www.randstad.ch/en/jobs/s-it/', 'https://www.randstad.ch/en/jobs/s-it'),
                  ('SBB', 'https://sbb2.prospective.ch/?sprCd=de', None),
                  ('Swisscom', 'https://swisscom-professionals.prospective.ch', None)]

jobs_desciption_tags = [(id, 'aufgaben-knowhow',), (property, 'og:description')]

#urlList = ['https://careers.swissre.com/search/?q=&q2=&locationsearch=&title=&location=CH&date=',
#            'https://sbb2.prospective.ch/?sprCd=de',
#           'https://swisscom-professionals.prospective.ch']
            #'https://careers.swissre.com/search/?q=&q2=&locationsearch=&title=&location=CH&date='
           #'https://www.randstad.ch/en/jobs/s-it/']
           #'https://www.swisscom.ch/en/about/jobs/vacancies.html',
           #'https://company.sbb.ch/de/jobs-karriere/offene-stellen/job-suche.html']
           #'https://jobs.ubs.com/TGnewUI/Search/Home/HomeWithPreLoad?partnerid=25008&siteid=5012&PageType=searchResults&SearchType=linkquery&LinkID=3109'
           #
