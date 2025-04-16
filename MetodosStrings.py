frase='leOnarDo tEm 26 Anos'

#Metodo CAPITALIZE =Ele ddeixa primeira letra da frase maiuscula,o resto minuscula
print(frase.capitalize())

#Metodo TITLE=Ele deixa a primeira letra de todas palavra em maiuscula,e as demais ficam minuscula
print(frase.title())

#Metodo CENTER(CENTRALIZAR) =Ele centraliza uma palavra de acordo com a quantidades e caracter especificado
print(frase.center(50,'_'))

#Bem usado: USADOS=Metodo LEN= Ele conta o numero de caracteres dentro de uma frase
print(len(frase)) 

#Metodo UPPER=Ele deixa toda a frase em letra MAIUSCULA
print(frase.upper())

#Metodo lower=Ele deixa toda a frase em letra minuscula
print(frase.lower())

#Metodo FIND=Ele retorna a posiçao da primeira letra da palavra destacada
print(frase.find('Anos'))
#Tem metodos q precisa de parametro e  tem metodo q nao precisa de parametro

#Metodo REPLACE=Ele substitui uma palavra ou caracter antiga por uma palavra ou caracter nova
print(frase.replace('Anos','celulares'))

#Metodo ISALNUM=Ele identifica dentro de uma frase se ela possui numeros OU letras,ele retorna um boleano(true ou false)

#CriandoSenha=input('Crie sua senha: ')
#validador=CriandoSenha.isalnum()
#print(validador)

#if validador is True:
    #print('Senha com Sucesso')
#else:
    #print('Algo de errado aconteceu,Refaça a sua senha')

#Metodo Ele identifica dentro de uma frase se ela possui SO numeros 

#CriandoSenha=input('Crie sua senha: ')
#validador=CriandoSenha.isdigit()
#print(validador)

#if validador is True:
    #print('Senha com Sucesso')
#else:
    #print('Algo de errado aconteceu,Refaça a sua senha')


#Metodo STRIP=Ele remove espaços das extremidades de uma frase
#Frase2="    Leonardo   "
#print(Frase2.strip())

Frase3= '   sou aluno do alvaro'
formatado= Frase3.strip().capitalize().replace('alvaro','Galileu')
print(formatado)



