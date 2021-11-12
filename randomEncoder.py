import base64
import random

class encoderGenrator:
	def __init__(self, text):
		self.text = text
		self.code = {}
		self.alpha = ['\t','\n',' ','!', '~', '`', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '-', '+', '{', '}', '|', '\\', '}', '{', '[', ']', ':', ';', '"', "'", ',', '.', '/', '?', '>', '<', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'U', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#'abcdefghijklmnopqurstuvwxyz'#add all charector here later
		self.genrateKeys()
		self.encodeedText = ''

	def genrateKeys(self):
		for x in self.alpha:
			self.randomCherector = self.alpha[random.randint(0,len(self.alpha)-1)]
			while True:
				if self.randomCherector not in [t[0] for t in self.code.values()]:#keys
					self.code[x]=self.randomCherector
					break
				else:
					self.randomCherector = self.alpha[random.randint(0,len(self.alpha)-1)]

	def bEncode(self):
		self.disHolder = []
		for x in self.text:
			self.disHolder.append(self.code[x])
		self.encodeedText = (base64.b64encode(''.join(self.disHolder).encode('ascii'))).decode('ascii')
		return (base64.b64encode(''.join(self.disHolder).encode('ascii'))).decode('ascii')


	def codeGenrator(self):
		print('import base64')
		print('code = '+str(self.code))
		print('eText = \''+self.encodeedText+'\'.encode(\'ascii\')')
		print('eBase = base64.b64decode(eText).decode(\'ascii\')')
		print('enm = []')
		print('enm[::1] = eBase')
		print('c = []')
		print('c[::1] = [[x[0], x[1]] for x in code.items()]')
		print('full = [y[0] for x in enm for y in c if x == y[1]]')
		print('print(\'\'.join(full))')
