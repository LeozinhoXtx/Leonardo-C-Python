notas=[
    ['Ana',[8,7,9]],
    ['Carlos',[5,6,7]],
    ['João',[10,9,8]]    
]
#O desafio deve imprimir nome do aluno e suas média de notas
for a in notas:
    print('_'*40)
    print(f'MÉDIA ALUNO {a[0]}'.upper().center(40,'_'))
    media_aluno=sum(a[1]) / len(a[1]) #linha mais importante
    print(f'{media_aluno}'.center(40,'_'))
    print('-'*40)

