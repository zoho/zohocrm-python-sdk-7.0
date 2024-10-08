try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Action(object):
	def __init__(self):
		"""Creates an instance of Action"""

		self.__details = None
		self.__type = None
		self.__key_modified = dict()

	def get_details(self):
		"""
		The method to get the details

		Returns:
			Details: An instance of Details
		"""

		return self.__details

	def set_details(self, details):
		"""
		The method to set the value to details

		Parameters:
			details (Details) : An instance of Details
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.details import Details
		except Exception:
			from .details import Details

		if details is not None and not isinstance(details, Details):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: details EXPECTED TYPE: Details', None, None)
		
		self.__details = details
		self.__key_modified['details'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

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
