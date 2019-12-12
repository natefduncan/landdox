import requests
import json
import pandas as pd
import os

from .endpoints import * 

class Client:
    endpoints = {
        "contacts" : contacts,
        "leases" : leases,
        "units" : units, 
        "wells" : wells,
        "custom" : custom, 
        "tracts" : tracts,
        "payments" : payments
    }

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorize()

    def __getattr__(self, name):
        endpoint = self.endpoints.get(name)
        endpoint.access_token = self.access_token
        return endpoint

    def authorize(self):
        payload = {
            "client_id" : self.client_id, 
            "client_secret" : self.client_secret,
            "audience" : "api.landdox.com",
            "grant_type" : "client_credentials"
        }
        url = "https://landdox.auth0.com/oauth/token"
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            raise ValueError("{error}".format(error=response))
        else:
            response = response.json()
            self.access_token = response.get("access_token")
            self.expires_in = response.get("expires_in")
            self.expires_in = response.get("token_type")


        

