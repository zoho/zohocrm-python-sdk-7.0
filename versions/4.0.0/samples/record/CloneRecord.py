from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.record.record_operations import RecordOperations
from zohocrmsdk.src.com.zoho.crm.api.record.action_response import ActionResponse
from zohocrmsdk.src.com.zoho.crm.api.record.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.record.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.record.success_response import SuccessResponse


class CloneRecord:
    @staticmethod
    def clone_record(module_api_name, record_id):
        record_operations = RecordOperations(module_api_name)
        response = record_operations.clone_record(record_id)

        if response:
            print("Status Code: " + str(response.get_status_code()))

            action_handler = response.get_object()

            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_responses = action_wrapper.get_data()

                for action_response in action_responses:
                    if isinstance(action_response, SuccessResponse):
                        success_response = action_response
                        print("Status: " + success_response.get_status().get_value())
                        print("Code: " + success_response.get_code().get_value())
                        print("Details: ")

                        if success_response.get_details():
                            for key, value in success_response.get_details().items():
                                print(f"{key}: {value}")

                        print("Message: " + success_response.get_message().get_value())

                    elif isinstance(action_response, APIException):
                        exception = action_response
                        print("Status: " + exception.get_status().get_value())
                        print("Code: " + exception.get_code().get_value())
                        print("Details: ")

                        if exception.get_details():
                            for key, value in exception.get_details().items():
                                print(f"{key}: {value}")

                        print("Message: " + exception.get_message().get_value())

            elif isinstance(action_handler, APIException):
                exception = action_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")

                if exception.get_details():
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")

                print("Message: " + exception.get_message().get_value())

            else:
                response_object = response.get_model()
                response_dict = response_object.__dict__
                for key, value in response_dict.items():
                    print(f"{key}: {value}")

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id='Client_Id', client_secret='Client_Secret', refresh_token='Refresh_Token')
        Initializer.initialize(environment, token)


module_api_name = "Leads"
record_id = 72722503
CloneRecord.initialize()
CloneRecord.clone_record(module_api_name, record_id)
