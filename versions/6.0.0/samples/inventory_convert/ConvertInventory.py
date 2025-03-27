from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.inventory_convert import InventoryConvertOperations, BodyWrapper, \
    InventoryConverter, ConvertTo, Module, ActionWrapper, SuccessResponse, APIException


class ConvertInventory:

    @staticmethod
    def convert_inventory(record_id, module_api_name):
        inventory_convert_operations = InventoryConvertOperations(record_id, module_api_name)
        request = BodyWrapper()
        inventory_converter = InventoryConverter()
        convert_to_list = []
        convert_to = ConvertTo()
        module = Module()
        module.set_api_name("Sales_Orders")
        module.set_id(85936900105)
        convert_to.set_module(module)
        convert_to_list.append(convert_to)
        inventory_converter.set_convert_to(convert_to_list)
        request.set_data([inventory_converter])
        response = inventory_convert_operations.convert_inventory(request)

        if response is not None:
            print("Status Code:", response.get_status_code())
            action_handler = response.get_object()
            if isinstance(action_handler, ActionWrapper):
                for action_response in action_handler.get_data():
                    if isinstance(action_response, SuccessResponse):
                        print("Status:", action_response.get_status().get_value())
                        print("Code:", action_response.get_code().get_value())
                        print("Details:", action_response.get_details())
                        print("Message:", action_response.get_message().get_value())
                    elif isinstance(action_response, APIException):
                        print("Status:", action_response.get_status().get_value())
                        print("Code:", action_response.get_code().get_value())
                        print("Details:", action_response.get_details())
                        print("Message:", action_response.get_message().get_value())
            elif isinstance(action_handler, APIException):
                print("Status:", action_handler.get_status().get_value())
                print("Code:", action_handler.get_code().get_value())
                print("Details:", action_handler.get_details())
                print("Message:", action_handler.get_message().get_value())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id='Client_Id', client_secret='Client_Secret', refresh_token='Refresh_Token')
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


record_id = 859369457208
module_api_name = "Quotes"
ConvertInventory.initialize()
ConvertInventory.convert_inventory(record_id, module_api_name)