import socket

count = 0
ret=[]
try:
	with open("siteswithresults.txt", "r") as ins:
		for linetot in ins:
			line = linetot.rstrip()
			site = line.split(' ')[0]
			expected = line.split(' ')[1]
			count+=1
			try:
				add1 = socket.gethostbyname(site)

				if add1 not in ret:
					ret.append(add1)

				if add1 == expected:
					print ('Query to ' + site + ' OK: ' + add1)
				elif (add1.split('.')[0] == '192') or (add1.split('.')[0] == '127'):
					#toblock something like 192.x.x.x and 127.x.x.x
					print ('Query to ' + site + ' KO: ' + add1 + ' is in black list')
				elif (add1.split('.')[0] == '10') and (add1.split('.')[1] == '10') and (add1.split('.')[2] == '10'):
					#toblock something like 10.10.10.x
					print ('Query to ' + site + ' KO: ' + add1 + ' is in black list')
				else:
					print ('Query to ' + site + ' not as expected: ' + add1 + ' ** but NOT in black list')
			
			except Exception as e:
				#print (e)
				if expected == 'error':
					print ('Query to ' + site + ' OK: not exist')
				else:
					print ('Query to ' + site + ' not as expected: now not reachable' + add1)
	if len(ret)==1:
		print ('Response is always the same')
	else:
		print ('Multiple responses')
except Exception as e:
	# print ('error: sites.txt not found')
	print(e)



