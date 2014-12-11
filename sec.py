from sys import argv
import datetime

script, filename=argv

def break_words(stuff):         
	words = stuff.split()
	return words
	
def utc2local(utc):
	temp = datetime.datetime.fromtimestamp(utc).strftime('%Y-%m-%d %H:%M:%S')
	return temp

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
	
	if len(sentence)==10:
	
		q_utc=sentence[0]
		q=utc2local(float(q_utc))
		time.append(q)
		
	
		r=sentence[1]
		duration.append(r)
		
	
	
		s=sentence[2]
		remotehost.append(s)

