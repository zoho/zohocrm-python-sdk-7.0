try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.conversion_option.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__conversionoptions = None
		self.__key_modified = dict()

	def get_conversionoptions(self):
		"""
		The method to get the conversionoptions

		Returns:
			ConversionOptions: An instance of ConversionOptions
		"""

		return self.__conversionoptions

	def set_conversionoptions(self, conversionoptions):
		"""
		The method to set the value to conversionoptions

		Parameters:
			conversionoptions (ConversionOptions) : An instance of ConversionOptions
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.conversion_option.conversion_options import ConversionOptions
		except Exception:
			from .conversion_options import ConversionOptions

		if conversionoptions is not None and not isinstance(conversionoptions, ConversionOptions):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: conversionoptions EXPECTED TYPE: ConversionOptions', None, None)
		
		self.__conversionoptions = conversionoptions
		self.__key_modified['__conversion_options'] = 1

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
