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
from massrc.com.citrix.mas.nitro.resource.config.mps.network_service_lb_config import network_service_lb_config


'''
Configuration for Network Service Config Sets resource
'''

class network_service_configsets(base_resource):
	_service_lb_configs=[]
	_formation_template_id= ""
	_network_service_id= ""
	_id= ""
	_network_service_name= ""
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
			return "network_service_configsets"
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
			return "network_service_configsetss"
		except Exception as e :
			raise e



	'''
	get Network Service LB Configs Array
	'''
	@property
	def service_lb_configs(self) :
		try:
			return self._service_lb_configs
		except Exception as e :
			raise e
	'''
	set Network Service LB Configs Array
	'''
	@service_lb_configs.setter
	def service_lb_configs(self,service_lb_configs) :
		try :
			if not isinstance(service_lb_configs,list):
				raise TypeError("service_lb_configs must be set to array of network_service_lb_config value")
			for item in service_lb_configs :
				if not isinstance(item,network_service_lb_config):
					raise TypeError("item must be set to network_service_lb_config value")
			self._service_lb_configs = service_lb_configs
		except Exception as e :
			raise e


	'''
	get Formation Template ID
	'''
	@property
	def formation_template_id(self) :
		try:
			return self._formation_template_id
		except Exception as e :
			raise e
	'''
	set Formation Template ID
	'''
	@formation_template_id.setter
	def formation_template_id(self,formation_template_id):
		try :
			if not isinstance(formation_template_id,str):
				raise TypeError("formation_template_id must be set to str value")
			self._formation_template_id = formation_template_id
		except Exception as e :
			raise e


	'''
	get Network Service ID
	'''
	@property
	def network_service_id(self) :
		try:
			return self._network_service_id
		except Exception as e :
			raise e
	'''
	set Network Service ID
	'''
	@network_service_id.setter
	def network_service_id(self,network_service_id):
		try :
			if not isinstance(network_service_id,str):
				raise TypeError("network_service_id must be set to str value")
			self._network_service_id = network_service_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the networks
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the networks
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
	get Network Service Name
	'''
	@property
	def network_service_name(self) :
		try:
			return self._network_service_name
		except Exception as e :
			raise e
	'''
	set Network Service Name
	'''
	@network_service_name.setter
	def network_service_name(self,network_service_name):
		try :
			if not isinstance(network_service_name,str):
				raise TypeError("network_service_name must be set to str value")
			self._network_service_name = network_service_name
		except Exception as e :
			raise e

	'''
	Use this operation to get the network service config sets.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				network_service_configsets_obj=network_service_configsets()
				response = network_service_configsets_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network_service_configsets resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_service_configsets_obj = network_service_configsets()
			option_ = options()
			option_._filter=filter_
			return network_service_configsets_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network_service_configsets resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_service_configsets_obj = network_service_configsets()
			option_ = options()
			option_._count=True
			response = network_service_configsets_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network_service_configsets resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_service_configsets_obj = network_service_configsets()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_service_configsets_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_service_configsets_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_service_configsets
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_service_configsets_responses, response, "network_service_configsets_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_service_configsets_response_array
				i=0
				error = [network_service_configsets() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_service_configsets_response_array
			i=0
			network_service_configsets_objs = [network_service_configsets() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_service_configsets'):
					for props in obj._network_service_configsets:
						result = service.payload_formatter.string_to_bulk_resource(network_service_configsets_response,self.__class__.__name__,props)
						network_service_configsets_objs[i] = result.network_service_configsets
						i=i+1
			return network_service_configsets_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_service_configsets,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_service_configsets_response(base_response):
	def __init__(self,length=1) :
		self.network_service_configsets= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_service_configsets= [ network_service_configsets() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_service_configsets_responses(base_response):
	def __init__(self,length=1) :
		self.network_service_configsets_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_service_configsets_response_array = [ network_service_configsets() for _ in range(length)]
