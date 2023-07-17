import json

from requests import Response
from utils.http_methods_for_google_api import Http_method
from utils.api import Google_maps_api

"""Methods for checking responses"""
class Checking():

    """Method for checking status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        print(response.status_code)
        assert status_code == response.status_code, "Status code - " + str(response.status_code) + ", expected - " + str(status_code)
        print("Status code as expected, actual result - " + str(response.status_code))

    """Method for checking mandatory fields"""
    @staticmethod
    def check_mandatory_field(response: Response, expected_value):
        token = response.json()
        assert list(token) == expected_value, "Error, actual result is: " + str(list(token)) + ", expected - " + str(expected_value)
        print(list(token))
        print("Mandatory fields as expected, actual result: " + str(list(token)))

    @staticmethod
    def check_value_fields(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "Value in field '" + field_name + "' is incorrect." + " Must be: " + expected_value
        print("expected_value in field '" + field_name + "' found: '" + expected_value + "'"  )








