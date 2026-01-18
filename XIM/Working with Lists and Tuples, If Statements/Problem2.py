"""Use a for loop to print the numbers from 1 to 20, inclusive.
a. Use min() and max() to make sure your list actually starts at 1 and ends at 20. Use
sum() function to see the sum of the first 20 numbers.
b. Use the third argument of the range() function to make a list of the odd numbers
from 1 to 20. Use a for loop to print each number.
"""

numbers = list(range(1,21))
for number in numbers:
    print(number)

print(f"Minimum number from the list is : {min(numbers)}")
print(f"Maximum number from the list is : {max(numbers)}")
print(f"Sum of numbers from the list (1-20) is : {sum(numbers)}\n")

odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)