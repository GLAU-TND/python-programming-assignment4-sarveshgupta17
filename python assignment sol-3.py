l=eval(input())
s=input()
m=len(s)
sp=[]
st=''

for i in l:
    if len(i) > m:
       for j in range(m):
          st+=i[j]
       if s==st:
          sp.append(i)
          st=''
       else:
           st=''
print(sp)