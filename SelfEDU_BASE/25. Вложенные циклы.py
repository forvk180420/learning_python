for i in range(1, 4):
    for j in range(1, 6):
        print(f'i = {i}, j = {j};', end=' ')
    print()
# Результат:
# i = 1, j = 1; i = 1, j = 2; i = 1, j = 3; i = 1, j = 4; i = 1, j = 5;
# i = 2, j = 1; i = 2, j = 2; i = 2, j = 3; i = 2, j = 4; i = 2, j = 5;
# i = 3, j = 1; i = 3, j = 2; i = 3, j = 3; i = 3, j = 4; i = 3, j = 5;

a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []
# for row in a:
#     print(row, type(row))
#     for x in row:
#         print(x, type(x), end=' ')
#     print()
"""Проссумируем списки a и b"""
for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j]) 
    c.append(r)
print(c)  # [[2, 3, 4, 5], [4, 5, 6, 7], [6, 7, 8, 9]]

print('-------------')
"""Транспонирование таблицы"""
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
trans = []
for i in range(len(A)):
    rl = []
    for j in range(len(A[i])):
        rl.append(A[j][i])
    trans.append(rl)
    # A[i][j], A[j][i] = A[j][i], A[i][j]
print(f'tn = {trans}')  # tn = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]

print('-------------')
for r in A:
    for x in r:
        print(x, end='\t')
    print()
# Результат:
# 1	2	3	4
# 5	6	7	8
# 9	10	11	12
# 13	14	15	16
