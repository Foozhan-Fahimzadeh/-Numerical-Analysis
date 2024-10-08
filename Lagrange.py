#Foozhan Fahimzade 400442306
x = []
y = []
def daroonyab(x, y, xi, n):
    sum = 0
    for i in range(n):
        c = y[i]
        for j in range(n):
            if j!=i:
                c = c*(xi - x[j])/(x[i] - x[j])
        sum += c
    return sum


n = int(input())

for i in range(n):
    a = int(input("x[{i}]".format(i=i+1)))
    x.append(a)
    b = int(input("y[{i}]".format(i=i+1)))
    y.append(b)

z = int(input())
print("Value of f(", z,") is : " , daroonyab(x, y, z, n))


