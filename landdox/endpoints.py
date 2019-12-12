    
import requests

class Endpoint:
    version = "v2"
    base = "https://api.landdox.com"

    def __init__(self, name, access_token):
        self.name = name
        self.access_token = access_token

    def handle_error(self, response):
        if response.status_code != 200:
            raise ValueError("{error}".format(error=str(response)))
        else:
            return response.json()

    def put(self, id, data):
        url = "/".join([self.base, self.version, self.name, str(id)])
        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.put(url, data={"data" : data}, headers=header)
        safe_response = self.handle_error(response)
        return safe_response
    
    def get(self, id):
        url = "/".join([self.base, self.version, self.name, str(id)])
        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.get(url, headers=header)
        safe_response = self.handle_error(response)
        return safe_response

    def delete(self, id):
        url = "/".join([self.base, self.version, self.name, str(id)])
        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.delete(url, headers=header)
        safe_response = self.handle_error(response)
        return safe_response

    def create(self, data):
        url = "/".join([self.base, self.version, self.name])
        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.post(url, data = {"data" : data}, headers=header)
        safe_response = self.handle_error(response)
        return safe_response

    def list(self, page_size=10, page_number=1):
        url = "/".join([self.base, self.version, self.name])
        url += "?page[size]={page_size}&page[number]={page_number}".format(page_size=page_size, page_number=page_number)
        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.get(url, headers=header)
        safe_response = self.handle_error(response)
        return safe_response

#https://api.landdox.com/documentation#tag/Contacts
class contacts(Endpoint):
    access_token = None
    def __init__(self):
        super().__init__(type(self).__name__, self.access_token)

#https://api.landdox.com/documentation#tag/Leases
class leases(Endpoint):
    access_token = None
    def __init__(self):
        super().__init__(type(self).__name__, self.access_token)

#https://api.landdox.com/documentation#tag/Units
class units(Endpoint):
    access_token = None
    def __init__(self):
        super().__init__(type(self).__name__, self.access_token)

#https://api.landdox.com/documentation#tag/Wells
class wells(Endpoint):
    access_token = None
    def __init__(self):
        super().__init__(type(self).__name__, self.access_token)

#https://api.landdox.com/documentation#tag/Custom-Forms
class custom(Endpoint):
    access_token = None
    def __init__(self, name=None):
        super().__init__(name, self.access_token)

#https://api.landdox.com/documentation#tag/Payments
class payments(Endpoint):
    access_token = None
    def __init__(self, payment_type=None):
        if payment_type:
            name = type(self).__name__ + "/" + payment_type
        else:
            raise ValueError("Payment endpoint requireds payment_type parameter of eithe revenue or expense")
        super().__init__(name, self.access_token)

#https://api.landdox.com/documentation#tag/Tracts
class tracts(Endpoint):
    access_token = None
    def __init__(self):
        super().__init__(type(self).__name__, self.access_token)

    def get(self, id, tract_type=None):
        url = "/".join([self.base, self.version, self.name, id])

        if tract_type:
            if tract_type in ["location", "acreage"]:
                url += "/" + tract_type
            else:
                raise ValueError("Tract_type must be either location or acreage.")

        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.get(url, headers=header)
        safe_response = self.handle_error(response)
        return safe_response

    def list(self, page_size=10, page_number=1, id=None, list_type=None):
        url = "/".join([self.base, self.version, self.name])

        if list_type:
            if id == None:
                ValueError("Id cannot be None for this endpoint.")

            if list_type not in ["ownerships", "interests"]:
                raise ValueError("List type must be either ownerships or interests.")

            else:
                url += "/".join([str(id), str(list_type)])

        header = {"authorization" : "Bearer " + self.access_token}
        response = requests.get(url, headers=header)
        safe_response = self.handle_error(response)
        return safe_response


    