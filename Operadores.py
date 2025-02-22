#REALIZANDO UMA OPERAÇAO DE SOMA
idades_leo=int(input('Digite a idade do leo: '))


#IREMOS CONVERTER O DADO INSERIDO PARA NUMERO INTEIRO
idade_Alvaro=int(input('Digite a idade alvaro: '))


idades_somadas=idades_leo+idade_Alvaro
print(f'As idades somadas possuem o valor de {idades_somadas}!')

print(type(idades_somadas))
      
      #REALIZANDO UMA SUBTRAÇAO

idades_subtracao=idade_Alvaro-idades_leo
print(f'As idades subtraidas possuem o valor de {idades_subtracao}!')

#REALIZANDO UMA MULTIPLICAÇAO

idades_multiplicadas=idades_leo*idade_Alvaro
print(f'As idades multiplicadas possuem o valor de {idades_multiplicadas}!')

#REALIZANDO UMA DIVISAO

idades_divididas=idades_leo/idade_Alvaro
print(f'As idades divididas possuem o valor de {idades_divididas}!')

#REALIZANDO UMA OPERAÇAO RESTO

idades_resto = idades_leo % idade_Alvaro
print(f'O resto entre as idades possuem o valor de {idades_resto}!')