da=0
suma=0
patrat=0
produs=0
s2=0
s1=0
n = int(input(""))
for i in range(0,n+1):
    i=i**3
    s1+=i
for l in range(0,n+1):
    s2+=l
    
produs=s2**2    
if(s1>produs):
    print("s1>s2")
elif(produs>s1):
    print("s2>s1")
elif(s1==produs):
    print("s1=s2")
#b
for h in range(0,n+1):
    patrat=h**2
    suma+=patrat
    produs=0
produs=3*suma
suma=0
for h in range(0,n+1):
    suma+=h
da=n**3+n**2+(suma)
if(produs>da):
    print("s2>s1")
elif(produs<da):
    print("s1>s2")
elif(da==produs):
    print("s2=s1")
