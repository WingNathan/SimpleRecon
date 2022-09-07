#Simple Reconissence Express 
#Welcome!

#-----------------------------------------------------------------
import os
import subprocess
import nmap
from time import sleep
nm = nmap.PortScanner()

def LetsNmapScan():
  scan_target = nm.scan(hosts=URL)
  nm.all_hosts()
  sleep(2)
  for host in nm.all_hosts():
			
     print("Host: %s(%s)" % (host, nm[host].hostname()))

     print("Open TCP Ports: ")

     print("%s" % (nm[host].all_tcp()))
     print("---------------------------------------")
     print ("")
     print ("")

     if FTP in ("%s" % (nm[host].all_tcp())):
     	print ("FTP is Open!")
     else:
     	print ("FTP is Closed!")
     if SSH in ("%s" % (nm[host].all_tcp())):
     	print ("SSH is Open!")
     else:
     	print ("SSH is Closed!")
     if HTTP in ("%s" % (nm[host].all_tcp())):
     	print ("HTTP is Open!")
     else:
     	print ("HTTP is Closed!")
     if SMB in ("%s" % (nm[host].all_tcp())):
     	print ("SMB is Open!")
     else:
     	print ("SMB is Closed!")
     if POP3 in ("%s" % (nm[host].all_tcp())):
     	print ("POP3 is Open!")
     else:
     	print ("POP3 is Closed!")
     if TELNET in ("%s" % (nm[host].all_tcp())):
     	print ("TELNET is Open!")
     else:
     	print ("TELNET is Closed!")
     	print ("")
     	print ("")
     	print("---------------------------------------")
     	sleep(5)
  return()
  
def LetsBustThoseDirectorys():

	process = subprocess.Popen(['gobuster', 'dir', '-u', URL, '-w', WORDLIST, '-x', 'php,txt,old,html'], 
                 stdout=subprocess.PIPE,
                           universal_newlines=True)

	while True:
	    output = process.stdout.readline()
	    print(output.strip())
	    # Do something else
	    return_code = process.poll()
	    if return_code is not None:
	        print('RETURN CODE', return_code)
	        # Process has finished, read rest of the output 
	        for output in process.stdout.readlines():
	            print(output.strip())
	        break             
                        
	return()
	
	
def WPSScan():

	process = subprocess.Popen(['wpscan', '--url', URL], 
                 stdout=subprocess.PIPE,
                           universal_newlines=True)

	while True:
	    output = process.stdout.readline()
	    print(output.strip())
	    # Do something else
	    return_code = process.poll()
	    if return_code is not None:
	        print('RETURN CODE', return_code)
	        # Process has finished, read rest of the output 
	        for output in process.stdout.readlines():
	            print(output.strip())
	        break             
                        
	return()



#---------------------------------------------------------------------


#--------------- Variables --------------------------
URL = input("Enter URL of Target for Recon:   ")
WORDLIST = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
FTP = "21" or "20"
HTTP = "80"
SSH = "22"
SMB = "139" or "445"
POP3 = "110"
TELNET = "23"
#--------------------------------------------------------------------
# LETS SCAN
sleep(3)
print ("Nmap is now running! Please be patient... you will get your ports soon")
print ("")
print ("")
print ("")
print ("")
LetsNmapScan()		
print ("")
print ("")
print ("")
print ("")
print ("Well there you go.. Happy now. Anyway lets get you those Directorys")
print ("")
print ("")
print ("")
print ("")
LetsBustThoseDirectorys()
print ("")
print ("")
print ("")
print ("Nice, Maybe Wordpress is there.. No? lets WPScan anyway")
print ("")
print ("")
WPSScan()
