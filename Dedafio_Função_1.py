#FUNÇÃO MAIN() =Boa prática que ajuda a organizar e controlar a xecuçao do código,especialmente em projetos maiores e reutilizáveis


#Funçao e metodos

def calcular_média(lista_de_notas):
    media = sum(lista_de_notas) / len(lista_de_notas) #sum somando total de notas  #len que retorna numero de elementos dentro da lista
    return media


def avaliar_aluno(nome, media_notas):

    if media_notas >= 9 and media_notas <=10:
        print(f'Parabéns, {nome}! Excelente desempenho')            

    elif media_notas >= 7 and media_notas <=8.9:
        print(f'Muito bem, {nome}! Você está indo bem')

    elif media_notas >= 5 and media_notas <= 6.9:
        print(f'Atenção,{nome}! Você precisa se dedicar mais.')

    else:
        print(f'Força,{nome}! Vamos estudar juntos!')        

    #Fim das funçoes e metodos


#FUNÇÃO PRINCIPAL QUE UTILIZA AS FUNÇÕES DE SUPORTE

def main():
    lista_notas = []
    while True:
        nota = float(input("Digite a nota ('999' pra finalizar): ")) #FLOAT = Converte pra Decimal
        if nota == 999:
            break
        else:
            lista_notas.append(nota)

    media_aluno = calcular_média(lista_notas)
    nome_aluno = input("Digite o nome do aluno: ")

    avaliar_aluno(nome_aluno, media_aluno)

if __name__ == "__main__": #EXECUÇÃO PRINCIPAL  
    main()








