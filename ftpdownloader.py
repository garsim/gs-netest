from ftplib import FTP

def f(s):
    #save the chuck of data in s
    print s

port=21
ip="ftp.indirizzo.it"
password = "a@a.a"
user = "utente"

ftp = FTP(ip)
ftp.login(user,password)

nameOfFile = "example.exe";

ftp.cwd("/extras")

#files = ftp.nlst()

#for i,v in enumerate(files,1):
#    print i,"->",v

try:
	ftp.retrbinary("RETR " + nameOfFile, open(nameOfFile, 'wb').write)
	print (nameOfFile + " - FTP Download OK")
	#ftp.retrbinary("RETR " + nameOfFile,f) 
	##for printing and not save file
except:
	print "Error download from ftp"