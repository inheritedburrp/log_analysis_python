from sys import argv
import logging
import logging.handlers

script, filename=argv

def break_words(stuff):         
	words = stuff.split(' ')
	return words

def pop_first_word(words):
	word = words.pop(0)
	return word

def pop_word(words):
	word = words.pop(4)
	return word
	
def pop_se_word(words):
	word = words.pop(5)
	return word

log= open(filename)
num_lines = sum(1 for lines in log)
log.seek(0)
time=[]
duration=[]
remotehost=[]
code_status=[]
bytes=[]
method=[]
url=[]
hierarchy=[]
types=[]


lines=log.readlines()

for p in lines:

	
	
	sentence=break_words(p)




	q=pop_first_word(sentence)
	time.append(q)
	





	r=pop_word(sentence)
	duration.append(r)
	



	s=pop_word(sentence)
	remotehost.append(s)
	



	t=pop_word(sentence)
	code_status.append(t)
	




	u=pop_word(sentence)
	bytes.append(u)
	


	v=pop_word(sentence)
	method.append(v)
	


	w=pop_word(sentence)
	url.append(w)



	x=pop_se_word(sentence)
	hierarchy.append(x)




	y=pop_se_word(sentence)
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
