from ftplib import FTP

def f(s):
    #save the chuck of data in s
    print s

port=21
ip="ftp.indirizzo.it"

ftp = FTP(ip)
ftp.login() #user anonymous, passwd anonymous

nameOfFile = "example.exe";

ftp.cwd("/extras")

#files = ftp.nlst()

#for i,v in enumerate(files,1):
#    print i,"->",v

try:
	ftp.retrbinary("RETR " + nameOfFile, open(nameOfFile, 'wb').write)
	print (nameOfFile + " - FTP Download *as Anonymous* OK")
	#ftp.retrbinary("RETR " + nameOfFile,f) 
	##for printing and not save file
except:
	print "Error download from ftp *as Anonymous*"