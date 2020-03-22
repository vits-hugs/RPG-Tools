# o objetivo do programa é poder controlar a inicitiva dos personagens
from fun import menu
import pandas as pd
from random import randint
from operator import itemgetter
menu.fazmenu()
opmenu = int(input('Opção? '))
if opmenu == 1:
    while True:
        try:
         n = int(input('Quantidade de jogadores: '))
        except:
            print('digita numero caraio')
        else:
            break
    char = {}
    grupo = []
    #  fazer função para evitar crash do programa em caso de erro humano
    # Registro do grupo em um dicionario dentro de uma lista
    for d in range(0,n):
         char['nome'] = input('Nome: ')
         try:
           char['vida'] = int(input('vida: '))
         except:
           print('erow')
         char['mod iniciativa'] = int(input('modificador de iniciativa: '))
         grupo.append(char.copy())
         char.clear()
    print('Grupo Registrado!')
    memo = grupo
    print(grupo)
    opmenu = int(input('Opção? '))
per = []
iroll = []
#rodando iniciativa do grupo
if opmenu == 2:
    for i in range(0,n):
        d20 = randint(1,20)
        per.append(d20)
        per.append(d20+grupo[i]['mod iniciativa'])
        per.append(grupo[i]['nome'])
        iroll.append(per.copy())
        per.clear()
    iroll.sort(key=itemgetter(1),reverse=True)
    for contador in range(0,n):
        print('\033[35m-*\033[m'*20)
        print(f'o {iroll[contador][2]} tirou  {iroll[contador][0]}  totalizando {iroll[contador][1]}')
    print('\033[35m-*\033[m' * 20)
    print('-'*30,'\n')
    print('    \033[7:41mCOMBATE INICIANDO!!!!\033[m\n')
    print('-'*30)
    for cmbt in range(0,n):
        print(cmbt,'-',grupo[cmbt]['nome'],'está com',grupo[cmbt]['vida'],'vida')
confirmador = 0
# curando e dando dano
while confirmador < 99:
    echar = int(input('reduzir vida de qual personagem?(dano negativo para curar)'))
    qtdano = int(input('quantida de dano: ')) *-1
    print(grupo[echar]['nome'],'recebeu',qtdano*-1,'de dano')
    grupo[echar]['vida'] += qtdano
    print('agora esta com ',grupo[echar]['vida'],'de vida')
    confirmador= int(input('continuar? ([999] para sair)'))
    memo = grupo
m = pd.DataFrame(memo)
m.to_csv('grupitcho')
















