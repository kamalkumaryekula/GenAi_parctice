# 51.write a program to display the numbers sequentially from 1 to 99 with 5 numbers on    
# each line. 
for i in range(1, 100):
    print(f"{i:2}", end=" ")
    if i % 5 == 0:
        print()

# output:

#  1  2  3  4  5 
#  6  7  8  9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 
# 21 22 23 24 25 
# 26 27 28 29 30 
# 31 32 33 34 35 
# 36 37 38 39 40 
# 41 42 43 44 45
# 46 47 48 49 50
# 51 52 53 54 55
# 56 57 58 59 60
# 61 62 63 64 65
# 66 67 68 69 70
# 71 72 73 74 75
# 76 77 78 79 80
# 81 82 83 84 85
# 86 87 88 89 90
# 91 92 93 94 95
# 96 97 98 99

# 52. write a program to display the numbers sequentially from 1 to 99 with 5 numbers on 
# each column. 
for i in range(1, 20):  
    for j in range(i, 100, 20):  
        print(f"{j:2}", end=" ")
    print()

# output:

#  1 21 41 61 81 
#  2 22 42 62 82
#  3 23 43 63 83
#  4 24 44 64 84
#  5 25 45 65 85
#  6 26 46 66 86
#  7 27 47 67 87
#  8 28 48 68 88
#  9 29 49 69 89
# 10 30 50 70 90
# 11 31 51 71 91
# 12 32 52 72 92
# 13 33 53 73 93
# 14 34 54 74 94
# 15 35 55 75 95
# 16 36 56 76 96
# 17 37 57 77 97
# 18 38 58 78 98
# 19 39 59 79 99


# 53.Write a program to read 9 elements and print the array elements in 3 x 3 matrix format. 
arr = []
print("Enter 9 elements:")
for _ in range(9):
    arr.append(int(input()))

print("\n3x3 Matrix:")
for i in range(0, 9, 3):
    print(arr[i], arr[i+1], arr[i+2])


# output:
# Enter 9 elements:
# 2
# 3
# 6
# 5
# 9
# 8
# 7
# 4
# 1

# 3x3 Matrix:
# 2 3 6
# 5 9 8
# 7 4 1

# 54. Write a program to display the multiplication table for a given number. 

num = int(input("Enter a number: "))
print(f"\nMultiplication Table for {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# output:

# Enter a number: 5
# Multiplication Table for 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50


