cifra=int(input("Introduceti cifra care doriti sa fie codificata in 8421 :"))
cod=[0,0,0,0]
for i in range(3,-1,-1):
    cod[i]=cifra%2
    cifra=cifra//2
print("Codificare in 8421 : ")
for i in cod:
    print(i)
