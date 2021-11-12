import gzip
import sys

class packer:
	def __init__(self, inFile):
		self.fileName = inFile#this gets the filename
		self.imports = ['gzip']#thes are the moduals required for this class

		#this gets the contents of the file
		with open(self.fileName) as filesname:
			self.fileData = filesname.read() 


	def compressMe(self, data):
		"""returns a gzip compressed utf8 string"""
		return gzip.compress(data.encode()).decode('cp437')

	def deCompressMe(self, data):
		"""returns a decompressed string"""
		return gzip.decompress(data.encode('cp437')).decode()



a = packer()
#print(a.fileData)
#print(a.compressMe(a.fileData))
#print(a.deCompressMe(a.compressMe(a.fileData)))
