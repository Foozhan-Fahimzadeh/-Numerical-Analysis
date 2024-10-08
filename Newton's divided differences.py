#Foozhan Fahimzade 400442306
def divided_difference(x, y):
    n = len(x)
    F = [[0 for i in range(n)]
         for j in range(n)]
    for i in range(n):
        F[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    return F


def newton_interpolation(x, y, value):
    n = len(x)
    F = divided_difference(x, y)
    result = F[0][0]
    for i in range(1, n):
        term = F[0][i]
        for j in range(i):
            term *= (value - x[j])
        result += term
    return result


a = []
b = []
n = int(input())
for i in range(n):
    a.append(int(input("x[{i}]".format(i = i+1))))
    b.append(int(input("y[{i}]".format(i = i+1))))
val = int(input())
print(newton_interpolation(a, b, val))
