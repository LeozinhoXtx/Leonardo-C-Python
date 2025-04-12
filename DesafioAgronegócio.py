Automatizar=int(input('Quantas Fazendas iram automatizar o relaatorio?:'))

print('Para cada fazenda solicite')
input('O Nome da fazenda:')
input('O Nome do responsavel:')
input('O Tipo de grão colhido:')
input('A Quantidade colhida(em toneladas):')

for f in range(Automatizar):
    input(f"Dados Da Fazenda:{f+1}")
    
    Fazenda=input('Fazenda:')
    Resultado_1=Fazenda.center(30,'*')
    print(Resultado_1)

    responsavel=input('Responsavel:')
    depois_1=responsavel.title()
    print(depois_1)

    Grão=input('Grao:')
    maiuscula=Grão.upper()
    print(maiuscula)

    Quantiades=input('Quantidade Colhida:')
    print(f'{Quantiades:,}')
  
    

   

   








