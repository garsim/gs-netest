import socket
import sys

try:
	addr1 = socket.gethostbyname('google.com')
	#addr2 = socket.gethostbyname('yahoo.com')

	print('Query to google.com: ' + addr1)
	#print ('yahoo.com ' + addr2)
except:
	print ('google.com ' + ': Error in query')


#site = sys.argv[1]

#print(site)
#print("so...")

#addr3 = socket.gethostbyname(site)

#print(addr3)

