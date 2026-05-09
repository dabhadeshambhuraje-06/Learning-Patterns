#*
#**
#***
#****
#*****
#****
#***
#**
#*
n = int(input())

#for normal pattern

for i in range(1,n+1):
    print("*"*i)

#for reverse pattern

for i in range(n-1,0,-1):
    print("*"*i)
