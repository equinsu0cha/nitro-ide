'''
Copyright (c) 2008-2015 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for ICA session timeout resource
'''

class ica_session_timeout(base_resource):
	_timeout_value= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_session_timeout"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "ica_session_timeouts"
		except Exception as e :
			raise e



	'''
	get Ica session timeout value
	'''
	@property
	def timeout_value(self) :
		try:
			return self._timeout_value
		except Exception as e :
			raise e
	'''
	set Ica session timeout value
	'''
	@timeout_value.setter
	def timeout_value(self,timeout_value):
		try :
			if not isinstance(timeout_value,int):
				raise TypeError("timeout_value must be set to int value")
			self._timeout_value = timeout_value
		except Exception as e :
			raise e

	'''
	To get the ica session timeout.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_session_timeout_obj=ica_session_timeout()
				response = ica_session_timeout_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set the ica session timeout.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ica_session_timeout_obj=ica_session_timeout()
				return cls.update_bulk_request(client,resource,ica_session_timeout_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_session_timeout resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_session_timeout_obj = ica_session_timeout()
			option_ = options()
			option_._filter=filter_
			return ica_session_timeout_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_session_timeout resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_session_timeout_obj = ica_session_timeout()
			option_ = options()
			option_._count=True
			response = ica_session_timeout_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_session_timeout resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_session_timeout_obj = ica_session_timeout()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_session_timeout_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['_count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_session_timeout_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_session_timeout
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_session_timeout_responses, response, "ica_session_timeout_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_session_timeout_response_array
				i=0
				error = [ica_session_timeout() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_session_timeout_response_array
			i=0
			ica_session_timeout_objs = [ica_session_timeout() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ica_session_timeout'):
					for props in obj._ica_session_timeout:
						result = service.payload_formatter.string_to_bulk_resource(ica_session_timeout_response,self.__class__.__name__,props)
						ica_session_timeout_objs[i] = result.ica_session_timeout
						i=i+1
			return ica_session_timeout_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_session_timeout,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_session_timeout_response(base_response):
	def __init__(self,length=1) :
		self.ica_session_timeout= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_session_timeout= [ ica_session_timeout() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_session_timeout_responses(base_response):
	def __init__(self,length=1) :
		self.ica_session_timeout_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_session_timeout_response_array = [ ica_session_timeout() for _ in range(length)]
