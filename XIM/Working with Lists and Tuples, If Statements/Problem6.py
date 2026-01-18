"""Create a list to store numbers 0 to 20 with a common difference of 0.5. Create another list to
store numbers 0 to 20 with a common difference of 1.
a. Check if the number 4.5 is present in both the list using if statement without for
loop.
b. Print the common numbers from both the list using only one for loop.
c. Remove all the items from the second list and check if it is empty by not using any
operator."""

list1 = list(number*0.5 for number in range(41))
list2 = list(range(0,21))
if 4.5 in list1:
    print("4.5 is present in list 1")
if 4.5 in list2:
    print("4.5 is present in list 2")

for number in list2:
    if number in list2:
        print(number)

list2.clear()
if list2:
    print("Not empty")
else:
    print("Empty")