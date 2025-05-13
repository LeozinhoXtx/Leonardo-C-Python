#Tuplas=Sao estruturas que armazenam varios tipos de dados,e que sao IMUTÁVEIS seus elementos ,ou seja ,nao posso altera-los
#Tuplas=é representada pelo par de '()' parenteses
#Tuplas=É indexável,e utiliza-se o colchete [e] com a numeraçao do elemento
#Tuplas=Ela suporta Fatiamento(slicing)


tupla_preços=(10,9,5)


print(tupla_preços[1]) #9
print(tupla_preços[0:2]) #10,9

print(list(tupla_preços)) #Vai converter a tupla_preços em uma lista
lista_preços=[10,9,7]
print(tuple(lista_preços)) #Vai converter a lista_preços em uma tupla

#Lista =alterando elemento em uma lista

roupas_lista=['camisa','calça','blazer']
roupas_lista[0]='camiseta'
print(roupas_lista)

#Tupla=Alterando elemento em uma lista

roupas_tupla=('camisa','calça','blazer')
#roupas_tupla[0]='camiseta'
print(roupas_tupla)  #Erro! Tuplas nao podem ser alteradas

#metodos aceitaveis em uma tupla

cores=('azul', 'verde','vermelho','azul','azul')
print(cores.count('azul'))
print(cores.index('verde')) #Retorna a posiçao da 1 vez q a palavra verde aparece


