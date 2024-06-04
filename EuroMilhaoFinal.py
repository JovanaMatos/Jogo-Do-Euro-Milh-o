""" 
PI04 - IEFP RANHOLAS / SINTRA
JOVANA MATOS
FORMADOR : CARLOS ALVARES
"""


import random

# Terá alguns nomes de variaveis não adequada ao que se propoe, pois muitas das vezes fiz por bloco ou em dias diferentes. Se achar necessário altero!
 #Porem vou comentando para melhor visualização
Numeros = [0,0,0,0,0]#Lista do sorteio Random
estrela = [0,0] #Lista do sorteio Random
lernumero= [] #Aposta Do usuario
lerestrela = [] #Aposta Do usuario
semana = 0
sortE = 0 #Varivel para receber o Random sorteado da estrela e para comparar
acertosN = 0  #Apenas um contador para saber quantidades de acertos dos Numeros
acertosE = 0  #Apenas um contador para saber quantidades de acertos das Estrelas
verificarN = 0  #Apenas para ler aposta dos Numeros do ultilizador e comparar
verificarE =0 #Apenas para ler aposta das Estrelas do ultilizador e comparar
sort = 0 #Varivel para receber o Random sorteado dos Numeros e para comparar


print ("*** EURO MILHÃO ***")
print ("Para apostar no euro milhão digite 5 numeros e 2 estrelas ")
print ("****EURO MILHÃO NUMEROS ALEATÓRIOS 1 - 50 ****")
while len(lernumero) < 5: # Essa primeira parte será para verificação dos dados para numeros que o usuario digita, criando uma lista de 5 posições
    continuar = True      #Condição para O verificarN não ser inserir na lista é : inserir numeros iguais da lista lernumeros , >50 ou < 0 
    while continuar == True:
        print ("Digite o ",len(lernumero)+1, " numero: ")
        verificarN = int (input())
        if verificarN  in lernumero or verificarN <= 0 or verificarN > 50:
            print ("Numero invalido!\n - Numero deve ser maior que 0\n - Menor ou igual a 50 \n - Não pode ser igual a um já digitado\n Digite novamente!\n")
        else:
            lernumero.append(verificarN)
            continuar = False
      
print ("****EURO MILHÃO ESTRELAS ALEATÓRIAS 1- 12 ****") # Essa a mesma coisa dos numeros porem sendo estrela e apenas 2 posições
while len(lerestrela) < 2:                                #Condição para o verificarE  não ser inserido na lista, numeros iguais da lista lerEstrela  > 12 ou < 0 
    repete = True
    while repete == True:
        print ("Digite o ",len(lerestrela)+1, " numero: ")
        verificarE = int (input())
        if verificarE  in lerestrela or verificarE <= 0 or verificarE > 12:
            print ("Estrela invalida!\n - Estrela deve ser maior que 0\n - Menor ou igual a 12 \n - Não pode ser igual a uma já digitada\n Digite novamente!\n")
        else:
            lerestrela.append(verificarE)
            repete = False

while semana <= 99 : # Até 99 pq o contador começa no zero. Mas é para mim! Ele é para as 100 semanas e nele esta todo o programa irei comentando passo a passo!
    i = 0               #Aqui começa a gerar numeros aleatórios e nele tbm a verificação para não ter numeros iguais
    while i < 5:  #Necessitando para mim 2 while para verificar cada posição
        sort = random.randrange(1,51)   
        y = 0
        TemIgual= "F"     #Criei uma variavel para atribuir caso tenha um numero igual, no momento ele é F
        while y < 5:
            if sort == Numeros[y]: # se tiver igual a variavel TemIgual recebe "V" 
              #print ("no sorteio da possição -",i+1," o numero sorteado:",sort, "foi igual ao numero da posição", y+1) ESSE PRINT ERA UM TESTE, PARA APENAS VERIFICAR SE TINHA REPETIDO E SE  HOUVE SUBSTITUIÇÃO
              TemIgual = "V" # E com isso compara todos os valores até o fim do ciclo 
            y += 1           # levando a posição do while i não muda enquanto ter igual

        if TemIgual == "F": #Aqui o esse if verifica se varivel temigual é F atribui a sort (numero aleatório ) para a posição vazia e o ciclo while i aumenta p vericar a posição seguinte.
            Numeros[i] = sort
            i += 1 

    e = True
    
    while e == True:    #Aqui gerar estrelas e não ser repetidas
        estrela[0] = random.randrange(1,13)
        sortE = random.randrange(1,13)      
        if sortE != estrela[0]:
            estrela[1] = random.randrange(1,13)
            e = False
    
    comparacao = 0

    while comparacao < 5: #Ja aqui será a vericação dos numeros apostados pelo o usuario e os sorteados
        j = 0         # 2 while um verica uma posição por vez e o outro compara todas para depois sair e ir para a posição seguinte
        while j < 5:
            if lernumero[comparacao] == Numeros[j] :
                print ("****APOSTAS NUMEROS****\n")
                lernumero.sort()# Mostrar de forma crescente
                Numeros.sort()# Mostrar de forma crescente
                print ("Acertou na semana ", semana, "\n Aposta Numeros: ", lernumero, "\n Numeros sorteados: ", Numeros)
                print("----------------------------------------------------------------------------------------------------")
                acertosN += 1 # Para contar quantas vezes foi acertado
                comparacao += 5 # Para forçar sai do while comparacao pois só quero saber se acertou uma vez/ Se não ia ficar repetindo a frase e aumentar o contador de acertos, caso na aposta do ultilizador tivesse mais de um acerto
                break           #Forçar sair do while j pelos mesmos motivos do comentario acima
            else:
                j += 1  
        comparacao += 1

    for x in lerestrela:  #Verificação das estrelas 
        if x in estrela:
            estrela.sort()# Mostrar de forma crescente
            lerestrela.sort() # Mostrar de forma crescente
            print ("****APOSTAS ESTRELAS****\n")
            print ("Acertou na semana ", semana, "\n Aposta Estrelas: ", lerestrela, "\n Estrelas sorteadas: ", estrela)
            print("----------------------------------------------------------------------------------------------------")
            acertosE += 1 # Para contar quantas vezes foi acertado
            break #Forçar saida depois de verificar 1 vez/ Mesmo motivo dos numeros
    semana+= 1 
print ("Total de numeros em semanas acertadas: ",acertosN ) # Imprime quantas vezes acertou
print ("Total de estrelas em semanas acertadas: ",acertosE )







