count=0;

fo=open("access.log.2","r")
while(count<30):
    if(count<10):
        bing = fo.readlines()
        count+=1
        print bing
        print count

    elif(count>=10 and count<=19):
        yahoo = fo.readlines()
        count+=1
        print count

    elif(count>=20 and count<=29):
        duckgo = fo.readlines()
        count+=1
        print count

print bing
print yahoo
print duckgo

fo.close
