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

    def invoke_get(self, action):
        #print("Invoking: " + action)

        url = self.endpoint + action
        headers = self.get_headers()

        response = requests.get(url, headers = headers)
        if (response.status_code == 200):
            return response.json()
        
        self.throw_exception(response)
