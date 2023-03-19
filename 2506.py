num = int(input())
count = 0
for i in range(num):
    h, m, c = map(int,input().split())
    if m > c:
        count +=1
    elif m == 0 and c == 0:
        break

print(count)
    