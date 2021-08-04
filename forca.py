import random

def jogar():

    apresentar_titulo()

    palavra_secreta = extrai_palavra()

    letras_acertadas = inicializa_posicoes_da_lista(palavra_secreta)

    enforcou = False
    acertou = False
    n_erros = 0

    #print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_e_retorna_chute()

        if(chute in palavra_secreta ):
            letras_acertadas = grava_chute_correto(chute, letras_acertadas, n_erros, palavra_secreta)
        else:
            n_erros += 1
            desenha_forca(n_erros)
            print(f'A letra "{chute}" não está na palavra secreta. Você ainda tem {6 - n_erros} tentativas')

        enforcou = n_erros == 7

        acertou = "_" not in letras_acertadas

        print(f'{letras_acertadas}'.replace("[", "").replace("]", "").replace(",", " "))

        if(enforcou or acertou):
            indica_vitoria_ou_perda(acertou, enforcou, palavra_secreta)

def extrai_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    print(palavras)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    return palavra_secreta

def apresentar_titulo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def inicializa_posicoes_da_lista(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_e_retorna_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def grava_chute_correto(chute, letras_acertadas, n_erros, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

    print(f'A letra "{chute}" está na palavra secreta. Você ainda tem {6 - n_erros} tentativas')

    return letras_acertadas

def indica_vitoria_ou_perda(acertou, enforcou, palavra_secreta):
    if (acertou):
        print("Parabéns, você ganhou !")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    if (enforcou):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()

