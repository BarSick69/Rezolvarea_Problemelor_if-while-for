from fractions import Fraction
import math
numaratorul_1=int(input("dati numaratorul 1: "))
numar1=numaratorul_1
numitorul_1=int(input("dati numitorul 1: "))
numaratorul_2=int(input("dati numaratorul 2: "))
numar2=numaratorul_2
numitorul_2=int(input("dati numitorul 2: "))
if(numitorul_1!=numitorul_2):
    l=numitorul_2
    n=numitorul_1
    numitorul_1=n*l
    numitorul_2=l*n
    numaratorul_1=l*numaratorul_1
    numaratorul_2=n*numaratorul_2
l=numitorul_2
n=numitorul_1
suma=numaratorul_1+numaratorul_2
s1mple=math.gcd(suma,numitorul_2)
suma=suma//s1mple
numitorul_2=numitorul_2//s1mple
print("Suma: ",Fraction(suma,numitorul_2))
print("Produsul: ",Fraction(numar1*numar2,n*l))
   



