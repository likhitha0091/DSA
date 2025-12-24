def patterns(n):
    for i in range(n):
        for j in range(i):
            print("*", end =" ")
        print("\n")

for _ in range(int(input("Enter no.of times: "))):
    n = int(input("Enter value of n: "))
    patterns(n)
