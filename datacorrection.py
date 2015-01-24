
with open('access.log.1','r+') as f:
    data=f.readlines()
    newlines=[]

    for lines in data:
        if len(lines.split(' ')) == 10:
            newlines.append(lines)
            
        if len(lines.split(' ')) == 11:
            p=lines.split(' ')
            del p[1]
            q= " ".join(p)
            newlines.append(q)

        if len(lines.split(' ')) == 12:
            p=lines.split(' ')
            del p[1]
            del p[1]
            q= " ".join(p)
            newlines.append(q)

        if len(lines.split(' ')) == 13:
            p=lines.split(' ')
            del p[1]
            del p[1]
            del p[1]
            q= " ".join(p)
            newlines.append(q)

        if len(lines.split(' ')) == 14:
            p=lines.split(' ')
            del p[1]
            del p[1]
            del p[1]
            del p[1] 
            q= " ".join(p)
            newlines.append(q)

        if len(lines.split(' ')) == 15:
            p=lines.split(' ')
            del p[1]
            del p[1]
            del p[1]
            del p[1]         
            del p[1]
            q= " ".join(p)
            newlines.append(q)

with open('mainlog', 'w') as f1:
    f1.writelines(newlines)
