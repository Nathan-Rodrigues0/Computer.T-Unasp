loading = 1

while loading:
    if loading <= 30:
        print(chr(9608) * loading)#strings são multiplicados
        loading+=1
        
    else:
        print("Salvamento concluído")
        break

print("Carregando, Aguarde.....")
carregando = (chr(9608))
loading2 = 1

while loading2 <= 10:
    print(carregando * loading2)
    loading2 += 1

#resolução
from time import sleep
import os

print("\033[?25l]")#o cursor no terminal desaparece

loading = 1

while loading: #barra aumentando verticaclmente
    if loading <= 30:
        print(chr(9608) + " " + str(loading) + "%")#strings são multiplicados
        loading+=1
        sleep(0.2)#
        os.system("cls")#metodo importado para codificar o terminal (cls) apagando o terminal a um determinado loop
        #horinzotalmente adiciona os.sytem 
    else:
        print("Salvamento concluído")
        break
    