Arenas=[
    [1200,1500,1100,1800,1700],
    [1000,950,1100,1050,980],    
    [2000,1900,1950,2100,2200]   
]

Media_Arenas=[]

for a in Arenas:
    Soma=sum(a) / len(a)
    Media_Arenas.append(Soma)
    print(f'Média da Arena :{Soma}')
     
Maior_pontuaçao=max(Media_Arenas)
print(f'A Arena com melhor desempenho:Arena {Media_Arenas.index(Maior_pontuaçao)}')
    

    
    