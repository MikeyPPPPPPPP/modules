from cryptography.fernet import Fernet

class polygram:
	def __init__(self, data):
		self.code = data.encode()#this is the string we want to encrypt
		self.key = Fernet(Fernet.generate_key())# this is a random key
		self.imports = ['from cryptography.fernet import Fernet']#thes are the moduals required for this class

	def encrpytS(self):
		"""this will return an encrypted string"""
		return self.key.encrypt(self.code)

	def decryptS(self):
		"""this will return  a decrypted string"""
		return self.key.decrypt(self.encrpytS()).decode()

