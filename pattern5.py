#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

n=int(input())

#outer loop for rows
for i in range(1,n+1):
    
    #inner loop for columns
    for j in range(1,n+1):
        print(j,end=" ")

    print()
