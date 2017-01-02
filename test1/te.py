'''
d="1,2,3"
d=d.replace(',','')
l=len(d)
a=[0,0,0]
b=[4.0,5.0,6.0]
for item in range(l):
    print float(d[item])
    a[item]=float(d[item])

def add(m,n):
    sum1=[0,0,0]
    l=len(m)
    for item in range(l):
        sum1[item]=m[item]+n[item]
    print sum1

def multiply(m,n):
    sum1=0
    l=len(m)
    for item in range(l):
        sum1=m[item]*n[item]+sum1
    print sum1
map(multiply,a,b)
'''
a=[1.0,2.0,3.0]
b=[4.0,5.0,6.0]
c=map(lambda x,y:x+y,a,b)
print c
d=map(lambda x,y:x*y,a,b)
sum1=0
for item in range(len(c)):
    sum1=d[item]+sum1
print sum1