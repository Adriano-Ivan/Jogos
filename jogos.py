import forca
import adivinhacao

print("Que deseja jogar ?")
print("( 1 ) Adivinhação")
print("( 2 ) Forca")
opcao = int(input("Sua opção: "))

if(opcao == 1):
    print("Jogando adivinhação...", end="\n")
    adivinhacao.jogar()
elif(opcao == 2):
    print("Jogando forca...", end="\n")
    forca.jogar()