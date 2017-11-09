import urllib

testfile = urllib.URLopener()
try:
	testfile.retrieve("http://192.168.56.101/file.gz", "file.gz")
	print("file.gz - HTTP Download OK")
except:
	print("Error in HTTP Download")