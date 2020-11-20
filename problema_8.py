a = int(input(" "))
b = int(input(" "))
c = int(input(" "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if ((a == b) and (a != c)) or ((a == c) and (a != c)) or ((b == c) and (b != a)):
        print("Numerele alcatuiesc un triunghi isoscel")
    elif (a == b) and (a == c):
        print("Numerele alcatuiesc un triunghi echilateral")
    else:
        print("Numerele alcatuiesc un triunghi scalen")
else:
    print("Numerele nu alcatuiesc un triunghi")
