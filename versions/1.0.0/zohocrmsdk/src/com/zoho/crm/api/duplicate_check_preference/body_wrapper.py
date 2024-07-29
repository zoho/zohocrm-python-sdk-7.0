try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__duplicate_check_preference = None
		self.__key_modified = dict()

	def get_duplicate_check_preference(self):
		"""
		The method to get the duplicate_check_preference

		Returns:
			DuplicateCheckPreference: An instance of DuplicateCheckPreference
		"""

		return self.__duplicate_check_preference

	def set_duplicate_check_preference(self, duplicate_check_preference):
		"""
		The method to set the value to duplicate_check_preference

		Parameters:
			duplicate_check_preference (DuplicateCheckPreference) : An instance of DuplicateCheckPreference
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.duplicate_check_preference import DuplicateCheckPreference
		except Exception:
			from .duplicate_check_preference import DuplicateCheckPreference

		if duplicate_check_preference is not None and not isinstance(duplicate_check_preference, DuplicateCheckPreference):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: duplicate_check_preference EXPECTED TYPE: DuplicateCheckPreference', None, None)
		
		self.__duplicate_check_preference = duplicate_check_preference
		self.__key_modified['duplicate_check_preference'] = 1

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
