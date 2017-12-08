import urllib

testfile = urllib.URLopener()
try:
	testfile.retrieve("http://www.testsite.com/file.gz", "file.gz")
	print("file.gz - HTTP Download OK")
except:
	print("Error in HTTP Download")
