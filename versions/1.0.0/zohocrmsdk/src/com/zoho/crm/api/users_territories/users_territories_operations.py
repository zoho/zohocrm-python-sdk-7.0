try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class UsersTerritoriesOperations(object):
	def __init__(self, user):
		"""
		Creates an instance of UsersTerritoriesOperations with the given parameters

		Parameters:
			user (int) : An int representing the user
		"""

		if not isinstance(user, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: int', None, None)
		
		self.__user = user


	def get_territories_of_user(self):
		"""
		The method to get territories of user

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def associate_territories_to_user(self, request):
		"""
		The method to associate territories to user

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_territory_of_user(self, territory):
		"""
		The method to get territory of user

		Parameters:
			territory (int) : An int representing the territory

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories/'
		api_path = api_path + str(territory)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def validate_before_transfer_for_all_territories(self):
		"""
		The method to validate before transfer for all territories

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories/actions/validate_before_transfer'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.validation_handler import ValidationHandler
		except Exception:
			from .validation_handler import ValidationHandler
		return handler_instance.api_call(ValidationHandler.__module__, 'application/json')

	def validate_before_transfer(self, territory):
		"""
		The method to validate before transfer

		Parameters:
			territory (int) : An int representing the territory

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/actions/validate_before_transfer'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.validation_handler import ValidationHandler
		except Exception:
			from .validation_handler import ValidationHandler
		return handler_instance.api_call(ValidationHandler.__module__, 'application/json')

	def delink_and_transfer_from_all_territories(self, request):
		"""
		The method to delink and transfer from all territories

		Parameters:
			request (TransferWrapper) : An instance of TransferWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.transfer_wrapper import TransferWrapper
		except Exception:
			from .transfer_wrapper import TransferWrapper

		if request is not None and not isinstance(request, TransferWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: TransferWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories/actions/transfer_and_delink'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.transfer_action_handler import TransferActionHandler
		except Exception:
			from .transfer_action_handler import TransferActionHandler
		return handler_instance.api_call(TransferActionHandler.__module__, 'application/json')

	def delink_and_transfer_from_specific_territory(self, territory, request):
		"""
		The method to delink and transfer from specific territory

		Parameters:
			territory (int) : An int representing the territory
			request (TransferWrapper) : An instance of TransferWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.transfer_wrapper import TransferWrapper
		except Exception:
			from .transfer_wrapper import TransferWrapper

		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, TransferWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: TransferWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v7/users/'
		api_path = api_path + str(self.__user)
		api_path = api_path + '/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/actions/transfer_and_delink'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.transfer_action_handler import TransferActionHandler
		except Exception:
			from .transfer_action_handler import TransferActionHandler
		return handler_instance.api_call(TransferActionHandler.__module__, 'application/json')
