cifra=int(input("Introduceti cifra care doriti sa fie codificata in 8421 :")) #Citim cifra
copie=cifra # Facem o copie cifrei initiale
cod=[0,0,0,0]  # Initializam vectorul cu 0 , care va stoca cei 4 biti si in final va reprezenta numarul nostru codificat
if cifra>9 or cifra<0: #Verificam daca s-a introdus o cifra valida
    print("Cifra introdusa nu este valida")
    exit()
'''
Mai departe , impartim cifra succesiv la 2 si retinem resturile 
de la ultimul la primul , de aceea am parcurs for-ul invers.
'''
for i in range(3,-1,-1):
    cod[i]=cifra%2
    cifra=cifra//2
'''
In final , in vectorul cod , vom avea reprezentarea in 8421 a cifrei noastre 
si afisam fiecare cifra din vectorul.
'''
print("Codificare in 8421 a cifrei " + str(copie) + " este: " )
for i in cod:
    print(i)
