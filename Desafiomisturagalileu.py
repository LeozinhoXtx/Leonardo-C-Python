#usuario esta informando a quantidade de misturas que ele quer verificar
Teste_Raçoes= int(input ('Boa tarde ,tudo bem sim? Quantos teste de misturas voce quer verificar?:'))

#Padroes recomendados:
print('Padroes Recomendados')
porcentagem_milho1=input('Qual porcentagem do milho:')
porcentagem_soja1=input('Qual porcentagem do soja:')
porcentagem_nucleo1=input('Qual porcentagem do nucleo vitaminico:')

#Para cada mistura, o programa deve pedir os valores de porcentagem dos três ingredientes.

Mistura_aprovadas=0
Mistura_reprovadas=0


#for=Para cada M=mistura in=dentro Range=intervalo 
for m in range(Teste_Raçoes):
 print(f'Mistura {m+1}')
 milho=input('Porcentagem de milho:')
 soja=input('Porcentagem de soja:')
 nucleo=input('Porcentagem de nucleo:')

 if porcentagem_milho1==milho and porcentagem_soja1==soja and porcentagem_nucleo1==nucleo:
    print('Mistura Aprovada')
    Mistura_aprovadas+=1

 else:
     print('Mistura REPROVADA')
     Mistura_reprovadas+=1

print(f'A quantidade de mistura aprovadas e de {Mistura_aprovadas}')
print(f'A quantidade de mistura reprovadas e de {Mistura_reprovadas}')
