import allure
import requests
from utils.logger import Logger
"""Creating custom http method"""


class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            get_request = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookies)
            Logger.add_response(get_request)
            return get_request

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            post_request = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookies)
            Logger.add_response(post_request)
            return post_request

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            put_request = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookies)
            Logger.add_response(put_request)
            return put_request

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            delete_request = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookies)
            Logger.add_response(delete_request)
            return delete_request
