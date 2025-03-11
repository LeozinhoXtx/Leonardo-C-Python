
  #Neste momento estou cirando minha conta na plataforma
login = input('Crie seu login:')
senha =  input('Crie uma senha:')
  
#No dia seguinte ,pricisei informar o login e senha novamente na plataforma
login_tentativa = input('Bem vindo de volta! Voce foi deslogado,entre novamente! Digite seu usuario:')
senha_tentativa =input('Bem vindo de volta! Voce foi deslogado,entre novamente! Digite sua senha:')

#While(enquanto) as tentaivas de login ou senha forem diferentes,o bloco abaixo ira executar
while login != login_tentativa or senha != senha_tentativa:
    print('Login ou Senha incorretos .Por favor,tente mais uma vez')
    login_tentativa =input ('Digite o seu login')
    senha_tentativa = input('Digite sua senha:')

#If se o login and(E) senha estao corretos,usuarios conectado com sucesso
if login == login_tentativa and senha == senha_tentativa:
    print('Voce foi conectado com SUCESSO') 

#teste1: login correto e senha incorreta - validado
#teste2: login incorreto e senha correta - Validado
#teste3: login e senha incorretos - Validado
#teste4: login e senha Corretos - Validado



#or e para OU
#and é para e
#not in 'nao esta'




