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
Configuration for visualizer gslbvserver binding resource
'''

class ns_visualizer_gslb_bindings(base_resource):
	_gslbdomain_lbmonitor_binding=[]
	_gslbdomain_gslbvserver_binding=[]
	_gslbdomain_gslbservice_binding=[]
	_name= ""
	_ip_address= ""
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
			return "ns_visualizer_gslb_bindings"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "ns_visualizer_gslb_bindingss"
		except Exception as e :
			raise e



	'''
	get lb monitor binding of Gslbvserver
	'''
	@property
	def gslbdomain_lbmonitor_binding(self) :
		try:
			return self._gslbdomain_lbmonitor_binding
		except Exception as e :
			raise e
	'''
	set lb monitor binding of Gslbvserver
	'''
	@gslbdomain_lbmonitor_binding.setter
	def gslbdomain_lbmonitor_binding(self,gslbdomain_lbmonitor_binding) :
		try :
			if not isinstance(gslbdomain_lbmonitor_binding,list):
				raise TypeError("gslbdomain_lbmonitor_binding must be set to array of str value")
			for item in gslbdomain_lbmonitor_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._gslbdomain_lbmonitor_binding = gslbdomain_lbmonitor_binding
		except Exception as e :
			raise e


	'''
	get Service binding of Gslbvserver
	'''
	@property
	def gslbdomain_gslbvserver_binding(self) :
		try:
			return self._gslbdomain_gslbvserver_binding
		except Exception as e :
			raise e
	'''
	set Service binding of Gslbvserver
	'''
	@gslbdomain_gslbvserver_binding.setter
	def gslbdomain_gslbvserver_binding(self,gslbdomain_gslbvserver_binding) :
		try :
			if not isinstance(gslbdomain_gslbvserver_binding,list):
				raise TypeError("gslbdomain_gslbvserver_binding must be set to array of str value")
			for item in gslbdomain_gslbvserver_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._gslbdomain_gslbvserver_binding = gslbdomain_gslbvserver_binding
		except Exception as e :
			raise e


	'''
	get GSLB service binding of Gslbvserver
	'''
	@property
	def gslbdomain_gslbservice_binding(self) :
		try:
			return self._gslbdomain_gslbservice_binding
		except Exception as e :
			raise e
	'''
	set GSLB service binding of Gslbvserver
	'''
	@gslbdomain_gslbservice_binding.setter
	def gslbdomain_gslbservice_binding(self,gslbdomain_gslbservice_binding) :
		try :
			if not isinstance(gslbdomain_gslbservice_binding,list):
				raise TypeError("gslbdomain_gslbservice_binding must be set to array of str value")
			for item in gslbdomain_gslbservice_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._gslbdomain_gslbservice_binding = gslbdomain_gslbservice_binding
		except Exception as e :
			raise e


	'''
	get Name of gslbvserver
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of gslbvserver
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
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get gslbvserver bindings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_visualizer_gslb_bindings_obj=ns_visualizer_gslb_bindings()
				response = ns_visualizer_gslb_bindings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_visualizer_gslb_bindings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_visualizer_gslb_bindings_obj = ns_visualizer_gslb_bindings()
			option_ = options()
			option_._filter=filter_
			return ns_visualizer_gslb_bindings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_visualizer_gslb_bindings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_visualizer_gslb_bindings_obj = ns_visualizer_gslb_bindings()
			option_ = options()
			option_._count=True
			response = ns_visualizer_gslb_bindings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_visualizer_gslb_bindings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_visualizer_gslb_bindings_obj = ns_visualizer_gslb_bindings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_visualizer_gslb_bindings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_visualizer_gslb_bindings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_visualizer_gslb_bindings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_visualizer_gslb_bindings_responses, response, "ns_visualizer_gslb_bindings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_visualizer_gslb_bindings_response_array
				i=0
				error = [ns_visualizer_gslb_bindings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_visualizer_gslb_bindings_response_array
			i=0
			ns_visualizer_gslb_bindings_objs = [ns_visualizer_gslb_bindings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_visualizer_gslb_bindings'):
					for props in obj._ns_visualizer_gslb_bindings:
						result = service.payload_formatter.string_to_bulk_resource(ns_visualizer_gslb_bindings_response,self.__class__.__name__,props)
						ns_visualizer_gslb_bindings_objs[i] = result.ns_visualizer_gslb_bindings
						i=i+1
			return ns_visualizer_gslb_bindings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_visualizer_gslb_bindings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_visualizer_gslb_bindings_response(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_gslb_bindings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_visualizer_gslb_bindings= [ ns_visualizer_gslb_bindings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_visualizer_gslb_bindings_responses(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_gslb_bindings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_visualizer_gslb_bindings_response_array = [ ns_visualizer_gslb_bindings() for _ in range(length)]
