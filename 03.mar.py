# 88

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3  
# 2 2  
# 1 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end = " ")
    print()



# 89

# 5 4 3 2 1  
# 5 4 3 2 
# 5 4 3 
# 5 4  
# 5 

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j , end =" ")
    print()



# 90

# 5  
# 5 4  
# 5 4 3  
# 5 4 3 2 
# 5 4 3 2 1 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j ,end = " ")
    print()



# 91

# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3  
#       4 4  
#         5 

for i in range(1,6):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(i,6):
        print(i, end = " ")
    print()



# 92

# 1 2 3 4 5  
#   1 2 3 4 
#     1 2 3  
#       1 2
#         1

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ", end =" ")
    for j in range(1,i+1):
        print(j, end = " ")
    print()



# 93

# 1 2 3 4 5  
#   2 3 4 5 
#     3 4 5  
#       4 5 
#         5 

for i in range(1,6):
    for k in range(i-1):
        print(" ", end =" ")
    for j in range(i,6):
        print(j, end =" ")
    print()
