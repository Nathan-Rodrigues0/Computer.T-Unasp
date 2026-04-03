from time import sleep
import os

print("\033[?25l]")#o cursor no terminal desaparece

loading = 1

while loading: #barra aumentando verticaclmente
    if loading <= 30:
        print(chr(9608) + " " + str(loading) + "%")#strings são multiplicados
        loading+=1
        sleep(0.2)#
        #os.system("cls")#metodo importado para codificar o terminal (cls) apagando o terminal a um determinado loop
        #horinzotalmente adiciona os.sytem 
    else:
        print("Salvamento concluído")
        break

print(os.get_terminal_size())#ver o tamanho do terminal (quantidade de colunas e linhas)