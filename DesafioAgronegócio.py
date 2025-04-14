
#            DESAFIO     AGRONEGOCIO 



Automatizar=int(input('Quantas Fazendas iram automatizar o relatorio?:'))

print('Para cada Relatorio.')
print(f'-'*20)
input('Digite o nome da fazenda:')
input('Digite o nome do responsavel:')
input('Digite o tipo de grão:')
input('Digite a quantidade colhida(em toneladas):')




for f in range(Automatizar):
    input(f"Dados Da Fazenda:{f+1}")

    
    Fazenda=input('Fazenda:')
    Resultado_fazenda=Fazenda.center(30,'*')
    print(Resultado_fazenda)

    
    responsavel=input('Responsavel:')
    resul_responsavel=responsavel.title()
    print(resul_responsavel)

    

    Grão=input('Grao:')
    maiuscula=Grão.upper()
    print(maiuscula)

    Quantidades=int(input('Quantidade Colhida:'))
    print(f"Valor formatado: {Quantidades:,.2f}")





Safra=1000


if Quantidades > Safra:
    print("Status:Excenlente safra!")


else:
    print("Status:Produçao dentro da média!")


  
    

   

   








