try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
	from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.action_response import ActionResponse
	from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.response_handler import ResponseHandler
	from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants
	from .action_response import ActionResponse
	from .response_handler import ResponseHandler
	from .action_handler import ActionHandler


class APIException(ActionResponse, ActionHandler, ResponseHandler):
	def __init__(self):
		"""Creates an instance of APIException"""
		super().__init__()

		self.__code = None
		self.__details = None
		self.__message = None
		self.__status = None
		self.__key_modified = dict()
		self.__x_error = None
		self.__info = None

	def get_code(self):
		"""
		The method to get the code

		Returns:
			Choice: An instance of Choice
		"""

		return self.__code

	def set_code(self, code):
		"""
		The method to set the value to code

		Parameters:
			code (Choice) : An instance of Choice
		"""

		if code is not None and not isinstance(code, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: code EXPECTED TYPE: Choice', None, None)
		
		self.__code = code
		self.__key_modified['code'] = 1

	def get_details(self):
		"""
		The method to get the details

		Returns:
			dict: An instance of dict
		"""

		return self.__details

	def set_details(self, details):
		"""
		The method to set the value to details

		Parameters:
			details (dict) : An instance of dict
		"""

		if details is not None and not isinstance(details, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: details EXPECTED TYPE: dict', None, None)
		
		self.__details = details
		self.__key_modified['details'] = 1

	def get_message(self):
		"""
		The method to get the message

		Returns:
			string: A string representing the message
		"""

		return self.__message

	def set_message(self, message):
		"""
		The method to set the value to message

		Parameters:
			message (string) : A string representing the message
		"""

		if message is not None and not isinstance(message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message EXPECTED TYPE: str', None, None)
		
		self.__message = message
		self.__key_modified['message'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			Choice: An instance of Choice
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (Choice) : An instance of Choice
		"""

		if status is not None and not isinstance(status, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: Choice', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification

	def get_x_error(self):
		"""
		The method to get the x_error

		Returns:
			string: A string representing the x_error
		"""

		return self.__x_error

	def set_x_error(self, x_error):
		"""
		The method to set the value to x_error

		Parameters:
			x_error (string) : A string representing the x_error
		"""

		if x_error is not None and not isinstance(x_error, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: x_error EXPECTED TYPE: str', None, None)
		
		self.__x_error = x_error
		self.__key_modified['x-error'] = 1

	def get_info(self):
		"""
		The method to get the info

		Returns:
			string: A string representing the info
		"""

		return self.__info

	def set_info(self, info):
		"""
		The method to set the value to info

		Parameters:
			info (string) : A string representing the info
		"""

		if info is not None and not isinstance(info, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: info EXPECTED TYPE: str', None, None)
		
		self.__info = info
		self.__key_modified['info'] = 1
