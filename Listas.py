#LISTA=Estrutura ordenada de informaçao

#LISTA=Recebem varios tipos de dados

#lista de strings
Lista_fruta=['Maça','Uva','pera']

#Lista de numeros
Lista_Numeros=[1,4,6,9,3]

#Lista misturadas com strings,numeros e booleanos
Lista_misturadas=['Leonardo',26,True]

#Lista para calcular média de notas
Lista_notas=[6,8,9,10,2,5,7,1,3,0]
Media= sum(Lista_notas) / len(Lista_notas)
print(f'A Mèdia da lista de notas è de {Media}')


#Automaçao de Mensagens
Lista_nomes=['Ana','Gabriel','Leonardo']

for n in Lista_nomes:#Estrutura de laço para percorrer os elementos da lista_nomes
    print(f'O nome atual é {n}')


#Aplicaçao de filtros para nomes que começam com L

Lista_nome2=['Leonardo','Luana','Larissa','Bruno','Kleber','Matheus']
Lista_nome2_1=[]

for n in Lista_nome2:
    if n.startswith('L'):
       Lista_nome2_1.append(n)

print(Lista_nome2_1)

#Indexaçao de listas
lista_jogos= ['COD','Valorant','Fortnite']
print(lista_jogos[0])
print(lista_jogos[2])
print(lista_jogos[-1])
print(lista_jogos[-3])

#Listas de Listas
lista_clientes=[
    ['Alvaro','alvaro.sampaio@galileunegocios.com.br',32],
    ['Felipe','felipe.nasciben@galileunegocios.com.br',41],
    ['Matheus','matheus.biasotto@galileunegocios.com.br',29]
]

print(f'O nome do Cliente é:{lista_clientes[2][0]}')
print(f'A idade do cliente é:{lista_clientes[1][2]}')



