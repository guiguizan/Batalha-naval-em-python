from random import seed
from random import randint
seed(1)

print('░░░░░░      BOMBERMAN ON FIRE      ░░░░░░')
print('░░░░░░░         BEM - VINDO       ░░░░░░░')

n = int(input('Primeiramente, escolha o tamanho de seu mapa:  ')) #tamanho da matriz



matriz = []



def criaMapa(x):    #CRIA O MAPA
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(randint(0, 1000))

criaMapa(n)


aux=0
for a in range(len(matriz)):
    print(matriz[aux])
    aux+=1

print('*  MAPA DA RODADA  *')
print('')



m = int(input('Agora, qual será o alcance de sua explosão para baixo,cima e lados:  '))  #ALCANCE DA BOMBA
posi= int(input('Muito bem, nos diga a linha horizontal da bomba:  '))
posi2= int(input('Agora diga a linha vertical da bomba:  '))
print('')
casas= []
pontos=0

print('☼☼☼☼☼ CASAS ATINGIDAS ☼☼☼☼☼')
cont=0
for i in range(m+1):                            ##### EXPLOSAO DE CIMA + primeiro num
    explosaoCima = posi - cont
    if explosaoCima>=0 and explosaoCima <=n:
        casas.append(matriz[explosaoCima][posi2])
        pontos = pontos + (matriz[explosaoCima][posi2])
    cont+=1



cont2=1
for i in range(m):                            #####explosao de BAIXO
    explosaoBaixo = posi + cont2
    if explosaoBaixo>=0 and explosaoBaixo <n:
        casas.append(matriz[explosaoBaixo][posi2])
        pontos = pontos + (matriz[explosaoBaixo][posi2])

    cont2+=1


cont3=1
for i in range(m):                               #####explosao ESQUERDA
    explosaoEsquerda = posi2 - cont3
    if explosaoEsquerda>=0 and explosaoEsquerda <n:
        casas.append(matriz[posi][explosaoEsquerda])
        pontos = pontos + (matriz[posi][explosaoEsquerda])
    cont3+=1



cont4=1
for i in range(m):                               #####explosao Direita
    explosaoDireita = posi2 + cont4
    if explosaoDireita>=0 and explosaoDireita <n:
        casas.append(matriz[posi][explosaoDireita])
        pontos = pontos + (matriz[posi][explosaoDireita])
    cont4+=1

print(casas)
print(' ')
print('Sua pontuação: ',pontos)



