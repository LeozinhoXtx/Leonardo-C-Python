
composiçao_raçoes = {'R73' : [{'Ingrediente1' : 0.5}, {'Ingrediente2' : 0.3}, {'Ingrediente3' : 0.2}]}
estoque_ingredientes =  [ {'Ingrediente1' : 100}, {'Ingrediente2' : 200},{'Ingrediente3' : 300} ]


#print(composiçao_raçoes['R73'][0]['Ingrediente1'])
#print(estoque_ingredientes[0]['ingrediente1'])

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
        consumo_i1= qtdade_consumida * composiçao_raçoes['R73'][0]['Ingrediente1']
        consumo_i2= qtdade_consumida * composiçao_raçoes['R73'][1]['Ingrediente2']
        consumo_i3= qtdade_consumida * composiçao_raçoes['R73'][2]['Ingrediente3']
        
        estoque_ingredientes[0]['Ingrediente1'] -= consumo_i1
        estoque_ingredientes[1]['Ingrediente2'] -= consumo_i2
        estoque_ingredientes[2]['Ingrediente3'] -= consumo_i3

        print('ESTOQUE ATUALIZADO'.center(40,'-'))
        for n in estoque_ingredientes:
            for dict_ingrediente in n:
                print(f'{dict_ingrediente} ------- {n[dict_ingrediente]}')

elif escolha_usuario == 2:
    qtdade_ingredientes = int(input("Digite a quantidade de ingredientes para lançar: "))
    for i in range(qtdade_ingredientes):
        tipo_ingrediente = input("Digite o ingrediente que será adicionado: ").capitalize()
        qtdade_adiconada = int(input("Digite a quantidade adicionada:"))
        for n in estoque_ingredientes:
            for dict_ingredient in n:
                if dict_ingredient == tipo_ingrediente:
                    n[dict_ingredient] += qtdade_adiconada

    print('ESTOQUE ATUALIZADO'.center(40,'-'))
    for n in estoque_ingredientes:
            for dict_ingrediente in n:
                print(f'{dict_ingrediente} ------- {n[dict_ingrediente]}')

else:
    print(f"ERRO - Digite 1 ou 2 para consumir ou Adicionar Estoque!".center(40))
    


