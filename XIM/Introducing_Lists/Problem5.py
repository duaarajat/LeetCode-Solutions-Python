"""You just found a bigger dinner table, so now more space is available. Think of three
more guests to invite to dinner.
a. Start with your program from Q. No. 3 or Q. No. 4. Add a print statement to
the end of your program informing people that you found a bigger dinner
table.
b. Use insert() to add one new guest to the beginning of your list.
c. Use insert() to add one new guest to the middle of your list.
d. Use append() to add one new guest to the end of your list. Print a new set of
invitation messages, one for each person in your list.
"""
people = ['Rani', 'Shashi', 'Mrs. Francis']
address = """The Ridge
Near Mall Road
Shimla, Himachal Pradesh"""

print("We have been able to now successfully book a bigger table hence our invitation list is now extended to three more guests\n")
people.insert(0,'Eleanor Roosevelt')
people.insert(1, 'Bell Hooks')
people.append('Barbara')

for person in people:
    print(f"Hello {person}!")
    print(f"Please accept this dinner request to 'Goofa Ashiana Restaurant', \n{address}\nOn 25th December, 2025\n")

print(people)