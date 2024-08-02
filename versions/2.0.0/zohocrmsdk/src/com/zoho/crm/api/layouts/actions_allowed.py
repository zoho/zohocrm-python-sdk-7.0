try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ActionsAllowed(object):
	def __init__(self):
		"""Creates an instance of ActionsAllowed"""

		self.__edit = None
		self.__rename = None
		self.__clone = None
		self.__downgrade = None
		self.__delete = None
		self.__deactivate = None
		self.__set_layout_permissions = None
		self.__key_modified = dict()

	def get_edit(self):
		"""
		The method to get the edit

		Returns:
			bool: A bool representing the edit
		"""

		return self.__edit

	def set_edit(self, edit):
		"""
		The method to set the value to edit

		Parameters:
			edit (bool) : A bool representing the edit
		"""

		if edit is not None and not isinstance(edit, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: edit EXPECTED TYPE: bool', None, None)
		
		self.__edit = edit
		self.__key_modified['edit'] = 1

	def get_rename(self):
		"""
		The method to get the rename

		Returns:
			bool: A bool representing the rename
		"""

		return self.__rename

	def set_rename(self, rename):
		"""
		The method to set the value to rename

		Parameters:
			rename (bool) : A bool representing the rename
		"""

		if rename is not None and not isinstance(rename, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rename EXPECTED TYPE: bool', None, None)
		
		self.__rename = rename
		self.__key_modified['rename'] = 1

	def get_clone(self):
		"""
		The method to get the clone

		Returns:
			bool: A bool representing the clone
		"""

		return self.__clone

	def set_clone(self, clone):
		"""
		The method to set the value to clone

		Parameters:
			clone (bool) : A bool representing the clone
		"""

		if clone is not None and not isinstance(clone, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: clone EXPECTED TYPE: bool', None, None)
		
		self.__clone = clone
		self.__key_modified['clone'] = 1

	def get_downgrade(self):
		"""
		The method to get the downgrade

		Returns:
			bool: A bool representing the downgrade
		"""

		return self.__downgrade

	def set_downgrade(self, downgrade):
		"""
		The method to set the value to downgrade

		Parameters:
			downgrade (bool) : A bool representing the downgrade
		"""

		if downgrade is not None and not isinstance(downgrade, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: downgrade EXPECTED TYPE: bool', None, None)
		
		self.__downgrade = downgrade
		self.__key_modified['downgrade'] = 1

	def get_delete(self):
		"""
		The method to get the delete

		Returns:
			bool: A bool representing the delete
		"""

		return self.__delete

	def set_delete(self, delete):
		"""
		The method to set the value to delete

		Parameters:
			delete (bool) : A bool representing the delete
		"""

		if delete is not None and not isinstance(delete, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete EXPECTED TYPE: bool', None, None)
		
		self.__delete = delete
		self.__key_modified['delete'] = 1

	def get_deactivate(self):
		"""
		The method to get the deactivate

		Returns:
			bool: A bool representing the deactivate
		"""

		return self.__deactivate

	def set_deactivate(self, deactivate):
		"""
		The method to set the value to deactivate

		Parameters:
			deactivate (bool) : A bool representing the deactivate
		"""

		if deactivate is not None and not isinstance(deactivate, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deactivate EXPECTED TYPE: bool', None, None)
		
		self.__deactivate = deactivate
		self.__key_modified['deactivate'] = 1

	def get_set_layout_permissions(self):
		"""
		The method to get the set_layout_permissions

		Returns:
			bool: A bool representing the set_layout_permissions
		"""

		return self.__set_layout_permissions

	def set_set_layout_permissions(self, set_layout_permissions):
		"""
		The method to set the value to set_layout_permissions

		Parameters:
			set_layout_permissions (bool) : A bool representing the set_layout_permissions
		"""

		if set_layout_permissions is not None and not isinstance(set_layout_permissions, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: set_layout_permissions EXPECTED TYPE: bool', None, None)
		
		self.__set_layout_permissions = set_layout_permissions
		self.__key_modified['set_layout_permissions'] = 1

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
