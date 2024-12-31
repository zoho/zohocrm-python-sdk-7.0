try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.users_territories.validation_handler import ValidationHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .validation_handler import ValidationHandler


class ValidationWrapper(ValidationHandler):
	def __init__(self):
		"""Creates an instance of ValidationWrapper"""
		super().__init__()

		self.__validate_before_transfer = None
		self.__key_modified = dict()

	def get_validate_before_transfer(self):
		"""
		The method to get the validate_before_transfer

		Returns:
			list: An instance of list
		"""

		return self.__validate_before_transfer

	def set_validate_before_transfer(self, validate_before_transfer):
		"""
		The method to set the value to validate_before_transfer

		Parameters:
			validate_before_transfer (list) : An instance of list
		"""

		if validate_before_transfer is not None and not isinstance(validate_before_transfer, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: validate_before_transfer EXPECTED TYPE: list', None, None)
		
		self.__validate_before_transfer = validate_before_transfer
		self.__key_modified['validate_before_transfer'] = 1

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
