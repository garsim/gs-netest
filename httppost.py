import requests

try:
	r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
	print(r.status_code, r.reason)
	print(r.text[:300] + '...')
except:
	print('Error in HTTPPost')