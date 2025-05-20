from requests import Response

import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
responses = post_new_user(data.user_body)
print(responses.status_code)
print(responses.json())

from configuration import URL_SERVICE, CREATE_USER_PATH
def send_create_user_request(first_name):
    url = URL_SERVICE + CREATE_USER_PATH
    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "firstName": first_name,
        "lastName": "TestLast",
        "phone": "+34123456789",
        "email": "test@example.com",
        "address": "123 Elm St",
        "age": 25
    }
    response = requests.post(url, json=body, headers=headers)
    print("Response status code:", response.status_code)
    print("Response body:", response.text)
    return response

import requests
from configuration import URL_SERVICE, CREATE_USER_PATH

class SenderStandRequest:
    def post_new_user(self, user_body):
        url = URL_SERVICE + CREATE_USER_PATH
        response = requests.post(url, json=user_body)
        return response

sender_stand_request = SenderStandRequest()


import requests
import configuration
import data
import copy

# Clona el body original y modifica el campo firstName
def send_create_user_request(first_name):
    user_data = copy.deepcopy(data.user_body)
    user_data["firstName"] = first_name
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_data)


def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    return response.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body)






