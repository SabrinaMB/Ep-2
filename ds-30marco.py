#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:56:12 2017

@author: RebecaMoreno
"""

import random as rdm
import json

#Abrir o arquivo

with open('pokedex1.json',"r") as arquivo: 
    pokedex1 = json.load(arquivo)
#criando a pokedex do usuario
suapokedex = [	
        {
		"nome" : "Pancham",
        "tipo" : "Lutador",
		"PS" : 3,
		"ataque" : 4,
		"defesa" : 3,
		"ataque especial" : 2,
		"defesa especial" : 2,
		"velocidade" : 2
	    }
]

#cada ps sao 3 vidinhas .:. neste caso, aq de cima, ele tem 9 vidas :D

#mostrando o seu pokemon:   
print('\nVoce comeca com o pokemon {0}!! \nEle é do tipo {1} e tem:\n{2} pontos de vida;\n{3} de poder de ataque;\n{4} de defesa;\n{5} de ataque especial;\n{6} de defesa especial;\n{7} de velocidade!'.format(suapokedex[0]['nome'],suapokedex[0]['tipo'],suapokedex[0]['PS']*3,suapokedex[0]['ataque'],suapokedex[0]['defesa'],suapokedex[0]['ataque especial'],suapokedex[0]['defesa especial'],suapokedex[0]['velocidade']))

#encontrar ou nao o bicho
#lutar ou correr
#morrer ou nao
#trocar de pokemon
#treinar pokes
#evoluir o poke
#passar de nivel
#ir passear em lugares novos do nivel (disponibilizados)


x = 0

#Lopping infinito
while x == 0:
  opcao = input('escolha: dormir ou passear?')
  if opcao == 'passear':
    inimigo = rdm.randint(0,7)
    pokedex1[inimigo]['PS'] - ()
  elif opcao == 'dormir':
    print('Boa noite')
    x = 1

    
    
    
    
    
    
    
    
    
    