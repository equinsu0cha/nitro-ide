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
Configuration for Setting of Placement Policy resource
'''

class placementpolicy(base_resource):
	_tenant_id= ""
	_expression= ""
	_name= ""
	_id= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/oca/v1/placementpolicys"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "placementpolicys"
		except Exception as e :
			raise e

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
			return "placementpolicy"
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
			return "placementpolicys"
		except Exception as e :
			raise e



	'''
	get Tenant id of the network
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant id of the network
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
	get expression of the placementpolicy
	'''
	@property
	def expression(self) :
		try:
			return self._expression
		except Exception as e :
			raise e
	'''
	set expression of the placementpolicy
	'''
	@expression.setter
	def expression(self,expression):
		try :
			if not isinstance(expression,str):
				raise TypeError("expression must be set to str value")
			self._expression = expression
		except Exception as e :
			raise e


	'''
	get Name of placementpolicy
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of placementpolicy
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Id of the placementpolicy
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id of the placementpolicy
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
	Use this operation to add a placementpolicy.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				placementpolicy_obj= placementpolicy()
				return cls.perform_operation_bulk_request(service,"add", resource,placementpolicy_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a placementpolicy.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					placementpolicy_obj=placementpolicy()
					return cls.delete_bulk_request(client,resource,placementpolicy_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get placementpolicy details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				placementpolicy_obj=placementpolicy()
				response = placementpolicy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update a placementpolicy.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				placementpolicy_obj=resource[0]
				return cls.update_bulk_request(client,resource,placementpolicy_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of placementpolicy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			placementpolicy_obj = placementpolicy()
			option_ = options()
			option_._filter=filter_
			return placementpolicy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the placementpolicy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			placementpolicy_obj = placementpolicy()
			option_ = options()
			option_._count=True
			response = placementpolicy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of placementpolicy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			placementpolicy_obj = placementpolicy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = placementpolicy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(placementpolicy_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.placementpolicy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(placementpolicy_responses, response, "placementpolicy_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.placementpolicy_response_array
				i=0
				error = [placementpolicy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.placementpolicy_response_array
			i=0
			placementpolicy_objs = [placementpolicy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_placementpolicy'):
					for props in obj._placementpolicy:
						result = service.payload_formatter.string_to_bulk_resource(placementpolicy_response,self.__class__.__name__,props)
						placementpolicy_objs[i] = result.placementpolicy
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(placementpolicy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class placementpolicy_response(base_response):
	def __init__(self,length=1) :
		self.placementpolicy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.placementpolicy= [ placementpolicy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class placementpolicy_responses(base_response):
	def __init__(self,length=1) :
		self.placementpolicy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.placementpolicy_response_array = [ placementpolicy() for _ in range(length)]
