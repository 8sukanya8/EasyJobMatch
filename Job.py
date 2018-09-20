import datetime
from enum import Enum

class Job():
    def __init__(self, id, url, date_of_creation = datetime.datetime.now(), status = Job_Status.Available):
        if(id is not None and url is not None):
            self.id = id
            self.url = url
            self.date_of_creation = date_of_creation
            self.status = status
        else:
            print("id and url fields should not be None type.\n id = ", id, ", url = ", url)


class Job_Status(Enum):
    Available = 1
    Unavailable = 2
    Unknown = 3