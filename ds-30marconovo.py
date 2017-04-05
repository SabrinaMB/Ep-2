#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:56:12 2017

@author: RebecaMoreno
"""

import sys,time
import random as rdm
import json

with open('pokedex1.json') as arquivo: 
    pokedex1 = json.load(arquivo)

def print_slow(str):
     for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

suapokedex = [
        {
        "nome" : "Pancham",
        "tipo" : "Lutador",
        "PS" : 12,
        "ataque" : 4,
        "defesa" : 3,
        "ataque especial" : 2,
        "defesa especial" : 2,
        "velocidade" : 2
        }
]

#if len(suapokedex) == 1:
print_slow('\nVoce comeca com o pokemon {0}!! \nEle é do tipo {1} e tem:\n{2} pontos de vida;\n{3} de poder de ataque;\n{4} de defesa;\n{5} de ataque especial;\n{6} de defesa especial;\n{7} de velocidade!'.format(suapokedex[0]['nome'],suapokedex[0]['tipo'],suapokedex[0]['PS'],suapokedex[0]['ataque'],suapokedex[0]['defesa'],suapokedex[0]['ataque especial'],suapokedex[0]['defesa especial'],suapokedex[0]['velocidade']))


def suafuncaobatalha(suavida,caraataque,suadefesa):
    suavida = suavida - (caraataque - suadefesa)
    return suavida



def carafuncaobatalha(caravida,seuataque,caradefesa):
    caravida = caravida - (seuataque - caradefesa)
    return caravida

posicaodopokemon = 0
pp = posicaodopokemon

if pp == 1:
    pp = pp - 1

k = 20
xp = 0 
x = 0
#Lopping infinito
while x == 0:
   opcao = input('Você deseja:\n(1)Passear;\n(2)Dormir?')
   if opcao == '1':
       print_slow("Você está passeando.....\n")
       print_slow("Você encontrou um inimigo!!")
       inimigo = rdm.randint(0,6)
       #print_slow("E o nome dele eh.....{}".format(pokedex1[inimigo]['nome']))
       suavida = int(suapokedex[pp]['PS'])
       seuataque = int(suapokedex[pp]['ataque'])
       suadefesa = int(suapokedex[pp]['defesa'])
       vidainimigo = int(pokedex1[inimigo]['PS'])
       ataqueinimigo = int(pokedex1[inimigo]['ataque'])
       defesainimigo = int(pokedex1[inimigo]['defesa'])
       print_slow("E o nome dele eh.....{0}\nEle é do tipo {1} e tem:\n{2} pontos de vida;\n{3} de poder de ataque;\n{4} de defesa;\n{5} de ataque especial;\n{6} de defesa especial;\n{7} de velocidade!".format(pokedex1[inimigo]['nome'],pokedex1[inimigo]['tipo'],pokedex1[inimigo]['PS'],pokedex1[inimigo]['ataque'],pokedex1[inimigo]['defesa'],pokedex1[inimigo]['ataque especial'],pokedex1[inimigo]['defesa especial'],pokedex1[inimigo]['velocidade']))
       Batalhar = input("Você deseja:\n(1)Batalhar;\n(2)Correr?")
       while Batalhar == "1" and suavida>0 and vidainimigo>0:
           suavida = suafuncaobatalha(suavida,ataqueinimigo,suadefesa)
           vidainimigo = carafuncaobatalha(vidainimigo,seuataque,defesainimigo)
           print_slow("Agora, sua nova vida é:{}".format(suavida))
           print_slow("Agora, a nova vida do seu inimigo é:{}".format(vidainimigo))
                 
           if vidainimigo<=0:
               print_slow('Parabens!! Voce venceu!!\n Por isso voce ganhou {0} XPs'.format(k))
               xp += k
               suapokedex.append(pokedex1[inimigo])
               print_slow("Agora, o pokemon {0} foi adicionado a sua pokedex!!".format(pokedex1[inimigo]['nome']))
               print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
               
           if suavida <= 0:
                print_slow("Desculpe... Você perdeu...")
                print_slow("Mas pelo menos, a vida de seu pokemon foi restaurada!")
           elif suavida>0 and vidainimigo>0:
                Batalhar = input("Você deseja:\n(1)Continuar batalhando;\n(2)Fugir??")
                 

   #if opcao == '3' or opcao == 'treinar':
   #    print('Vamos para o FabLab!\n')
  #     print_slow("Chegando.....\n")
 #      print('Chegamos!!\n')
       
       
   elif opcao == '2' or opcao == 'dormir':
       print_slow('Boa noite!                       ')
       dorminhoco = input('Quer acordar?\n(1)Sim\n(2)Nao')
       if dorminhoco == 1:
           x = 0
       else:
           print_slow('Xau xau')
           break 
           x != 0
   elif (opcao!='2' and opcao!='1') or (Batalhar != '1'and Batalhar != '2'):
       print("Ei!! Você só tem essas duas opções!!") 
       
print(suapokedex)