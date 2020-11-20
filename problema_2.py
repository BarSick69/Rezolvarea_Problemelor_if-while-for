n = int(input())

suma = 0
p = 1       

for i in range(1, n + 1):
    curent = p* i    
    suma += curent
    p = curent

print(suma)