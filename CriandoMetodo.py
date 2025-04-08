#criar um sistema que recebe a idade de uma pessoa,e retorna se ela pode dirigir ou nao


#Metodo para avaliar se pessoa pode ou nao dirigir
def autorizaçao (idade):
    if idade < 18 :
     print("A pessoa nao pode dirigir")
    else:
       print("A pessoa pode dirigir")

idade_p1= int(input('Digite a idade da pessoa'))
autorizaçao(idade_p1)

#Metodo que cria um boletim ,recebendo como parametro o nome,materia e nota
def boletim (nome,materia,nota):
   print(f'-'*20)
   print(f'O nome do aluno é {nome}')
   print(f'A materia avaliada é {materia}')
   print(f'E sua nota é {nota}')
   print(f'-'*20)

boletim('Leonardo','Matematica',10)
boletim('Alvaro','quimica',2)