def patterns(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end =" ")
        print("\n")

for _ in range(int(input("Enter no.of times: "))):
    n = int(input("Enter value of n: "))
    patterns(n)

output:
Enter no.of times: 1
Enter value of n: 5
1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 
