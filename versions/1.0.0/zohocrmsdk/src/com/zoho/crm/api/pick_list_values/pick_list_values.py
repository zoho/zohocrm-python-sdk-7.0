try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class PickListValues(object):
	def __init__(self):
		"""Creates an instance of PickListValues"""

		self.__sequence_number = None
		self.__display_value = None
		self.__reference_value = None
		self.__colour_code = None
		self.__actual_value = None
		self.__id = None
		self.__type = None
		self.__layout_associations = None
		self.__key_modified = dict()

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			int: An int representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (int) : An int representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: int', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_reference_value(self):
		"""
		The method to get the reference_value

		Returns:
			string: A string representing the reference_value
		"""

		return self.__reference_value

	def set_reference_value(self, reference_value):
		"""
		The method to set the value to reference_value

		Parameters:
			reference_value (string) : A string representing the reference_value
		"""

		if reference_value is not None and not isinstance(reference_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reference_value EXPECTED TYPE: str', None, None)
		
		self.__reference_value = reference_value
		self.__key_modified['reference_value'] = 1

	def get_colour_code(self):
		"""
		The method to get the colour_code

		Returns:
			string: A string representing the colour_code
		"""

		return self.__colour_code

	def set_colour_code(self, colour_code):
		"""
		The method to set the value to colour_code

		Parameters:
			colour_code (string) : A string representing the colour_code
		"""

		if colour_code is not None and not isinstance(colour_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: colour_code EXPECTED TYPE: str', None, None)
		
		self.__colour_code = colour_code
		self.__key_modified['colour_code'] = 1

	def get_actual_value(self):
		"""
		The method to get the actual_value

		Returns:
			string: A string representing the actual_value
		"""

		return self.__actual_value

	def set_actual_value(self, actual_value):
		"""
		The method to set the value to actual_value

		Parameters:
			actual_value (string) : A string representing the actual_value
		"""

		if actual_value is not None and not isinstance(actual_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actual_value EXPECTED TYPE: str', None, None)
		
		self.__actual_value = actual_value
		self.__key_modified['actual_value'] = 1

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

	def get_layout_associations(self):
		"""
		The method to get the layout_associations

		Returns:
			list: An instance of list
		"""

		return self.__layout_associations

	def set_layout_associations(self, layout_associations):
		"""
		The method to set the value to layout_associations

		Parameters:
			layout_associations (list) : An instance of list
		"""

		if layout_associations is not None and not isinstance(layout_associations, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout_associations EXPECTED TYPE: list', None, None)
		
		self.__layout_associations = layout_associations
		self.__key_modified['layout_associations'] = 1

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
