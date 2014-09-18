from sys import argv
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
a=0



while a < num_lines:

	
	p=log.readlines()[a]
	sentence=break_words(p)




	q=pop_first_word(sentence)
	time=[]
	time.append(q)
	print "Array of Time", time





	r=pop_word(sentence)
	duration=[]
	duration.append(r)
	print "array of Duration", duration



	s=pop_word(sentence)
	remotehost=[]
	remotehost.append(s)
	print "array of remotehost", remotehost



	t=pop_word(sentence)
	code_status=[]
	code_status.append(t)
	print "array of code_status", code_status




	u=pop_word(sentence)
	bytes=[]
	bytes.append(u)
	print "array of Page Size in bytes", bytes



	v=pop_word(sentence)
	method=[]
	method.append(v)
	print "array of Request method", method




	w=pop_word(sentence)
	url=[]
	url.append(w)
	print "array of URL", url



	x=pop_se_word(sentence)
	hierarchy=[]
	hierarchy.append(x)
	print "array of Hierarchy code", hierarchy




	y=pop_se_word(sentence)
	type=[]
	type.append(y)
	print "array of Type", type
	
	
	a = a + 1
