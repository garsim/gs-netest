import ftplib 

ftp = ftplib.FTP('myserver.com','login','password') 
fp = open('file.txt','rb') 
ftp.cwd('directory')


try:
	ftp.storbinary('STOR file.txt', fp) # Invia il file
	print("FTP Upload OK")
except:
	print "Error in FTP upload" 
fp.close() # Chiude lo stream del file
ftp.quit() # Chiude la connessione
