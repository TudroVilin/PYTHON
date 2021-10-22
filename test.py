print("Calculador números narcisistas.")
print(" ")
print("Introduzca un número:")
n=input()
l=len(n)
s=0
for i in range(l):
    c=n[i]
    c=int(c)
    s=s+(c**l)
if(s==int(n)):
    print("El número es narcisista.")
    print(" ")
else:
    print("El número no es narcisista.")
    print(" ")