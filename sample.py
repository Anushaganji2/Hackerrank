n=int(input("n=")) #input
a = 1
b = 1
for i in range(n):
    for j in range(i+1):
        print(a, end="")
    print()
    c = a + b
    a = b
    b = c