from datetime import date

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.convert_lead import ConvertLeadOperations, BodyWrapper, LeadConverter, \
    ActionWrapper, APIException, SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import Record, Field
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class ConvertLead:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", refresh_token="refreshToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def convert_lead(lead_id):
        convert_lead_operations = ConvertLeadOperations(lead_id)
        request = BodyWrapper()
        data = list()
        record1 = LeadConverter()
        record1.set_overwrite(True)
        record1.set_notify_lead_owner(True)
        record1.set_notify_new_entity_owner(True)

        accounts = Record()
        accounts.set_id(34770607004)
        record1.set_accounts(accounts)

        contacts = Record()
        contacts.set_id(3477064004)
        record1.set_contacts(contacts)

        assign_to = MinifiedUser()
        assign_to.set_id(3477173021)
        record1.set_assign_to(assign_to)

        deals = Record()
        deals.add_field_value(Field.Deals.deal_name(), "deal_name")
        deals.add_field_value(Field.Deals.description(), "deals description")
        deals.add_field_value(Field.Deals.closing_date(), date(2021, 1, 13))
        deals.add_field_value(Field.Deals.stage(), Choice("Closed Won"))
        deals.add_field_value(Field.Deals.amount(), 50.7)

        deals.add_key_value("Custom_field", "Value")
        deals.add_key_value("Pipeline", Choice("Qualification"))

        record1.set_deals(deals)
        data.append(record1)

        request.set_data(data)
        response = convert_lead_operations.convert_lead(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


ConvertLead.initialize()
ConvertLead.convert_lead(347705200002)
