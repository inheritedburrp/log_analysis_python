from sys import argv

script, filename=argv

def break_words(stuff):         
	words = stuff.split()
	return words


f=open(filename)
num_lines = sum(1 for lines in f)
f.seek(0)


time=[]
duration=[]
remotehost=[]
code_status=[]
bytes=[]
method=[]
url=[]
hierarchy=[]
types=[]



for p in f:
	sentence=break_words(p)
	
	q=sentence[0]
	time.append(q)
	

	r=sentence[1]
	duration.append(r)
	


	s=sentence[2]
	remotehost.append(s)
	


	t=sentence[3]
	code_status.append(t)
	
	
	u=sentence[4]
	bytes.append(u)
	
	

	v=sentence[5]
	method.append(v)
	


	w=sentence[6]
	url.append(w)



	x=sentence[7]
	hierarchy.append(x)


	
	y=sentence[8]
	types.append(y)
	
	
print time
print duration
print remotehost
print code_status
print bytes
print method
print url
print hierarchy
print types
