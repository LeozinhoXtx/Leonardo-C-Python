pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]
lista_Preços_itens_entregues= []

print("_"*20)
print("Produtos Entregues".center(20, ' '))
print("_"*20)
for t in pedidos:
    if t[3] == "Entregue":
        lista_Preços_itens_entregues.append(t[2])
        print(f'- {t[0]}')

print(f'Valor total do itens entregues: {sum(lista_Preços_itens_entregues)}')

print('Ultimos 3 pedidos:')
for p in pedidos [-3:]:
    print(f' - {p[0]}')

Vestuarios_cancelados = 0

for v in pedidos:
    if v[1] == "Vestuário" and v[3] == "Cancelado":
         Vestuarios_cancelados += 1

print(f'Cancelados da categoria "Vestuário": {Vestuarios_cancelados}')

Escolha_usuario=input("Digite uma categoria: ")

for p in pedidos:
    if Escolha_usuario ==  p[1]:
        print(p[0])






