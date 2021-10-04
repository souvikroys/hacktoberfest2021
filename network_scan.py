print("============================================================="); 
print("\tSimple-CMD\tC0d3d by : Souvik_Roy");  
print("============================================================="); 
print("\t\tEmail : souvik09243@gmail.com");  
print("============================================================="); 

#Modules Required 
#1. Socket 
#2. Sys
#3. Threading

import socket
import sys 
import threading

address=input("Target IP or Domain name: ")
try:
	s=socket.gethostbyname(address)
except:
	print("\n============================================================="); 
	print("Invalid Address")
	print("============================================================="); 
	exit()
	

print("\n============================================================="); 
print("Port Scanning of addr: ",s)
print("============================================================="); 

start_port=int(input("\nEnter Starting Port: "))
end_port=int(input("Enter Ending Port: "))

print("\n============================================================="); 
is_empty=0

def portscan(ports):
	sock=socket.socket()
	try:	
		x=sock.connect((s,ports))
		print("port {}: open".format(ports))
		x.close()
		is_empty=1
	except:
		pass

for ports in range(start_port,end_port+1):

		t=threading.Thread(target=portscan,kwargs={'ports':ports})
		t.start()


if (is_empty==0):
	print("\nNo Ports are opened !")
print("\n=============================================================");
sys.exit()
