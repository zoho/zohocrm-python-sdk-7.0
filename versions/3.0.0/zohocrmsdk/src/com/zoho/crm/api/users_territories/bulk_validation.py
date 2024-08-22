try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.users_territories.validation_group import ValidationGroup
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .validation_group import ValidationGroup


class BulkValidation(ValidationGroup):
	def __init__(self):
		"""Creates an instance of BulkValidation"""
		super().__init__()

		self.__alert = None
		self.__assignment = None
		self.__criteria = None
		self.__name = None
		self.__id = None
		self.__key_modified = dict()

	def get_alert(self):
		"""
		The method to get the alert

		Returns:
			bool: A bool representing the alert
		"""

		return self.__alert

	def set_alert(self, alert):
		"""
		The method to set the value to alert

		Parameters:
			alert (bool) : A bool representing the alert
		"""

		if alert is not None and not isinstance(alert, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: alert EXPECTED TYPE: bool', None, None)
		
		self.__alert = alert
		self.__key_modified['alert'] = 1

	def get_assignment(self):
		"""
		The method to get the assignment

		Returns:
			bool: A bool representing the assignment
		"""

		return self.__assignment

	def set_assignment(self, assignment):
		"""
		The method to set the value to assignment

		Parameters:
			assignment (bool) : A bool representing the assignment
		"""

		if assignment is not None and not isinstance(assignment, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assignment EXPECTED TYPE: bool', None, None)
		
		self.__assignment = assignment
		self.__key_modified['assignment'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			bool: A bool representing the criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (bool) : A bool representing the criteria
		"""

		if criteria is not None and not isinstance(criteria, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: bool', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

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
