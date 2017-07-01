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
Configuration for Tenant Network Pools resource
'''

class tenant_network_pool(base_resource):
	_tenant_id= ""
	_parent_name= ""
	_is_assigned= ""
	_id= ""
	_network_pool_id= ""
	_parent_id= ""
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
			return "tenant_network_pool"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "tenant_network_pools"
		except Exception as e :
			raise e



	'''
	get Id of the parent tenant
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Id of the parent tenant
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get To check whether network pool is assigned or not
	'''
	@property
	def is_assigned(self) :
		try:
			return self._is_assigned
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e


	'''
	get Id of network pool
	'''
	@property
	def network_pool_id(self) :
		try:
			return self._network_pool_id
		except Exception as e :
			raise e
	'''
	set Id of network pool
	'''
	@network_pool_id.setter
	def network_pool_id(self,network_pool_id):
		try :
			if not isinstance(network_pool_id,str):
				raise TypeError("network_pool_id must be set to str value")
			self._network_pool_id = network_pool_id
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_network_pool_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_network_pool
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_network_pool_responses, response, "tenant_network_pool_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_network_pool_response_array
				i=0
				error = [tenant_network_pool() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_network_pool_response_array
			i=0
			tenant_network_pool_objs = [tenant_network_pool() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_network_pool'):
					for props in obj._tenant_network_pool:
						result = service.payload_formatter.string_to_bulk_resource(tenant_network_pool_response,self.__class__.__name__,props)
						tenant_network_pool_objs[i] = result.tenant_network_pool
						i=i+1
			return tenant_network_pool_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_network_pool,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_network_pool_response(base_response):
	def __init__(self,length=1) :
		self.tenant_network_pool= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_network_pool= [ tenant_network_pool() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_network_pool_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_network_pool_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_network_pool_response_array = [ tenant_network_pool() for _ in range(length)]
