pagamento_cliente= input('O cliente deu o golpe? Responde S para sim e N para nao!')

if pagamento_cliente== 'N':     #Condicao para verificar a informaçao armazenada na variavel pagamento_cliente
    print('Ele e um bom cliente')  #Imprimir o resultado caso a condicao for verdadeira 
elif pagamento_cliente== "S":  #segunda cenario de condiçao, da pra colocar mais de um elif
    print('Ele e um mal cliente')n
else: #Caso contrario 
    print('Nao entendi sua resposta. Responda S para sim N para nao')