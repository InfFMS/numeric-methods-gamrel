import re
with open('data.csv', "r", encoding='utf-8') as f:
    file = f.read()
    parts = re.split(r'[,\n? ]+', file)
    parts=list(filter(None, parts))
parts.pop(0)
parts.pop(0)
count = len(parts)
i=0
I=[]
U=[]
R=[]
while i<count:
    I.append(parts[i])
    U.append(parts[i+1])
    i+=2
count = len(I)
i=0
while i<count:
    x=float(U[i])
    y=float(I[i])
    R.append(x/y)
    i+=1
print(R)