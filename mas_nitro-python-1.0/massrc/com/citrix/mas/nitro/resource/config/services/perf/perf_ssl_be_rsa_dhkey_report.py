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
Configuration for SSL Back-end RSA vs. DH Key exchanges report resource
'''

class perf_ssl_be_rsa_dhkey_report(base_resource):
	_sslbersa2048keyexchangesrate= ""
	_sslbersa512keyexchangesrate= ""
	_sslbedh1024keyexchangesrate= ""
	_timestamp= ""
	_sslbedh512keyexchangesrate= ""
	_sslbedh2048keyexchangesrate= ""
	_sslbersa1024keyexchangesrate= ""
	_device_ip_address= ""
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
			return "perf_ssl_be_rsa_dhkey_report"
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
			return "perf_ssl_be_rsa_dhkey_reports"
		except Exception as e :
			raise e



	'''
	get sslbersa2048keyexchangesrate Value 
	'''
	@property
	def sslbersa2048keyexchangesrate(self) :
		try:
			return self._sslbersa2048keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbersa2048keyexchangesrate Value 
	'''
	@sslbersa2048keyexchangesrate.setter
	def sslbersa2048keyexchangesrate(self,sslbersa2048keyexchangesrate):
		try :
			if not isinstance(sslbersa2048keyexchangesrate,float):
				raise TypeError("sslbersa2048keyexchangesrate must be set to float value")
			self._sslbersa2048keyexchangesrate = sslbersa2048keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbersa512keyexchangesrate Value
	'''
	@property
	def sslbersa512keyexchangesrate(self) :
		try:
			return self._sslbersa512keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbersa512keyexchangesrate Value
	'''
	@sslbersa512keyexchangesrate.setter
	def sslbersa512keyexchangesrate(self,sslbersa512keyexchangesrate):
		try :
			if not isinstance(sslbersa512keyexchangesrate,float):
				raise TypeError("sslbersa512keyexchangesrate must be set to float value")
			self._sslbersa512keyexchangesrate = sslbersa512keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbedh1024keyexchangesrate Value 
	'''
	@property
	def sslbedh1024keyexchangesrate(self) :
		try:
			return self._sslbedh1024keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbedh1024keyexchangesrate Value 
	'''
	@sslbedh1024keyexchangesrate.setter
	def sslbedh1024keyexchangesrate(self,sslbedh1024keyexchangesrate):
		try :
			if not isinstance(sslbedh1024keyexchangesrate,float):
				raise TypeError("sslbedh1024keyexchangesrate must be set to float value")
			self._sslbedh1024keyexchangesrate = sslbedh1024keyexchangesrate
		except Exception as e :
			raise e


	'''
	get timestamp in milliseconds
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set timestamp in milliseconds
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get sslbedh512keyexchangesrate Value 
	'''
	@property
	def sslbedh512keyexchangesrate(self) :
		try:
			return self._sslbedh512keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbedh512keyexchangesrate Value 
	'''
	@sslbedh512keyexchangesrate.setter
	def sslbedh512keyexchangesrate(self,sslbedh512keyexchangesrate):
		try :
			if not isinstance(sslbedh512keyexchangesrate,float):
				raise TypeError("sslbedh512keyexchangesrate must be set to float value")
			self._sslbedh512keyexchangesrate = sslbedh512keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbedh2048keyexchangesrate Value 
	'''
	@property
	def sslbedh2048keyexchangesrate(self) :
		try:
			return self._sslbedh2048keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbedh2048keyexchangesrate Value 
	'''
	@sslbedh2048keyexchangesrate.setter
	def sslbedh2048keyexchangesrate(self,sslbedh2048keyexchangesrate):
		try :
			if not isinstance(sslbedh2048keyexchangesrate,float):
				raise TypeError("sslbedh2048keyexchangesrate must be set to float value")
			self._sslbedh2048keyexchangesrate = sslbedh2048keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbersa1024keyexchangesrate Value 
	'''
	@property
	def sslbersa1024keyexchangesrate(self) :
		try:
			return self._sslbersa1024keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbersa1024keyexchangesrate Value 
	'''
	@sslbersa1024keyexchangesrate.setter
	def sslbersa1024keyexchangesrate(self,sslbersa1024keyexchangesrate):
		try :
			if not isinstance(sslbersa1024keyexchangesrate,float):
				raise TypeError("sslbersa1024keyexchangesrate must be set to float value")
			self._sslbersa1024keyexchangesrate = sslbersa1024keyexchangesrate
		except Exception as e :
			raise e


	'''
	get Device IP Address
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get SSL Back-end RSA and DH Key exchange statistics.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_ssl_be_rsa_dhkey_report_obj=perf_ssl_be_rsa_dhkey_report()
				response = perf_ssl_be_rsa_dhkey_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_ssl_be_rsa_dhkey_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_ssl_be_rsa_dhkey_report_obj = perf_ssl_be_rsa_dhkey_report()
			option_ = options()
			option_._filter=filter_
			return perf_ssl_be_rsa_dhkey_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_ssl_be_rsa_dhkey_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_ssl_be_rsa_dhkey_report_obj = perf_ssl_be_rsa_dhkey_report()
			option_ = options()
			option_._count=True
			response = perf_ssl_be_rsa_dhkey_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_ssl_be_rsa_dhkey_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_ssl_be_rsa_dhkey_report_obj = perf_ssl_be_rsa_dhkey_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_ssl_be_rsa_dhkey_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_ssl_be_rsa_dhkey_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_ssl_be_rsa_dhkey_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_ssl_be_rsa_dhkey_report_responses, response, "perf_ssl_be_rsa_dhkey_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_ssl_be_rsa_dhkey_report_response_array
				i=0
				error = [perf_ssl_be_rsa_dhkey_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_ssl_be_rsa_dhkey_report_response_array
			i=0
			perf_ssl_be_rsa_dhkey_report_objs = [perf_ssl_be_rsa_dhkey_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_ssl_be_rsa_dhkey_report'):
					for props in obj._perf_ssl_be_rsa_dhkey_report:
						result = service.payload_formatter.string_to_bulk_resource(perf_ssl_be_rsa_dhkey_report_response,self.__class__.__name__,props)
						perf_ssl_be_rsa_dhkey_report_objs[i] = result.perf_ssl_be_rsa_dhkey_report
						i=i+1
			return perf_ssl_be_rsa_dhkey_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_ssl_be_rsa_dhkey_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_ssl_be_rsa_dhkey_report_response(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_be_rsa_dhkey_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_ssl_be_rsa_dhkey_report= [ perf_ssl_be_rsa_dhkey_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_ssl_be_rsa_dhkey_report_responses(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_be_rsa_dhkey_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_ssl_be_rsa_dhkey_report_response_array = [ perf_ssl_be_rsa_dhkey_report() for _ in range(length)]
