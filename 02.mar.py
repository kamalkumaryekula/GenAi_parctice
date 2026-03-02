# 82

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10
k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k, end = " ")
        k+=1
    print()



# 83

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range(1,6):
    for j in range(1,i+1):
        print(j , end = " ")
    print()


# 84

# 1  
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5  5 

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end =" ")
    print()



# 85

# 1 
# 1 1  
# 1 2 1 
# 1 2 3 1 
# 1 2 3 4 1 
# 1 2 3 4 5 1 

for i in range(0,6):
    for j in range(1, i+1):
        print(j, end = " ")
    print(1)



# 86

# 1 2 3 4 5  
# 1 2 3 4 
# 1 2 3
# 1 2  
# 1 

for i in range(5,0,-1):
    for j in range(1, i+1):
        print(j , end = " ")
    print()



# 87

# 1 1 1 1 1 
# 2 2 2 2  
# 3 3 3  
# 4 4  
# 5 

for i in range(1,6):
    for j in range(i,6):
        print(i,end = " ")
    print()