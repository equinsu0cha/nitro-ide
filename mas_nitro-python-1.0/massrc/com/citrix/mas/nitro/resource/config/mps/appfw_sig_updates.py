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
Configuration for App Flow Signature Update resource
'''

class appfw_sig_updates(base_resource):
	_last_updated= ""
	_version= ""
	_release= ""
	_build= ""
	_filename= ""
	_sshfilecontent= ""
	_id= ""
	_md5= ""
	_schema_version= ""
	_filecontent= ""
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
			return "appfw_sig_updates"
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
			return "appfw_sig_updatess"
		except Exception as e :
			raise e



	'''
	get Last Updated.
	'''
	@property
	def last_updated(self) :
		try:
			return self._last_updated
		except Exception as e :
			raise e


	'''
	get NetScaler Version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e


	'''
	get Release of the NetScaler.
	'''
	@property
	def release(self) :
		try:
			return self._release
		except Exception as e :
			raise e


	'''
	get Build Number of NetScaler
	'''
	@property
	def build(self) :
		try:
			return self._build
		except Exception as e :
			raise e


	'''
	get Filename.
	'''
	@property
	def filename(self) :
		try:
			return self._filename
		except Exception as e :
			raise e


	'''
	get SSH File Content.
	'''
	@property
	def sshfilecontent(self) :
		try:
			return self._sshfilecontent
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the appflow updates.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the appflow updates.
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
	get MD5 of File Content.
	'''
	@property
	def md5(self) :
		try:
			return self._md5
		except Exception as e :
			raise e


	'''
	get Schema Version of NetScaler
	'''
	@property
	def schema_version(self) :
		try:
			return self._schema_version
		except Exception as e :
			raise e


	'''
	get File Content.
	'''
	@property
	def filecontent(self) :
		try:
			return self._filecontent
		except Exception as e :
			raise e

	'''
	Use this operation to get appfw updates..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				appfw_sig_updates_obj=appfw_sig_updates()
				response = appfw_sig_updates_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of appfw_sig_updates resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			appfw_sig_updates_obj = appfw_sig_updates()
			option_ = options()
			option_._filter=filter_
			return appfw_sig_updates_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the appfw_sig_updates resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			appfw_sig_updates_obj = appfw_sig_updates()
			option_ = options()
			option_._count=True
			response = appfw_sig_updates_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of appfw_sig_updates resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			appfw_sig_updates_obj = appfw_sig_updates()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = appfw_sig_updates_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(appfw_sig_updates_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfw_sig_updates
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(appfw_sig_updates_responses, response, "appfw_sig_updates_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.appfw_sig_updates_response_array
				i=0
				error = [appfw_sig_updates() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.appfw_sig_updates_response_array
			i=0
			appfw_sig_updates_objs = [appfw_sig_updates() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_appfw_sig_updates'):
					for props in obj._appfw_sig_updates:
						result = service.payload_formatter.string_to_bulk_resource(appfw_sig_updates_response,self.__class__.__name__,props)
						appfw_sig_updates_objs[i] = result.appfw_sig_updates
						i=i+1
			return appfw_sig_updates_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(appfw_sig_updates,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class appfw_sig_updates_response(base_response):
	def __init__(self,length=1) :
		self.appfw_sig_updates= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.appfw_sig_updates= [ appfw_sig_updates() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class appfw_sig_updates_responses(base_response):
	def __init__(self,length=1) :
		self.appfw_sig_updates_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.appfw_sig_updates_response_array = [ appfw_sig_updates() for _ in range(length)]
