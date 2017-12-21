from ftplib import FTP

port=21
ip="ftp.indirizzo.it"
password = "a@a.a"
user = "utente"

ftp = FTP(ip)
ftp.login() #user anonymous, passwd anonymous

try:
	files = ftp.nlst()
	print('FTP List:')
	for i,v in enumerate(files,1):
	    print i,"->",v
except:
	print "Error FTP List"