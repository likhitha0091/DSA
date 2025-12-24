def patterns(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end =" ")
        print("\n")

for _ in range(int(input("Enter no.of times: "))):
    n = int(input("Enter value of n: "))
    patterns(n)

output:
Enter no.of times: 1
Enter value of n: 5
* 

* * 

* * * 

* * * * 

* * * * * 
