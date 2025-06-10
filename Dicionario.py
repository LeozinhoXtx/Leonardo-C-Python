#Dicionario é uma estrutura de dados que organiza informaçoes em pares chaves e valor
#Dicionario representado por {}

Arm_leo={
    'GavetaA':'Meias',#Chave:GavetaA  Valor:Meias
    'GavetaB':'Camisetas',#Chave:GavetaB  Valor:Camisetas
}

#Criei um dicionario chamado Arm_leo,onde ele possui as chaves GavetaA e GavetaB,as quais armazenam os valores meis e camisetas 
#print(Arm_leo['GavetaA'])

skins_raras_fortnite={
    'Alvaro':'Honor Guard',
    'Leo':'Double Helix',
    'Gustavo':'Ragnarox',
    'Felipe':'Galaxy',
    'João':'Black Knight',
}

#printando o valor da chave:ALvaro no dicionario skins_raras_fortnite
print(skins_raras_fortnite['Alvaro'])

#Percorrendo o dicionario utilizando o for
#for j in skins_raras_fortnite:
    #print(j)
#Neste formato imprimi todas as chaves existentes no dicionario

#Metodo .get(CHAVE) , ira retorna o valor dessa chave especificada 
print(skins_raras_fortnite.get('Alvaro'))

#Metodo .keys(), retorna todas as chaves de um dicionario
print(skins_raras_fortnite.keys())

#Metodo .values(),retorna todos os valores de um dicionario
print(skins_raras_fortnite.values())

#Metodo .items(),retorna todas as CHAVES e VALORES de um dicionario
print(skins_raras_fortnite.items())

#for j in skins_raras_fortnite.keys():
    #print(j)#Volta todas as chaves 

#for v in skins_raras_fortnite.values():
    #print(v)#Volta todos os valores

#for k, v in skins_raras_fortnite.items():#indetificamos Chave com k e valores com V
    #print(f'A chave {k} possui o valor {v}!')

#metodo .setdefaut(CHAVE,VALOR) ,verifica se dicionario possui a chave especificada .Caso negativo,ele adiciona a nova chave e atribui o valor especificado
skins_raras_fortnite.setdefault('Fabricio','Marshmello')
print(skins_raras_fortnite)

#Metodo skins_raras_fortnite.clear(),ele limpa o dicionario inteiro
skins_raras_fortnite.clear()
print(skins_raras_fortnite)

#DICIONÁRIOS ANINHADOS
jogos={
    'Minecraft':{'preço':59.90,'estoque':5},
    'FIFA 23':{'preço':199.90,'estoque':3},
    'God of war':{'preço':149.90,'estoque':4},
}

print(jogos['FIFA 23']['preço'])

for v in jogos.values():
    print(v['estoque'])







