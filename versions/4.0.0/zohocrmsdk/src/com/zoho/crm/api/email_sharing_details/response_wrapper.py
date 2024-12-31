try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.email_sharing_details.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__emailssharingdetails = None
		self.__key_modified = dict()

	def get_emailssharingdetails(self):
		"""
		The method to get the emailssharingdetails

		Returns:
			list: An instance of list
		"""

		return self.__emailssharingdetails

	def set_emailssharingdetails(self, emailssharingdetails):
		"""
		The method to set the value to emailssharingdetails

		Parameters:
			emailssharingdetails (list) : An instance of list
		"""

		if emailssharingdetails is not None and not isinstance(emailssharingdetails, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: emailssharingdetails EXPECTED TYPE: list', None, None)
		
		self.__emailssharingdetails = emailssharingdetails
		self.__key_modified['__emails_sharing_details'] = 1

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
