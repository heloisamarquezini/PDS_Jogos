import random
    
    numeroSecreto = random.randint(1,101)
    tentavias  = 101
    
    
    def jogar():
        
        print("*********************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("*********************************")
        
        NivelDificuldade()
        
        print("numero screto" , numeroecreto)
        global tentativas
        while tentativas >0:
            numeroDigitado = int(
                input(" Digite um número de 1 a 100 para tentar adivinhar o número secreto:"))
            if nuemeroDigitado == numeroSecreto:
                print("Parabéns o numero ecolhido esta correto")
                print("O numero ecreto era" , numeroSecreto)
                break
            else:
                tentativas -= 1        
                print("O número digitado está errado")
                print(dica(numeroDigitado))
                if tentativas > 0;
                   print("Tente novamente, voce tem:" , tentativas, "tentativas")
                else:
                    print("Game Over")
                    
                    
    def dica(numeroEscolhido: int):
        print("Escolhido", numeroEscolhido, "Secreto, numeroSecreto",numeroEscolhido
        if numeroEscolhido>numeroSecreto:
            return "O numero escolhido é Maior que o numero secreto," numeroEscolhido
       else:
           return: "O numero escolhido é Menor que o numero secreto" ,numeroEscolhido
           
           
    def NivelDiiculdade():
        print("Qual o nivel de diiculdade?")
        print("(1)Fácil(2) Médio (3) Díicil)
        dificuldade = int(input("Defina o nível"))
        global tentativas
        if (dificulade ==1):
            tentativas = 10
        elif (difuldade == 2):
            tentativas = 8
        else:
            tentativas = 6
    jogar()
        
