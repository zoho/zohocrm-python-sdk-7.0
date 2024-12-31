try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TransferAndDelink(object):
	def __init__(self):
		"""Creates an instance of TransferAndDelink"""

		self.__id = None
		self.__transfer_to_user = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_transfer_to_user(self):
		"""
		The method to get the transfer_to_user

		Returns:
			TransferToUser: An instance of TransferToUser
		"""

		return self.__transfer_to_user

	def set_transfer_to_user(self, transfer_to_user):
		"""
		The method to set the value to transfer_to_user

		Parameters:
			transfer_to_user (TransferToUser) : An instance of TransferToUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_territories.transfer_to_user import TransferToUser
		except Exception:
			from .transfer_to_user import TransferToUser

		if transfer_to_user is not None and not isinstance(transfer_to_user, TransferToUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transfer_to_user EXPECTED TYPE: TransferToUser', None, None)
		
		self.__transfer_to_user = transfer_to_user
		self.__key_modified['transfer_to_user'] = 1

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
