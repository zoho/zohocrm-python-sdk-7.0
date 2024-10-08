try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__ziaorgenrichment = None
		self.__key_modified = dict()

	def get_ziaorgenrichment(self):
		"""
		The method to get the ziaorgenrichment

		Returns:
			list: An instance of list
		"""

		return self.__ziaorgenrichment

	def set_ziaorgenrichment(self, ziaorgenrichment):
		"""
		The method to set the value to ziaorgenrichment

		Parameters:
			ziaorgenrichment (list) : An instance of list
		"""

		if ziaorgenrichment is not None and not isinstance(ziaorgenrichment, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ziaorgenrichment EXPECTED TYPE: list', None, None)
		
		self.__ziaorgenrichment = ziaorgenrichment
		self.__key_modified['__zia_org_enrichment'] = 1

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
