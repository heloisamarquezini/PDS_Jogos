import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    
    print("(1) Forca(2) Adivinhação")
    
    jogo = int(input("Qual jogo?"))
    
    if(jogo == 1):
        print("Jogando forca")
        froca.jogar()
    elif(jogo == 2):
        print(" Jogando adivinhação")
        adivinhacao.jogar()
        
if(_name_)  == "_main_" :
    escolhe_jogo()
        
        