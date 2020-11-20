suma2=0
v=0
produs=1
suma=1
varsta=int(input("dati varsta: "))
if(varsta<=20):
 for i in range(1,varsta+1):
    suma=suma*2+i

 while(suma2<100):
        v+=1
        suma2=suma2*2+v
    
    
 print(suma)
 print("primeste mai mult de 100 dolari la ",v," ani")