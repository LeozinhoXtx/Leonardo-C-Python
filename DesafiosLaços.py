

lista_numeros= [10,5,9,4]  #esta linha estou criando uma lista de numeros diversos
multiplicacao_acumulada=1  #aqui estou criando uma variavel chamada multiplicaçao_acumulada com valor zero

for i in  lista_numeros: #traduçao:for (para) i (cada) in (dentro) da lista de numeros,vou rodar o codigo abaixo
  multiplicacao_acumulada=multiplicacao_acumulada * i  #multiplicaçao_acumulada += i 
  print(multiplicacao_acumulada) #imprimir o resultado em tela para cada vez que o laço e executado/rodado
