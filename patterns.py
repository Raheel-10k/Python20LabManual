n=int(input("Enter the no. : "))
#PATTERN 1
for i in range (1,n+1,1):
    for j in range(i):
        print(" * ",end=" ")
    print(" ")
print("\n\n\n")  #For distinction of differnet patterns
#PATTERN 2
for i in range (1,n+1,1):
    for j in range(i):
        print( i ,end=" ")
    print(" ")
print("\n\n\n") #For distinction of differnet patterns
#PATTERN 3
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print("")   #change in line