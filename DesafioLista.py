Arenas=[
    [1200,1500,1100,1800,1700],
    [1000,950,1100,1050,980],    
    [2000,1900,1950,2100,2200]   
]

Media_Arenas=[]
numero_arena=0


for a in Arenas:
    numero_arena += 1  
    Media=sum(a) / len(a)
    Media_Arenas.append(Media)
    print(f'Média da Arena {numero_arena} :{Media}')
     
Maior_pontuaçao=max(Media_Arenas)
print(f'A Arena com melhor desempenho:Arena {Media_Arenas.index(Maior_pontuaçao)+1}')



    