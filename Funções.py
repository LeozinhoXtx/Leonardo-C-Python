#metodos acompanha um objeto (variavel,string,lista,tupla,dicionario)
#Função nao acompanha nenhum objeto
import random
#Criando uma função sem parametro e sem retorno

def boas_vindas():
    print('Bem-vindo ao Galileu!')#Código que será executado quando eu chamar a função boas_vindas

boas_vindas()#Chamando a função boas_vindas

#Criando função sem parametro e com retorno 
def numero_aleatorio_1_100():
    return print (random.randint(1,100))

numero_aleatorio_1_100()

#Criando uma funçao com parametro e com retorno
def soma_acumulada(a,b,c):
    return a + b + c

print(soma_acumulada(2, 3, 5))

#Criando uma função com parametro e sem retorno
def bem_vindo_customizado(nome):
    print(f'Seja muito bem-vindo {nome}')

bem_vindo_customizado('Beatriz')


def aplicando_descontos(valor,desconto):
    return valor-desconto

print(aplicando_descontos(100, 35))


def aplicando_descontos(valor,percentual_desconto):
    novo_valor= valor*(1-percentual_desconto)
    return print(novo_valor)

print(aplicando_descontos(100, 0.35))


senha= 'Bruce1999'

def verificaçao_senha():
    senha_tentativa=input('Digite sua senha!')
    while True:
        if senha == senha_tentativa:
            print('Senha correta')
            break
        else:
            print('Senha incorreta')
            senha_tentativa=input('Errou! Digite novamente sua senha:')

verificaçao_senha()





    