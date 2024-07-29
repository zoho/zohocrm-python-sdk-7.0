try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.users_territories.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__transfer_and_delink = None
		self.__key_modified = dict()
		self.__territories = None

	def get_transfer_and_delink(self):
		"""
		The method to get the transfer_and_delink

		Returns:
			list: An instance of list
		"""

		return self.__transfer_and_delink

	def set_transfer_and_delink(self, transfer_and_delink):
		"""
		The method to set the value to transfer_and_delink

		Parameters:
			transfer_and_delink (list) : An instance of list
		"""

		if transfer_and_delink is not None and not isinstance(transfer_and_delink, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transfer_and_delink EXPECTED TYPE: list', None, None)
		
		self.__transfer_and_delink = transfer_and_delink
		self.__key_modified['transfer_and_delink'] = 1

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

	def get_territories(self):
		"""
		The method to get the territories

		Returns:
			list: An instance of list
		"""

		return self.__territories

	def set_territories(self, territories):
		"""
		The method to set the value to territories

		Parameters:
			territories (list) : An instance of list
		"""

		if territories is not None and not isinstance(territories, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territories EXPECTED TYPE: list', None, None)
		
		self.__territories = territories
		self.__key_modified['territories'] = 1
