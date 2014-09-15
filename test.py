from sys import argv
script, filename=argv

def break_words(stuff):         
	words = stuff.split(' ')
	return words

def pop_first_word(words):
	word = words.pop(0)
	dec = word.split('.')
	time=dec[0]
	duration=dec[1]
	return time, duration

def pop_sec_word(words):
	word = words.pop(5)
	return word

def pop_third_word(words):
	word = words.pop(6)
	return word

def pop_fourth_word(words):
	word = words.pop(7)
	return word

def pop_fifth_word(words):
	word = words.pop(8)
	return word

def pop_sixth_word(words):
	word = words.pop(9)
	return word
def pop_seventh_word(words):
	word = words.pop(10)
	return word

def pop_eighth_word(words):
	word = words.pop(11)
	return word

def pop_ninth_word(words):
	word = words.pop(12)
	return word

def pop_tenth_word(words):
	word = words.pop(13)
	return word


log= open(filename)
num_lines = sum(1 for lines in log)
log.seek(0)
p=log.readlines()[0]
sentence=break_words(p)
print sentence




q,r=pop_first_word(sentence)
time=[]
duration=[]
time.append(q)
duration.append(r)
print "Array of Time", time
print "Array of Duration", duration


'''


r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration



s=pop_sec_word(sentence)
remotehost=[]
duration.append(s)
print "array of remotehost", remotehost

'''
'''
r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration




r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration




r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration





r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration




r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration




r=pop_sec_word(sentence)
duration=[]
duration.append(r)
print "array of Duration", duration  '''
