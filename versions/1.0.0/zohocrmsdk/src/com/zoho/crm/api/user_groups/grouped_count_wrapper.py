try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.user_groups.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class GroupedCountWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of GroupedCountWrapper"""
		super().__init__()

		self.__grouped_counts = None
		self.__info = None
		self.__key_modified = dict()

	def get_grouped_counts(self):
		"""
		The method to get the grouped_counts

		Returns:
			list: An instance of list
		"""

		return self.__grouped_counts

	def set_grouped_counts(self, grouped_counts):
		"""
		The method to set the value to grouped_counts

		Parameters:
			grouped_counts (list) : An instance of list
		"""

		if grouped_counts is not None and not isinstance(grouped_counts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: grouped_counts EXPECTED TYPE: list', None, None)
		
		self.__grouped_counts = grouped_counts
		self.__key_modified['grouped_counts'] = 1

	def get_info(self):
		"""
		The method to get the info

		Returns:
			Info: An instance of Info
		"""

		return self.__info

	def set_info(self, info):
		"""
		The method to set the value to info

		Parameters:
			info (Info) : An instance of Info
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.info import Info
		except Exception:
			from .info import Info

		if info is not None and not isinstance(info, Info):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: info EXPECTED TYPE: Info', None, None)
		
		self.__info = info
		self.__key_modified['info'] = 1

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
