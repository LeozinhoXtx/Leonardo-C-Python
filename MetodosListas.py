#Metodo .append()=Adiciona um elemento na lista
#Por padrão,o elemento é sempre adicionado na ultima posiçao da lista


nomes=['Fabio','Larissa']
lista=nomes.append('Gabriel')
print(nomes)

#Metodo .insert(Posiçao,item a ser adicionado)
#Posiçao em python começa em zero

nomes.insert(1,'Renato')
print(nomes)

#Metodo .remove()=Remover o item dentro especificado de uma lista
#nomes.remove('larissa')
#print(nomes)

#Metodo .sort(), ele ORDENA em ordem alfabetica OU numerica uma lista
#Ele nao ordena listas misturadas como letras e numeros

nomes.sort()
print(nomes)

Lista_numeros_aleatorios=[2,4,1,9,5,3,10,15,11,10]
Lista_numeros_aleatorios.sort()
print(Lista_numeros_aleatorios)

#Metodo .reverse(),ele inverte a ordem de uma lista

Lista_numeros_aleatorios.reverse()
print(Lista_numeros_aleatorios)

#Metodo .count(item),ele conta a quantidade de ocorrencias de um item especificado
print(Lista_numeros_aleatorios.count(10))

#Metodo len(LISTA) , ele conta a quantidades de elementos dentro de uma lista especificada
print(len(Lista_numeros_aleatorios))

#Metodo .index(ITEM PROCURADO)
print(Lista_numeros_aleatorios.index(9))


#ITERAVEL=Posso acessar item a item de uma lista separadamente


nomes=['n1','n2','n3']
for n in (nomes):
   print(n)




