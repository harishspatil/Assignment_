#Python program to count the number of even and odd numbers from a series of numbers.
S = (2, 33, 45, 88, 77, 98, 54, 0, 17)
even_count = 0
odd_count = 0

for i in range(len(S)):
    if(S[i] % 2 == 0):
        even_count += 1
    else:
        odd_count +=  1

print("The count of even numbers in S = ", even_count)
print("The count of odd  numbers in S = ", odd_count)