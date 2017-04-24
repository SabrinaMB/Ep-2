#importar o necessario
import sys,time
import random as rdm
import json


#abrir os arquivos das pokedex
with open('pokedex1.json') as arquivop1: 
    pokedex1 = json.load(arquivop1)
    arquivop1.close()
    
with open('evolucoes1.json') as arquivoe1: 
    evolucoes1 = json.load(arquivoe1)
    arquivoe1.close()
    
with open('evolucoes2.json') as arquivoe2: 
    evolucoes2 = json.load(arquivoe2)
    arquivoe2.close()
    
with open('pokedex10.json') as arquivop10: 
    pokedex10 = json.load(arquivop10)
    arquivop10.close()
    
with open('pokedex50.json') as arquivop50: 
    pokedex50 = json.load(arquivop50)
    arquivop50.close()
    
with open('pokedex100.json') as arquivop100: 
    pokedex100 = json.load(arquivop100)
    arquivop100.close()
    
with open('suapokedex.json') as arquivo: 
    suapokedex = json.load(arquivo)
    arquivo.close()
        
with open('nivel.json') as arquivon: 
    nivel = json.load(arquivon)
    arquivon.close()
    
with open('contador.json') as arquivoc: 
    contador = json.load(arquivoc)
    arquivoc.close()
    
#definindo as funcoes:
#funcao para printar devagar
def print_slow(str):
     for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

#funcao para batalhar
def suafuncaobatalha(suavida,caraataque,suadefesa):
    taxasortea = rdm.randint(0,100)/100
    taxasorted = rdm.randint(0,100)/100
    if suadefesa*taxasorted <= caraataque*taxasortea:
        suavida = suavida - (caraataque*taxasortea - suadefesa*taxasorted)
    if suavida < 0:
        suavida = 0
    else:
        suavida = suavida
    return float(round(suavida,2))

def carafuncaobatalha(caravida,seuataque,caradefesa):
    taxasortea = rdm.randint(0,100)/100
    taxasorted = rdm.randint(0,100)/100
    if seuataque*taxasortea >= caradefesa*taxasorted:
        caravida = caravida - (seuataque*taxasortea - caradefesa*taxasorted)
    if caravida < 0:
        caravida = 0 
    else:
        caravida = caravida
    return float(round(caravida,2))


#criando o if de se voce tem um ou mais pokemons
if len(suapokedex) == 1:
    print_slow('\nVoce comeca com o pokemon {0}!! \nEle é do tipo {1} e tem:\n{2} pontos de vida;\n{3} de poder de ataque;\n{4} de defesa;\n{5} de velocidade!'.format(suapokedex[0]['nome'],suapokedex[0]['tipo'],suapokedex[0]['PS'],suapokedex[0]['ataque'],suapokedex[0]['defesa'],suapokedex[0]['velocidade']))
else:
    print("\nVocê tem os seguintes pokemons:\n")
    for i in range(len(suapokedex)):
        print('{0}\n \nEle é do tipo {1} e tem:\n{2} pontos de vida;\n{3} de poder de ataque;\n{4} de defesa;\n{5} de velocidade!!\n\n'.format(suapokedex[i]['nome'],suapokedex[i]['tipo'],suapokedex[i]['PS'],suapokedex[i]['ataque'],suapokedex[i]['defesa'],suapokedex[i]['velocidade']))



#criando variaveis necessarias para o while:
#iniciando a variavel pp que sera usada para definir a posicao do pokemon na lista
pp = 0
#criando uma lista vazia que contera os pokemons adicionados a suapokedex e excluira os perdidos, para mudar a posicao dos pokemons (nao pode jogar com o poke que nao tem)
LP = []
#definindo o valor de xp ganhado após cada batalha vencida
k = 20
#variavel para rodar o while
x = 0

