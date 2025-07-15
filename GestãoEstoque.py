
composiçao_raçoes = {'R73' : [{'Ingrediente1' : 0.5}, {'Ingrediente2' : 0.3}, {'Ingrediente3' : 0.2}]}
estoque_ingredientes =  [ {'Ingrediente1' : 100}, {'Ingrediente2' : 200},{'Ingrediente3' : 300} ]


print(composiçao_raçoes['R73'][0]['Ingrediente1'])

print('LANÇAMENTO DE ESTOQUE'.center(50,'-'))
print(' 1 - Consumir \n 2 - Adcionar')
escolha_usuario = int(input('Escolha uma das opções (1 ou 2) : '))

if escolha_usuario == 1 :
    codigo_raçao = input('Digite qual ração foi consumida: ' .strip().upper())
    if codigo_raçao in composiçao_raçoes:
        print(f'\nComposiçao da ração {codigo_raçao}: ')
        for ingrediente_dict in composiçao_raçoes[codigo_raçao]:
            for ingrediente in ingrediente_dict:
                print(f'{ingrediente} _______ {ingrediente_dict[ingrediente]}') 
        print('-'*50)
        qtdade_consumida = int(input('Digite a quantidade consumida em KG: '))


