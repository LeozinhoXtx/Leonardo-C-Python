loja_games={
    'Minecraft':{'Preço':59.90,'Estoque':5},
    'Fifa23':{'Preço':199.90,'Estoque':3},
    'God of war':{'Preço':149.90,'Estoque':4},
}

#Criando dicionário de carrinho vazio
carrinho={}

#Mostre todos os jogos disponiveis , valores e estoque
for jogos , infors in loja_games.items():
    print(f'{jogos} - R${infors['Preço']} - {(infors['Estoque'])} unidades em estoque')

print('-'*60)



while True:
    escolha_jogo=input('Qual jogo voce deseja? (Digite "sair" para finalizar)').strip().capitalize()#Escolha do jogo pelo usuário
    if escolha_jogo.lower() == 'sair': #Usando .lower() pra deixar a saida da palavra tudo minuscula
        break #Ele irá para o laço caso o usuario digite sair

    if escolha_jogo in loja_games:#Verificamos se o jogo escolhido existia no dicionario principal lojas_games
        qtdad_compra=int(input('Quantas unidades você quer comprar?'))
        infors_games=loja_games[escolha_jogo]#Criamos um dicionario que recebe exclusivamente as informações do jogo escolhido
        if qtdad_compra <= infors_games['Estoque']: #Verificando o estoque do jogo escolhido
                loja_games[escolha_jogo]['Estoque'] -= qtdad_compra
                if escolha_jogo in carrinho:#Criando uma condicional para ver se o jogo esolhido ,ja foi adicionado no carrinho
                     carrinho[escolha_jogo] += qtdad_compra #Se sim, vou somar a nova compra com qtidades anteriores 
                else:
                     carrinho[escolha_jogo] = qtdad_compra
                print(f'Carrinho: {qtdad_compra} unidades adicionadas do jogo {escolha_jogo}')
        else:#cenário quando não há estoque do jogo escolhido
                print(f'Não tem estoque suficiente de {escolha_jogo}!')
    else:
         print(f'Jogo não encontrado! Passe aqui semana que vem!')

total=0
print('RESUMO DA COMPRA'.center(40,'-'))
for jogo, qtd in carrinho.items():
     preço= loja_games[jogo]['Preço']
     total += preço*qtd
     print(f'{jogo} x {qtd}'.center(40))
print(f'Total: R$ {total}'.center(40))












































































  
