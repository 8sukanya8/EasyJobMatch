
class Company():
    def __init__(self, id, name, uid, url_id, status, url = "", careers_page = ""):
        if(id is not None and name is not None):
            self.id = id
            self.name = name
            self.uid = uid
            self.url_id = url_id
            self.status = status
            self.url = url
            self.careers_page = careers_page
        else:
            print("id and name fields should not be None type.\n id = ", id, ", name = ", name)

