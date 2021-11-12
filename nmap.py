#ipconfig getifaddr en0    get just my local ip for mac
#hostname -I               get just my local ip for linux
import subprocess
import time

HOST_AND_HOSTNAME = {}
HOST_AND_MAC = {}
CURRENT_IP = ""
GATWAY = ""

def get_local_ip():
    global CURRENT_IP
    global GATWAY
    out = subprocess.Popen(['ipconfig','getifaddr','en0'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    CURRENT_IP = str(stdout.decode()).strip()
    GATWAY = CURRENT_IP[:-1]+"1"





def get_nmap_ping_scan():
    get_local_ip()
    host = CURRENT_IP[:-1]+str(1)+'/24'
    global HOST_AND_HOSTNAME
    hosts = []
    batcmd="nmap -T5 -sn "+host+"  | grep 'Nmap'"
    interfaces = []#this will hold the interfaces found
    out = subprocess.Popen(batcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(.5)
    stdout,stderr = out.communicate()# gets output and errors
    for x in stdout.decode().split('\n'):#loops through each line of the decoded output
      if "Nmap" in x:
        hosts.append(host)
        try:
            #print(x.split('for ')[1])
            parser = x.split('for ')[1]
            if '(' in parser:# if it has a hostname
                HOST_AND_HOSTNAME[parser.split(' (')[0]]=parser.split(' (')[1][:-1]#adds {hostname:ip}
            else:
                HOST_AND_HOSTNAME['no host name']=parser#if no hostname give it a value of not host name
        except:
            pass


def get_mac(ip):
    batcmd="arp -n "+ip
    mac = []#this will hold the interfaces found
    out = subprocess.Popen(batcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    mac = [x for x in stdout.decode().split(' ') if ':' in x]#list comprehention to make a list of macs
    HOST_AND_MAC[ip]=mac




#get_mac('192.168.86.37')