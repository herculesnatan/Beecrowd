num = int(input())
words = []
for i in range(num):
    word = input()
    read = len(word)
    if read <= 9:
        words.append(word)
    else:
        new_word = f'{word[0]}{read-2}{word[-1]}'
        words.append(new_word)
for w in words:
    print(w)
        
        