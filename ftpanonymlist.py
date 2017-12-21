from ftplib import FTP

ip="ftp.indirizzo.it"

ftp = FTP(ip)
ftp.login() #user anonymous, passwd anonymous

try:
	files = ftp.nlst()
	print('FTP List:')
	for i,v in enumerate(files,1):
	    print i,"->",v
except:
	print "Error FTP List"