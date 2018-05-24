import sys
import zipfile

def getchar(x):
	if x<26:
		return chr(x+65)
	if x<52:
		return chr(x+71)
	else:
		return chr(x-4)

def get_string(i):
	hehe=''
	while i!=0:
		x = i%62
		i = int(i/62)
		hehe+=getchar(x)
	return str.encode(hehe[::-1])

zip_ref = zipfile.ZipFile('test.zip', 'r')

i = 0
while i!=-1:
	try:
		st = get_string(i)
		print(st)
		zip_ref.extractall(pwd=st)
	except:
		i+=1
	else:
		i=-1

zip_ref.close()

