estoque=(
    ('Mouse LG Tech',10),
    ('Mic Hyper X',5),
    ('Acer Nitro 5',3),
    ('Webcam HD',0)
)

print('Produtos com menos de 5 unidades')

for i in estoque:
    if i[1] < 5:
        print(f'-{i[0]}')


contador=0

for i  in estoque:
    if i[1] == 0:
        contador +=1 
print(f'Produtos esgotados:{contador}')

soma_item=0

for i in estoque:
    soma_item += i[1]
print(f'Total Geral de Itens no Estoque:{soma_item}')









