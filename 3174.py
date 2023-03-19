n = int(input())
total = 0
buneco = 0
for i in range(n):
    nome, grupo, horas = input().split()
    horas = int(horas)
    if grupo == 'bonecos':
        
        b = horas // 8
        a = horas % 8
        buneco += a
        total += b
    elif grupo == 'arquitetos':
        b = horas // 4
        total += b
    elif grupo == 'musicos':
        b = horas // 6
        total += b
    elif grupo == 'desenhistas':
        b = horas // 12
        total += b

div = buneco // 8
total += div
print(total)
    
        
        
    