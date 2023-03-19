dodo, leo, pepper = input().split()


if dodo == 'papel' and leo == 'pedra' and pepper == 'pedra':
    print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
    
elif dodo == 'papel' and leo == 'tesoura' and pepper == 'papel':
    print("Iron Maiden's gonna get you, no matter how far!")

elif dodo == 'pedra' and leo == 'pedra' and pepper == 'papel':
    print("Urano perdeu algo muito precioso...")
else:
    print("Putz vei, o Leo ta demorando muito pra jogar...")