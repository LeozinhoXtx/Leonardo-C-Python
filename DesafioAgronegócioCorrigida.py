QtdadeFazendas=3


for f in range(QtdadeFazendas):
    print('-'*40)
    nomefazenda=input(f'Digite o nome da fazenda {f+1}:')
    nomeresponsavel=input(f'Digite o nome do responsavel {f+1}:')
    tipograo=input(f'Digite o tipo de grão {f+1}:')
    qtdade=int(input(f'Digite a quantidade colhida(em toneladas) {f+1}:'))


    print('-'*40)
    print('Relatorio'.center(40))
    print('-'*40)

    print(nomefazenda.center(30,'*'))

    print(f'O responsavel da fazenda é:{nomeresponsavel.title()}')
    print(f'O tipo de grão é:{tipograo.upper()}')
    print(f'A quantidades em toneladas é:{qtdade:,.2f}')

    if qtdade > 1000:
        print('STATUS:Excelente Safra!')

    else:
        print('STATUS:Produção dentro da média!')