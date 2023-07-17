"""Checking for Google Maps API"""
import requests
from utils.http_methods_for_google_api import Http_method

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"
class Google_maps_api:

    """Creating new place"""
    @staticmethod
    def create_new_place():
        json_for_creating_new_location = {
            "location":{
        "lat":-38.383494,
        "lng":33.427362
        }, "accuracy":50,
        "name":"Frontlinehouse",
        "phone_number":"(+91)9838933937",
        "address":"234 15 Street NW, Toronto, Ca",
        "types":[
        "shoepark",
        "shop"
        ],
        "website":"http://google.com",
        "language":"French-IN"

        }
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)
        post_request = Http_method.post(post_url, json_for_creating_new_location)
        print(post_request.text)
        return post_request

    """Getting new place by place_id"""
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        get_request = Http_method.get(get_url)
        print(get_request.text)
        return get_request


    """Changing new place by place_id"""

    @staticmethod
    def change_new_place(place_id):
        put_resource = "/maps/api/place/update/json"
        json_for_changing_location = {
        "place_id": place_id,
        "address": "3021 17 Ave, SW, Toronto, Canada",
        "key": "qaclick123"
        }

        put_url = base_url + put_resource + key
        print(put_url)
        put_request = Http_method.put(put_url, json_for_changing_location)
        print(put_request.text)
        return put_request

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }
        delete_request = Http_method.delete(delete_url, json_for_delete_location)
        print(delete_request.text)
        return delete_request





