n=eval(input("dati n "))
m=eval(input("dati m "))
while(n%m==0):
    n/=m
if(n==1):
    print("DA")
else:
    print("NU")
