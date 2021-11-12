
import requests
class roku:
	def __init__(self, ip):
		self.ip = ip
		self.url = ''
		self.headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}

	def build_url(self,text):
		self.url = 'http://'+self.ip+':8060/keypress/'+text

	def power(self):
		self.build_url('Power')
		response = requests.post(self.url, headers=self.headers)

	def rev(self):
		self.build_url('Rev')
		response = requests.post(self.url, headers=self.headers)
	def fwd(self):
		self.build_url('Fwd')
		response = requests.post(self.url, headers=self.headers)

	def info(self):
		self.build_url('Info')
		response = requests.post(self.url, headers=self.headers)
	def replay(self):
		self.build_url('InstantReplay')
		response = requests.post(self.url, headers=self.headers)
	def home(self):
		self.build_url('Home')
		response = requests.post(self.url, headers=self.headers)
