n = int(input('Введите число: '))
result = []
for i in range(1, n):
    for j in range(1, n):
        if n % (j + i) == 0 and j > i:
            result.append(i)
            result.append(j)
    if i == n // 2:
        break

print(''.join(map(str, result)))