jogos={
    'Minecraft':{'preço':59.90,'estoque':5},
    'Fifa23':{'preço':199.90,'estoque':3},
    'God of war':{'preço':149.90,'estoque':4},
}

#Mostre todos os jogos disponiveis , valores e estoque
for k , v in jogos.items():
    print(f'{k}- R${v['preço']} - {(v['estoque'])}unidades em estoque')

print('-'*60)

escolha_jogo=input('Qual jogo voce deseja?').strip().capitalize()

if escolha_jogo in jogos.keys():
     print('TEMOS EM NOSSO CONTROLE!')
     qtdade_solicitada=input('Quantos jogos você deseja comprar?')
     if qtdade_solicitada <= 
         print('Temos estoque disponivel')


    
else:
    print('NÃO TEMOS EM NOSSO CONTROLE')
    



  
