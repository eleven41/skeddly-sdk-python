import requests

from . import actions
from . import credentials
from . import configloader

from ..models import exceptions

class Client(
    actions.ActionsMixin,
    credentials.CredentialsMixin,
    ):

    def __init__(self, accessKey = None):
        self.endpoint = "https://api.skeddly.com/api/"

        if (accessKey is None):
            d = configloader.load_config()
            if ("accessKey" not in d):
                raise exceptions.SkeddlyException("Cannot read access key from config")
            accessKey = d["accessKey"]

        self.accessKey = accessKey
        self.is_log = False

    def throw_exception(self, response):
        message = None

        errorObj = response.json()
        if ("message" in errorObj):
            message = errorObj["message"]
        
        if ("errorCode" in errorObj):
            errorCode = errorObj["errorCode"]

            if (errorCode == "ParameterValidationFailed" and "modelState" in errorObj):
                modelState = errorObj["modelState"]
                raise exceptions.ParameterValidationFailedException(message, errorCode, modelState)

            raise exceptions.SkeddlyWebException(message, errorCode)

        raise exceptions.SkeddlyException(message)

    def get_headers(self):
        headers = {
            "Authorization": "AccessKey " + self.accessKey
        }
        return headers

    def get_endpoint(self, action):
        return self.endpoint + action

    def invoke_get(self, action):
        if (self.is_log):
            print("Invoking GET " + action)

        url = self.get_endpoint(action)
        headers = self.get_headers()

        response = requests.get(url, headers = headers)
        if (response.status_code == 200):
            return response.json()
        
        self.throw_exception(response)

    def invoke_post(self, action, body):
        if (self.is_log):
            print("Invoking POST " + action)

        url = self.get_endpoint(action)
        headers = self.get_headers()

        response = requests.post(url, json=body, headers = headers)
        if (response.status_code == 200):
            return response.json()
        
        self.throw_exception(response)

    def invoke_put(self, action, body = None):
        if (self.is_log):
            print("Invoking PUT " + action)

        url = self.get_endpoint(action)
        headers = self.get_headers()

        response = requests.put(url, json=body, headers = headers)
        if (response.status_code == 200):
            return response.json()
        
        self.throw_exception(response)

    def invoke_delete(self, action):
        if (self.is_log):
            print("Invoking DELETE " + action)

        url = self.get_endpoint(action)
        headers = self.get_headers()

        response = requests.delete(url, headers = headers)
        if (response.status_code == 200):
            return response.json()
        elif (response.status_code == 204):
            return None
        
        self.throw_exception(response)
