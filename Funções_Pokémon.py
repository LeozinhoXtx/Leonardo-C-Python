import random

#Criamos um dicionario aninhado(Dicionario dentro de dicionario)
pokemons = {
    'Charmander':{'Ataque': 'Bola de fogo', 'Dano': 35},
    'Squirtle':{'Ataque': 'Jato de água', 'Dano': 32},
    'Bulbassauro':{'Ataque': 'Chicote de planta', 'Dano': 30},
}

jogador1 = ' '
jogador2 = ' '

def selecionar_pokemon(jogador,):
    print('SELECIONE SEU POKEMON' .center (40,'-'))
    print(' (1) Charmander \n (2) Squirtle \n (3) Bulbassauro') #Quebrando linhas com \n
    print('_'*40)
    escolha = int(input('Escolha seu Pokémon (1,2 ou 3) ? '))
    if escolha == 1:
       escolha = "Charmander"
    elif escolha == 2:
       escolha = "Squirtle"
    elif escolha == 3:
        escolha = "Bulbassauro"
    else:
        print('Não entendi! Digite 1,2 ou 3')
    
    return escolha

escolha1 = selecionar_pokemon(jogador1)
escolha2 = selecionar_pokemon(jogador2)


def ficha_habilidades(escolha):
    print('FICHA DE HABILIDADES'.center(40,'-'))
    print(f'Vida : 100 | Ataque: { pokemons[escolha]['Ataque']}')

ficha_habilidades(escolha1)

def ataque (escolha): 
     return pokemons[escolha]['Dano'] * random.uniform(1,2)

dano1 = ataque (escolha1)
dano2 = ataque (escolha2)

print(f'O dano do Pokemon {escolha1} foi de {dano1:.2f}')
print(f'O dano do Pokemon {escolha2} foi de {dano2:.2f}')

def batalha_final():
    vida_restante1 = 100 - dano2 
    vida_restante2 = 100 - dano1

    if vida_restante1 > vida_restante2:
        print(f'Vencedor: Jogador1, pois a vida do jogador 2 é menor {vida_restante2:.2f}')
    else:
        print(f'Vencedor: Jogador2, pois a vida do jogador 2 é menor {vida_restante1:.2f}')

batalha_final()


