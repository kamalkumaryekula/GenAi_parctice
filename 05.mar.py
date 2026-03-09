#  Write a program read a string and print the occurrences of each character. 
s = input("Enter a string: ")
# without using dictionary.
for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
    print(f"{i}: {count}")


# Accept a string and find the total vowels and consonants. Use two functions.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowel_count = count_vowels(string)
consonant_count = count_consonants(string)

print(f"Total vowels: {vowel_count}")
print(f"Total consonants: {consonant_count}")
