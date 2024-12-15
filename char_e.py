mess=input()
ott=0
count=[]
for pos,char in enumerate(mess):
    if char=='e':
        count.append(pos)
ott=count[3:]
print(ott)
del ott
print(mess)