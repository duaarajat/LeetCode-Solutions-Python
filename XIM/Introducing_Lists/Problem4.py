"""You just heard that one of your guests can’t make the dinner, so you need to send
out a new set of invitations. You’ll have to think of someone else to invite.
a. Start with your program from Q. No. 3. Add a print statement at the end of
your program stating the name of the guest who can’t make it.
b. Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
c. Print a second set of invitation messages, one for each person who is still in
your list.
"""
people = ['Rani', 'Shashi', 'Qais']
address = """The Ridge
Near Mall Road
Shimla, Himachal Pradesh"""

for person in people:
    print(f"Hello {person}!")
    print(f"Please accept this dinner request to 'Goofa Ashiana Restaurant', \n{address}\nOn 25th December, 2025\n")

print(f"Due to some unforeseen circumstances {people[2]}, wouldn't be able to accomapny us for the dinner night.")
people[2] = 'Mrs. Francis'
print("The new invitation list is : \n")


for person in people:
    print(f"Hello {person}!")
    print(f"Please accept the dinner invitation to 'Goofa Ashiana Restaurant', \n{address}\nOn 25th December, 2025\n")
