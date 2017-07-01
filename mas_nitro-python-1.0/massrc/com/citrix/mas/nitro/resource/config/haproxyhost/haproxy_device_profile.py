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

from massrc.com.citrix.mas.nitro.resource.config.mps.device_profile import device_profile

'''
Configuration for haproxy_device_profile resource
'''

class haproxy_device_profile(device_profile):
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
			return "haproxy_device_profile"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(haproxy_device_profile,self).get_object_id()
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
			return "haproxy_device_profiles"
		except Exception as e :
			raise e


	'''
	Use this operation to add device profile.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				haproxy_device_profile_obj= haproxy_device_profile()
				return cls.perform_operation_bulk_request(service,"add", resource,haproxy_device_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete device profile(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					haproxy_device_profile_obj=haproxy_device_profile()
					return cls.delete_bulk_request(client,resource,haproxy_device_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get device profiles.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				haproxy_device_profile_obj=haproxy_device_profile()
				response = haproxy_device_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of haproxy_device_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			haproxy_device_profile_obj = haproxy_device_profile()
			option_ = options()
			option_._filter=filter_
			return haproxy_device_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the haproxy_device_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			haproxy_device_profile_obj = haproxy_device_profile()
			option_ = options()
			option_._count=True
			response = haproxy_device_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of haproxy_device_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			haproxy_device_profile_obj = haproxy_device_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = haproxy_device_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(haproxy_device_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.haproxy_device_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(haproxy_device_profile_responses, response, "haproxy_device_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.haproxy_device_profile_response_array
				i=0
				error = [haproxy_device_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.haproxy_device_profile_response_array
			i=0
			haproxy_device_profile_objs = [haproxy_device_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_haproxy_device_profile'):
					for props in obj._haproxy_device_profile:
						result = service.payload_formatter.string_to_bulk_resource(haproxy_device_profile_response,self.__class__.__name__,props)
						haproxy_device_profile_objs[i] = result.haproxy_device_profile
						i=i+1
			return haproxy_device_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(haproxy_device_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class haproxy_device_profile_response(base_response):
	def __init__(self,length=1) :
		self.haproxy_device_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.haproxy_device_profile= [ haproxy_device_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class haproxy_device_profile_responses(base_response):
	def __init__(self,length=1) :
		self.haproxy_device_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.haproxy_device_profile_response_array = [ haproxy_device_profile() for _ in range(length)]
