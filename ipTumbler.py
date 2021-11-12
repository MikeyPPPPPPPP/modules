import requests
import subprocess
import time

class Tumbler:
	IS_RUNNING = False
	IP = ''

	def start(self):
		out = subprocess.Popen(['tor > /dev/null 2>&1'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		IS_RUNNING = True

	def stop(self):
		for x in range(1,4):
			processToKill = ''
			out = subprocess.Popen(['ps | grep "tor"'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			stdout,stderr = out.communicate()
			for x in stdout.decode().split('\\n'):#loops through each line of the decoded output
				if "tor\n" in x:
					processToKill = x.split(" ")[0]
			subprocess.Popen([str('kill -9 '+processToKill)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			IS_RUNNING = False

	def changeMe(self):
		self.stop()
		time.sleep(2)
		self.start()

	def getIp(self):
		session = requests.session()
		session.proxies = {}
		session.proxies['http'] = 'socks5h://127.0.0.1:9050'
		session.proxies['https'] = 'socks5h://127.0.0.1:9050'
		IP = session.get('https://ident.me').text


