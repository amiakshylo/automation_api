import allure
from allure import epic
from utils.cheking import Checking
from requests import Response
from utils.api import Google_maps_api


"""Creating, changing, deleting location"""
@allure.epic("Test vreate new location")
class Test_google_maps_api:
    place_id = None

    @allure.epic("Test create new location")
    @staticmethod
    def test_create_new_location():
        print("POST request")
        result_post: Response = Google_maps_api.create_new_place()
        call_place_id = result_post.json()
        Test_google_maps_api.place_id = call_place_id.get("place_id")  # Set the class variable
        Checking.check_status_code(result_post, 200)
        Checking.check_mandatory_field(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_value_fields(result_post, "status", "OK")

    @allure.epic("Test change new location")
    @staticmethod
    def test_change_new_location():
        print("PUT request (Change address to '3021 17 Ave, SW, Toronto, Canada'")
        place_id = Test_google_maps_api.place_id  # Access the class variable place_id
        result_put: Response = Google_maps_api.change_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_mandatory_field(result_put, ['msg'])
        Checking.check_value_fields(result_put, "msg", "Address successfully updated")

    @allure.epic("Test get new location after changing")
    @staticmethod
    def test_get_new_location_after_putting():
        print("GET after PUT request")
        place_id = Test_google_maps_api.place_id  # Access the class variable place_id
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_mandatory_field(result_get,
                                       ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                        'language'])
        Checking.check_value_fields(result_get, "address", "3021 17 Ave, SW, Toronto, Canada")

    @allure.epic("Test delete new location")
    @staticmethod
    def test_delete_new_location():
        print("DELETE request")
        place_id = Test_google_maps_api.place_id  # Access the class variable place_id
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_mandatory_field(result_delete, ['status'])
        Checking.check_value_fields(result_delete, "status", "OK")

    @allure.epic("Test get new location after deleting")
    @staticmethod
    def test_get_new_location_after_deleting():
        print("GET after DELETE request")
        place_id = Test_google_maps_api.place_id
        result_get: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_mandatory_field(result_get, ['msg'])
        Checking.check_value_fields(result_get, "msg", "Delete operation failed, looks like the data doesn't exists")

        print("All tests successfully done!")


@allure.epic("Test create new location")
def test_get_new_location_after_adding():
    print("GET after POST request")
    place_id = Test_google_maps_api.place_id  # Access the class variable place_id
    result_get: Response = Google_maps_api.get_new_place(place_id)
    Checking.check_status_code(result_get, 200)
    Checking.check_mandatory_field(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                                'website', 'language'])
    Checking.check_value_fields(result_get, "address", "234 15 Street NW, Toronto, Ca")
