import sqlalchemy
import records
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import urlGenerator
import config

Base = declarative_base()
engine = create_engine('sqlite:///%s' % config.db_folder_path + "CompanyNames.db", echo=True)

def loadSession():
    """

    :param dbPath:
    :return:
    """
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class db_Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uid = Column(String)
    url_id = Column(String)
    status = Column(String)
    url = Column(String)
    careers_page = Column(String)

    def __init__(self, id, name, uid, url_id, status, url = "", careers_page = ""):
        if (id is not None and name is not None):
            self.id = id
            self.name = name
            self.uid = uid
            self.url_id = url_id
            self.status = status
            self.url = url
            self.careers_page = careers_page
        else:
            print("id and name fields should not be None type.\n id = ", id, ", name = ", name)

    def __repr__(self):
        return "<company(id ='%s', name ='%s', uid = '%s', url_id ='%s', status = '%s')>" % (
        self.id, self.name, self.uid, self.url_id, self.status)
        # url = '%s', careers_page = '%s' self.url, self.careers_page
session = loadSession()

def update_url(session):
    for instance in session.query(db_Company).order_by(db_Company.id):
        if(instance.name is not None and instance.name is not "" and instance.url is None):
            valid_url = urlGenerator.select_valid_url(urlGenerator.generate_url_from_company_name(instance.name))
            #if valid_url is not None and not (
            #        config.blacklist.keys().__contains__(valid_url) or
            #        instance.name in config.blacklist.values()):
            #    instance.url = valid_url
            #    session.commit()
            print(instance.id, instance.name, instance.url, valid_url)