#Lopping infinito nivel 1
if nivel == 1:
    while x == 0:
        opcao = input('Você deseja:\n(1)Passear;\n(2)Dormir;\n(3)Treinar? (Se não selecionar nenhum pokemon você começará com o primeiro. Para selecionar um pokemon vá passear)')      
        if opcao == '1':
            #se ele tiver mais de um pokemon ele pode escolher c qual quer jogar
            if len(suapokedex) > 1:
                for i in suapokedex:
                    print(i['nome'])
                ppm = input('Com qual pokemon você quer jogar? (Para escolher o primeiro digite 1, para o segundo digite 2, para o terceiro 3 e assim por diante.)')
                while ppm not in range(len(suapokedex)):
                    try:
                        ppm = int(ppm)
                    except ValueError:
                        print("Ei!! Você só tem essas opções!!")
                        ppm = input('Com qual pokemon você quer jogar? (Para escolher o primeiro digite 1, para o segundo digite 2, para o terceiro 3 e assim por diante.)')
                pp = ppm - 1
                print('Você esta jogando com o {0}.'.format(suapokedex[pp]['nome']))
            print_slow("Você está passeando...\n")
            print("Você encontrou um inimigo!!")
            #ve se entra na pokedex1 ou na pokedex10
            if contador <1:
                #escolher um numero aleatorio para definir a posicao do inimigo na pokedex1
                inimigo = rdm.randint(0,len(pokedex1)-1)
        
                #definir as variaveis para rodar a funcaobatalha
                suavida = int(suapokedex[pp]['PSA'])
                seuataque = int(suapokedex[pp]['ataque'])
                suadefesa = int(suapokedex[pp]['defesa'])
                vidainimigo = int(pokedex1[inimigo]['PS'])
                ataqueinimigo = int(pokedex1[inimigo]['ataque'])
                defesainimigo = int(pokedex1[inimigo]['defesa'])
                print_slow("E o nome dele é.....{0}\n".format(pokedex1[inimigo]['nome']))
                print("Ele é do tipo {0} e tem:\n{1} pontos de vida;\n{2} de poder de ataque;\n{3} de defesa;\n{4} de velocidade!".format(pokedex1[inimigo]['tipo'],pokedex1[inimigo]['PS'],pokedex1[inimigo]['ataque'],pokedex1[inimigo]['defesa'],pokedex1[inimigo]['velocidade']))
                Batalhar = input("Você deseja:\n(1)Batalhar;\n(2)Correr?")
                if Batalhar =='1':
                    print('Boa sorte na batalha, jogador!!')                
                elif Batalhar=='2':
                    if suapokedex[pp]['velocidade'] >= pokedex1[inimigo]['velocidade']:
                        print("Boa!! Você conseguiu fugir!!")
                    else:
                        print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                        Batalhar = '1'
                else:
                    print("Ei!! Você tem que escolher alguma opção, senão irá batalhar!!")
                    print('Boa sorte na batalha, jogador!!')
                    Batalhar = '1'
                #gerando un whille para rodar a funcaobatalha
                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                while Batalhar == "1" and suapokedex[pp]['PSA']>0 and vidainimigo>0:
                    print('\nEle te bateu e voce se defendeu!')
                    suapokedex[pp]['PSA'] = suafuncaobatalha(suapokedex[pp]['PSA'],ataqueinimigo,suadefesa)
                    print_slow("Por causa disso, sua nova vida é:{}".format(suapokedex[pp]['PSA']))
                    if suapokedex[pp]['PSA']>0:
                        print('\nMas voce bateu nele e ele se defendeu!')
                        vidainimigo = carafuncaobatalha(vidainimigo,seuataque,defesainimigo)
                        print_slow("Entao, a nova vida do seu inimigo é:{}".format(vidainimigo))
                      
                    if suapokedex[pp]['PSA'] == 0:
                        print_slow("\nDesculpe... Você perdeu. Agora o seu pokemon precisa descansar e restaurar suas forças para mais batalhas.\n")
                        if len(suapokedex) > 1:
                            print('\nVoce tem esses pokemons disponiveis:\n')
                            for i in suapokedex:
                                if i['PSA'] > 0:
                                    print(i["nome"])
                                    LP.append(i)
                            
                            ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            while ct not in range(len(LP)):
                                try:
                                    ct = int(ct)
                                except ValueError:
                                    print("Ei!! Você só tem essas opções!!")
                                    ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            ct = ct - 1
                            suapokedex[pp]['PSA'] = suapokedex[pp]['PS']                            
                            for r in suapokedex:   
                                #se o nome do meu poke na lista LP (nova lista p cara q quer continuar jogando) for igual ao nome da 
                                #minha lista pokedex, entao ele substitui a posicao do meu pp pra que os calculos da batalha e tudo
                                #mais que envolve o meu poke da batalha possa ser calculado de maneira correta.
                                if r['nome'] == LP[ct]['nome']:
                                    pp = suapokedex.index(r)
                            
                    if vidainimigo<=0:
                        print_slow('\nParabens!! Voce venceu!!\nPor isso voce ganhou {0} XPs\n'.format(k))
                        suapokedex[pp]['xp'] += k
                        app = 0
                        while app == 0:
                            ap = input('Voce quer adicionar o pokemon {0} na sua pokedex?\n(1)Sim\n(2)Nao\n'.format(pokedex1[inimigo]['nome']))
                            if ap == '1':
                                suapokedex.append(pokedex1[inimigo])
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow("Agora, o pokemon {0} foi adicionado a sua pokedex!!\n".format(pokedex1[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                app = 1
                            elif ap == '2':
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow('Tudo bem, {} nao foi adicionado a sua lista.'.format(pokedex1[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                app = 1
                            else:
                                print_slow("Ei!! Você só tem essas opções!!")
                    elif (suapokedex[pp]['PSA']>0) and (vidainimigo>0):
                        Batalhar = input("\nVocê deseja:\n(1)Continuar batalhando;\n(2)Fugir??")
                        if Batalhar=='2':
                            if suapokedex[pp]['velocidade'] >= pokedex1[inimigo]['velocidade']:
                                print("Boa!! Você conseguiu fugir!!")
                                print('A vida de seu pokemon foi restaurada para mais batalhas!')
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            else:
                                print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                                Batalhar='1'
                        
                        elif Batalhar=='1':
                            Batalhar='1'
                        else: 
                            print('Você tem que escolher alguma opção, senão continuara batalhando')
                            Batalhar ='1'
            elif contador <3 and contador >=1:
                #entra na pokedex 10
                #escolher um numero aleatorio para definir a posicao do inimigo na pokedex10
                inimigo = rdm.randint(0,len(pokedex10)-1)
    
                #definir as variaveis para rodar a funcaobatalha
                suavida = int(suapokedex[pp]['PSA'])
                seuataque = int(suapokedex[pp]['ataque'])
                suadefesa = int(suapokedex[pp]['defesa'])
                vidainimigo = int(pokedex10[inimigo]['PS'])
                ataqueinimigo = int(pokedex10[inimigo]['ataque'])
                defesainimigo = int(pokedex10[inimigo]['defesa'])
                print_slow("E o nome dele é.....{0}\n".format(pokedex10[inimigo]['nome']))
                print("Ele é do tipo {0} e tem:\n{1} pontos de vida;\n{2} de poder de ataque;\n{3} de defesa;\n{4} de velocidade!".format(pokedex10[inimigo]['tipo'],pokedex10[inimigo]['PS'],pokedex10[inimigo]['ataque'],pokedex10[inimigo]['defesa'],pokedex10[inimigo]['velocidade']))
                Batalhar = input("Você deseja:\n(1)Batalhar;\n(2)Correr?")
                if Batalhar == '1':
                    print('Boa sorte na batalha, jogador!!')                
                elif Batalhar == '2':
                    if suapokedex[pp]['velocidade'] >= pokedex10[inimigo]['velocidade']:
                        print("Boa!! Você conseguiu fugir!!")
                    else:
                        print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                        Batalhar = '1'
                else:
                    print("Ei!! Você tem que escolher alguma opção, senão irá batalhar!!")
                    print('Boa sorte na batalha, jogador!!')                    
                    Batalhar = '1'
                #gerando un whille para rodar a funcaobatalha
                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                while Batalhar == "1" and suapokedex[pp]['PSA']>0 and vidainimigo>0:
                    print('\nEle te bateu e voce se defendeu!')
                    suapokedex[pp]['PSA'] = suafuncaobatalha(suapokedex[pp]['PSA'],ataqueinimigo,suadefesa)
                    print_slow("\nPor causa disso, sua nova vida é:{}".format(suapokedex[pp]['PSA']))
                    if suapokedex[pp]['PSA']>0:
                        print('\nMas voce bateu nele e ele se defendeu!')
                        vidainimigo = carafuncaobatalha(vidainimigo,seuataque,defesainimigo)
                        print_slow("Entao, a nova vida do seu inimigo é:{}".format(vidainimigo))
                      
                    if suapokedex[pp]['PSA'] == 0:
                        print_slow("\nDesculpe... Você perdeu. Agora o seu pokemon precisa descansar e restaurar suas forças para mais batalhas.\n")
                        if len(suapokedex) > 1:
                            print('\nVoce tem esses pokemons disponiveis:\n')
                            for i in suapokedex:
                                if i['PSA'] > 0:
                                    print(i["nome"])
                                    LP.append(i)
                            
                            ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            while ct not in range(len(LP)):
                                try:
                                    ct = int(ct)
                                except ValueError:
                                    print("Ei!! Você só tem essas opções!!")
                                    ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            ct = ct -1
                            suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            
                            for r in suapokedex:   
                                #se o nome do meu poke na lista LP (nova lista p cara q quer continuar jogando) for igual ao nome da 
                                #minha lista pokedex, entao ele substitui a posicao do meu pp pra que os calculos da batalha e tudo
                                #mais que envolve o meu poke da batalha possa ser calculado de maneira correta.
                                if r['nome'] == LP[ct]['nome']:
                                    pp = suapokedex.index(r)
                            
                    if vidainimigo<=0:
                        print_slow('\nParabens!! Voce venceu!!\nPor isso voce ganhou {0} XPs\n'.format(k))
                        suapokedex[pp]['xp'] += k
                        appp = 0
                        while appp == 0:
                            apu = input('Voce quer adicionar o pokemon {0} na sua pokedex?\n(1)Sim\n(2)Nao\n'.format(pokedex10[inimigo]['nome']))
                            if apu == '1':
                                suapokedex.append(pokedex10[inimigo])
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow("Agora, o pokemon {0} foi adicionado a sua pokedex!!\n".format(pokedex10[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                appp = 1
                            elif apu == '2':
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow('Tudo bem, {} nao foi adicionado a sua lista.'.format(pokedex10[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                appp = 1
                            else:
                                print_slow("Ei!! Você só tem essas opções!!")
                     
                    elif (suapokedex[pp]['PSA']>0) and (vidainimigo>0):
                        Batalhar = input("Você deseja:\n(1)Continuar batalhando;\n(2)Fugir??")
                        if Batalhar=='2':
                            if suapokedex[pp]['velocidade'] >= pokedex10[inimigo]['velocidade']:
                                print("Boa!! Você conseguiu fugir!!")
                                print('A vida de seu pokemon foi restaurada para mais batalhas!')
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            else:
                                print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                                Batalhar='1'
            
                        elif Batalhar=='1':
                            Batalhar='1'
                        else: 
                            print('Você tem que escolher alguma opção, senão continuara batalhando')
                            Batalhar ='1'

           
        elif opcao == '2':
            print_slow('Boa Noite!                ')
            dorminhoco = input('\nQuer acordar?\n(1)Sim\n(2)Nao')
            if dorminhoco == "1":
                x = 0
            elif dorminhoco == "2":
                print_slow('Tchau Tchau!!')
                x = 1
            else:
                print("Ei!! Você quer dormir ou não??")
                
        elif opcao == '3':
            if 'nomeantigo' in suapokedex[pp]:
                print("Seu pokemon não pode mais ser evoluido")
            else:
                if suapokedex[pp]['xp'] >= 80:
                    print("Muito bem!! Seu pokemon foi evoluido!!")
                    contador += 1
                    for i in range(len(evolucoes1)):
                        if suapokedex[pp]['nome'] == evolucoes1[i]['nomeantigo']:
                            suapokedex.append(evolucoes1[i])
                            del suapokedex[pp]
                        if contador == 3:
                            with open('nivel.json', 'w') as arquivon: 
                                arquivon.write(json.dumps(2))
                                arquivon.close()
                            print("Parabéns!! Passou para o nível 2!!")
                else:
                    print("Você ainda não pode treinar, precisa de 80 XPs no pokemom que você deseja treinar.")
        
        else:
            print("Ei!! Você só tem essas opções!!")

elif nivel == 2:
    while x == 0:
        opcao = input('Você deseja:\n(1)Passear;\n(2)Dormir;\n(3)Treinar?')      
        if opcao == '1':
            #se ele tiver mais de um pokemon ele pode escolher c qual quer jogar
            if len(suapokedex) > 1:
                for i in suapokedex:
                    print(i['nome'])
                    
                ppm = input('Com qual pokemon você quer jogar? (Para escolher o primeiro digite 1, para o segundo digite 2, para o terceiro 3 e assim por diante.)')
                while ppm not in range(len(suapokedex)):
                    try:
                        ppm = int(ppm)
                    except ValueError:
                        print("Ei!! Você só tem essas opções!!")
                        ppm = input('Com qual pokemon você quer jogar? (Para escolher o primeiro digite 1, para o segundo digite 2, para o terceiro 3 e assim por diante.)')
                pp = ppm - 1
                print('Você esta jogando com o {0}.'.format(suapokedex[pp]['nome']))
            print_slow("Você está passeando...\n")
            print("Você encontrou um inimigo!!")
            #parque nivel dois parte um (sem evoluções)
            if contador >=3 and contador <6:            
                #escolher um numero aleatorio para definir a posicao do inimigo na pokedex50
                inimigo = rdm.randint(0,len(pokedex50)-1)
        
                #definir as variaveis para rodar a funcaobatalha
                suavida = int(suapokedex[pp]['PSA'])
                seuataque = int(suapokedex[pp]['ataque'])
                suadefesa = int(suapokedex[pp]['defesa'])
                vidainimigo = int(pokedex50[inimigo]['PS'])
                ataqueinimigo = int(pokedex50[inimigo]['ataque'])
                defesainimigo = int(pokedex50[inimigo]['defesa'])
                print_slow("E o nome dele é.....{0}\n".format(pokedex50[inimigo]['nome']))
                print("Ele é do tipo {0} e tem:\n{1} pontos de vida;\n{2} de poder de ataque;\n{3} de defesa;\n{4} de velocidade!".format(pokedex50[inimigo]['tipo'],pokedex50[inimigo]['PS'],pokedex50[inimigo]['ataque'],pokedex50[inimigo]['defesa'],pokedex50[inimigo]['velocidade']))
                Batalhar = input("Você deseja:\n(1)Batalhar;\n(2)Correr?")
                if Batalhar =='1':
                    print('Boa sorte na batalha, jogador!!')
                elif Batalhar=='2':
                    if suapokedex[pp]['velocidade'] >= pokedex50[inimigo]['velocidade']:
                        print("Boa!! Você conseguiu fugir!!")
                    else:
                        print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                        Batalhar = '1'
                else:
                    print("Ei!! Você tem que escolher alguma opção, senão irá batalhar!!")
                    print('\nBoa sorte na batalha, jogador!!')
                    Batalhar = '1'
                #gerando un whille para rodar a funcaobatalha
                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                while Batalhar == "1" and suapokedex[pp]['PSA']>0 and vidainimigo>0:
                    print('\nEle te bateu e voce se defendeu!')
                    suapokedex[pp]['PSA'] = suafuncaobatalha(suapokedex[pp]['PSA'],ataqueinimigo,suadefesa)
                    print_slow("\nPor causa disso, sua nova vida é:{}".format(suapokedex[pp]['PSA']))
                    if suapokedex[pp]['PSA']>0:
                        print('\nMas voce bateu nele e ele se defendeu!')
                        vidainimigo = carafuncaobatalha(vidainimigo,seuataque,defesainimigo)
                        print_slow("\nEntao, a nova vida do seu inimigo é:{}".format(vidainimigo))
                      
                    if suapokedex[pp]['PSA'] == 0:
                        print_slow("\nDesculpe... Você perdeu. Agora o seu pokemon precisa descansar e restaurar suas forças para mais batalhas.\n")
                        if len(suapokedex) > 1:
                            print('\nVoce tem esses pokemons disponiveis:\n')
                            for i in suapokedex:
                                if i['PSA'] > 0:
                                    print(i["nome"])
                                    LP.append(i)
                            
                            ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                        
                            while ct not in range(len(LP)):
                                try:
                                    ct = int(ppm)
                                except ValueError:
                                    print("Ei!! Você só tem essas opções!!")
                                    ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            ct = ct -1
                            suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            for r in suapokedex:   
                                #se o nome do meu poke na lista LP (nova lista p cara q quer continuar jogando) for igual ao nome da 
                                #minha lista pokedex, entao ele substitui a posicao do meu pp pra que os calculos da batalha e tudo
                                #mais que envolve o meu poke da batalha possa ser calculado de maneira correta.
                                if r['nome'] == LP[ct]['nome']:
                                    pp = suapokedex.index(r)
                            
                    if vidainimigo<=0:
                        print_slow('\nParabens!! Voce venceu!!\nPor isso voce ganhou {0} XPs\n'.format(k))
                        suapokedex[pp]['xp'] += k
                        apppp = 0
                        while apppp == 0:
                            apo = input('Voce quer adicionar o pokemon {0} na sua pokedex?\n(1)Sim\n(2)Nao\n'.format(pokedex50[inimigo]['nome']))
                            if apo == '1':
                                suapokedex.append(pokedex50[inimigo])
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow("Agora, o pokemon {0} foi adicionado a sua pokedex!!\n".format(pokedex50[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                apppp = 1
                            elif apo == '2':
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow('Tudo bem, {} nao foi adicionado a sua lista.'.format(pokedex50[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                apppp = 1
                            else:
                                print_slow("Ei!! Você só tem essas opções!!")
                     
                    elif (suapokedex[pp]['PSA']>0) and (vidainimigo>0):
                        Batalhar = input("Você deseja:\n(1)Continuar batalhando;\n(2)Fugir??")
                        if Batalhar=='2':
                            if suapokedex[pp]['velocidade'] >= pokedex50[inimigo]['velocidade']:
                                print("Boa!! Você conseguiu fugir!!")
                                print('A vida de seu pokemon foi restaurada para mais batalhas!')
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            else:
                                print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                                Batalhar='1'
            
                        elif Batalhar=='1':
                            Batalhar='1'
                        else: 
                            print('Você tem que escolher alguma opção, senão continuara batalhando')
                            Batalhar ='1'
            
    #parque nivel dois parte dois (com evoluções)
            elif contador >6:            
                #escolher um numero aleatorio para definir a posicao do inimigo na pokedex100
                inimigo = rdm.randint(0,len(pokedex100)-1)
        
                #definir as variaveis para rodar a funcaobatalha
                suavida = int(suapokedex[pp]['PSA'])
                seuataque = int(suapokedex[pp]['ataque'])
                suadefesa = int(suapokedex[pp]['defesa'])
                vidainimigo = int(pokedex100[inimigo]['PS'])
                ataqueinimigo = int(pokedex100[inimigo]['ataque'])
                defesainimigo = int(pokedex100[inimigo]['defesa'])
                print_slow("E o nome dele é.....{0}\n".format(pokedex100[inimigo]['nome']))
                print("Ele é do tipo {0} e tem:\n{1} pontos de vida;\n{2} de poder de ataque;\n{3} de defesa;\n{4} de velocidade!".format(pokedex100[inimigo]['tipo'],pokedex100[inimigo]['PS'],pokedex100[inimigo]['ataque'],pokedex100[inimigo]['defesa'],pokedex100[inimigo]['velocidade']))
                Batalhar = input("Você deseja:\n(1)Batalhar;\n(2)Correr?")
                if Batalhar =='1':
                    print('Boa sorte na batalha, jogador!!')
                elif Batalhar=='2':
                    if suapokedex[pp]['velocidade'] >= pokedex100[inimigo]['velocidade']:
                        print("Boa!! Você conseguiu fugir!!")
                    else:
                        print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                        Batalhar = 1
                else:
                    print("Ei!! Você tem que escolher alguma opção, senão irá batalhar!!")
                    print('Boa sorte na batalha, jogador!!')
                    Batalhar = '1'
                #gerando un while para rodar a funcaobatalha
                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                while Batalhar == "1" and suapokedex[pp]['PSA']>0 and vidainimigo>0:
                    print('\nEle te bateu e voce se defendeu!')
                    suapokedex[pp]['PSA'] = suafuncaobatalha(suapokedex[pp]['PSA'],ataqueinimigo,suadefesa)
                    print_slow("\nPor causa disso, sua nova vida é:{}".format(suapokedex[pp]['PSA']))
                    if suapokedex[pp]['PSA']>0:
                        print('\nMas voce bateu nele e ele se defendeu!')
                        vidainimigo = carafuncaobatalha(vidainimigo,seuataque,defesainimigo)
                        print_slow("\nEntao, a nova vida do seu inimigo é:{}".format(vidainimigo))
                      
                    if suapokedex[pp]['PSA'] == 0:
                        print_slow("\nDesculpe... Você perdeu. Agora o seu pokemon precisa descansar e restaurar suas forças para mais batalhas.\n")
                        if len(suapokedex) > 1:
                            print('\nVoce tem esses pokemons disponiveis:\n')
                            for i in suapokedex:
                                if i['PSA'] > 0:
                                    print(i["nome"])
                                    LP.append(i)
                            
                            ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            while ct not in range(len(LP)):
                                try:
                                    ct = int(ppm)
                                except ValueError:
                                    print("Ei!! Você só tem essas opções!!")
                                    ct = input('Para continuar batalhando escolha um dos pokemons acima. (O primeiro pokemon é o numero 1 etc.) Senao vc tem que fugir.')
                            ct = ct - 1
                            suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            for r in suapokedex:   
                                #se o nome do meu poke na lista LP (nova lista p cara q quer continuar jogando) for igual ao nome da 
                                #minha lista pokedex, entao ele substitui a posicao do meu pp pra que os calculos da batalha e tudo
                                #mais que envolve o meu poke da batalha possa ser calculado de maneira correta.
                                if r['nome'] == LP[ct]['nome']:
                                    pp = suapokedex.index(r)
                    if vidainimigo<=0:
                        print_slow('\nParabens!! Voce venceu!!\nPor isso voce ganhou {0} XPs\n'.format(k))
                        suapokedex[pp]['xp'] += k
                        appppp = 0
                        while appppp == 0:
                            apy = input('Voce quer adicionar o pokemon {0} na sua pokedex?\n(1)Sim\n(2)Nao\n'.format(pokedex100[inimigo]['nome']))
                            if apy == '1':
                                suapokedex.append(pokedex100[inimigo])
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow("Agora, o pokemon {0} foi adicionado a sua pokedex!!\n".format(pokedex100[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                appppp = 1
                            elif apy == '2':
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                                print_slow('Tudo bem, {} nao foi adicionado a sua lista.'.format(pokedex100[inimigo]['nome']))
                                print_slow('A vida de seu pokemon foi restaurada para mais batalhas!')
                                appppp = 1
                            else:
                                print_slow("Ei!! Você só tem essas opções!!")
                     
                    elif (suapokedex[pp]['PSA']>0) and (vidainimigo>0):
                        Batalhar = input("Você deseja:\n(1)Continuar batalhando;\n(2)Fugir??")
                        if Batalhar=='2':
                            if suapokedex[pp]['velocidade'] >= pokedex100[inimigo]['velocidade']:
                                print("Boa!! Você conseguiu fugir!!")
                                print('A vida de seu pokemon foi restaurada para mais batalhas!')
                                suapokedex[pp]['PSA'] = suapokedex[pp]['PS']
                            else:
                                print('Desculpe, mas o seu inimigo é mais rápido do que você!! Você terá de batalhar!!')
                                Batalhar='1'
            
                        elif Batalhar=='1':
                            Batalhar='1'
                        else: 
                            print('Você tem que escolher alguma opção, senão continuara batalhando')
                            Batalhar ='1'
     
        
        elif opcao == '2':
            print_slow('Boa Noite!                ')
            dorminhoco = input('\nQuer acordar?\n(1)Sim\n(2)Não')
            if dorminhoco == "1":
                x = 0
            elif dorminhoco == "2":
                print_slow('Tchau Tchau!!')
                x = 1
            else:
                print("Ei!! Você quer dormir ou não??")
                
        elif opcao == '3':
            if 'nomeantigo' in suapokedex[pp]:
                print("Seu pokemon não pode mais ser evoluido")
            else:
                if suapokedex[pp]['xp'] >= 80:
                    if suapokedex[pp] in evolucoes1 or suapokedex[pp] in evolucoes2:
                        print("Seu pokemon não pode mais ser evoluido")
                    else:
                        for i in range(len(evolucoes1)):
                            if suapokedex[pp]['nome'] == evolucoes1[i]['nomeantigo']:
                                suapokedex.append(evolucoes1[i])
                                del suapokedex[pp]
                        for i in range(len(evolucoes2)):
                            if suapokedex[pp]['nome'] == evolucoes2[i]['nomeantigo']:
                                suapokedex.append(evolucoes2[i])
                                del suapokedex[pp]
                        print("Muito bem!! Seu pokemon foi evoluido!!")
                else:
                    print("Você ainda não pode treinar, precisa de 80 XPs no pokemom que você deseja treinar.")
        
        else:
            print("Ei!! Você só tem essas opções!!")
        
    
salvar = input("Você gostaria de salvar o seu progresso??\n(1)Sim;\n(2)Não (Você continuara no nivel em que está de um jeito ou de outro)")
if salvar == '1':
    with open('suapokedex.json', 'w') as arquivo: 
        arquivo.write(json.dumps(suapokedex))
        arquivo.close()
    with open('contador.json', 'w') as arquivoc: 
        arquivoc.write(json.dumps(contador))
        arquivoc.close()
else:
    salvar = 2
