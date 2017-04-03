#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:50:46 2017

@author: Sabrina
"""
import sys,time
import random as rdm
import json

with open('pokedex1.json') as arquivo: 
    pokedex1 = json.load(arquivo)


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

print('\nVoce comeca com o pokemon {0}!! \nEle é do tipo {1} e tem:\n{2} pontos de vida;\n{3} de poder de ataque;\n{4} de defesa;\n{5} de ataque especial;\n{6} de defesa especial;\n{7} de velocidade!'.format(suapokedex[0]['nome'],suapokedex[0]['tipo'],suapokedex[0]['PS'],suapokedex[0]['ataque'],suapokedex[0]['defesa'],suapokedex[0]['ataque especial'],suapokedex[0]['defesa especial'],suapokedex[0]['velocidade']))


def suafuncaobatalha(suavida,caraataque,suadefesa):
    suavida = suavida - (caraataque - suadefesa)
    return suavida



def carafuncaobatalha(caravida,seuataque,caradefesa):
    caravida = caravida - (seuataque - caradefesa)
    return caravida


for i in range(len(suapokedex)):
    print("Você tem os seguintes pokemons: {0}".format(suapokedex[i]['nome']))

posicaodopokemon = 0
pp = posicaodopokemon
pp = input('Qual pokemon você gostaria de utilizar??')



x = 0
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        

#Lopping infinito
while x == 0:
    opcao = input('Você deseja:\n(1)Passear;\n(2)Dormir??\n')
    if opcao == '1' or opcao == 'passear':
        print_slow("Você está passeando.....\n")
        print("Você encontrou um inimigo!!")
        inimigo = rdm.randint(0,6)
        print(pokedex1[inimigo]['nome'])
        suavida = int(suapokedex[pp]['PS'])
        seuataque = int(suapokedex[pp]['ataque'])
        suadefesa = int(suapokedex[pp]['defesa'])
        vidainimigo = int(pokedex1[inimigo]['PS'])
        ataqueinimigo = int(pokedex1[inimigo]['ataque'])
        defesainimigo = int(pokedex1[inimigo]['defesa'])
        Batalhar = input("Você deseja:\n(1)Batalhar;\n(2)Correr??")
        while Batalhar == "1" and suavida>0 and vidainimigo>0:
                suavida = suafuncaobatalha(suavida,ataqueinimigo,suadefesa)
                vidainimigo = carafuncaobatalha(vidainimigo,seuataque,defesainimigo)
                print("Agora, sua nova vida é:{}".format(suavida))
                print("Agora, a nova vida do seu inimigo é:{}".format(vidainimigo))
                Batalhar = input("Você deseja continuar batalhando ou quer fugir??")
    elif opcao == '2' or opcao == 'dormir':
        print('Boa noite!!')
        x = 1
    else:
        print("Ei!! Você só tem essas duas opções!!")
