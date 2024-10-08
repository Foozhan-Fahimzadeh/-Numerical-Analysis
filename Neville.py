#Foozhan Fahimzade 400442306
def neville(x, y, target):
    n = len(x)
    result = [0] * n
    for i in range(n):
        result[i] = y[i]
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            result[j] = ((target - x[j-i]) * result[j] - (target - x[j]) * result[j-1]) / (x[j] - x[j-i])
    return result[n-1]

a = []
b = []
n = int(input())
for i in range(n):
    a.append(int(input("x[{i}]".format(i = i+1))))
    b.append(int(input("y[{i}]".format(i = i+1))))
val = int(input())
print(neville(a, b, val))