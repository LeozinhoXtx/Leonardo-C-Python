#Validando posiçoes dentro de um texto

#Python inicia a contagem sempre em "ZERO"
 
Nome='Leonardo'
#imprimir posiçao 3 da strings(texto) que esta armazenado em nom
print (Nome [3])  #conta da esquerda pra direita
print(Nome [-5]) #conta da direita pra esquerda

#F-strings Representada pela letra f antes das aspas,onde pode-se utilizar {} para inserir variaveis,expressoes e metodos em alguma saida de do tipo texto
Idade=18
Ano=2025
print(f'A {'idade'} e {'Ano'}')

pi= 3.1456787899099756747489


print(f'O numero pi é de {pi}')
print(f'O numero pi com duas casas decimais é {pi:.2f}')


mega_sena=6690879776577490

print(f'Utilizando separdor para o premio da mega sena {mega_sena:,}') #Formatamos os milhares com um separador VIRGULA