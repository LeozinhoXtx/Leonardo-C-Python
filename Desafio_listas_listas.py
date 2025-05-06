#Criamos uma lista de listas,contendo nomes e pontuaçoes para cada jogador
jogadores = [
    ["Lucas", 100, 98, 105],
    ["Ana", 88, 90, 95],
    ["Bruno", 120, 130, 128],
    ["Carla", 85, 80, 78]
]

#Criamos uma lista vazia que recebera listas com nomes e medias de cada jogador
lista_total=[]

for p in jogadores: #Para cada p=players dentro da lista jogadores
    nome_jogador= p[0] #quero acessar a posiçao 0 da lista dentro da lista jogadores,que seria nomes dos jogadores EX:LUCAS,ANA,BRUNO,CARLA
    media_jogador= sum(p[1:]) / len(p[1:])#Utilizamos a tecnica de fatiamento,pegando as informaçoes desde a posiçao 1 de cada lista
    lista_total.append([nome_jogador,media_jogador])#Adicionamos dentro da lista vazia lista_total as informaçoes de cada jogador seguido da media calculada

print(lista_total)

#Ordenar com base na média
ranking = sorted(lista_total, key=lambda x: x[1], reverse=True)
print(ranking)

print(f'O jogador com a maior média é:{ranking[0][0]}')
print(f'O jogador com a menor média é:{ranking[-1][0]}')



