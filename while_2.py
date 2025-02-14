# input
h=int(input("Digite el valor de la altura inicial: "))

# processing 
q=h/5
n=0
while h>=q:
    h=h-0.1*h
    n=n+1

print("La cantidad de rebotes fue: "+str(n))


