"""You just found out that your new dinner table won’t arrive in time for the dinner,
and you have space for only two guests.
a. Start with your program from Q. No. 5. Add a new line that prints a message
saying that you can invite only two people for dinner.
b. Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
c. Print a message to each of the two people still on your list, letting them
know they’re still invited.
d. Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""

people = ['Eleanor Roosevelt', 'Rani', 'Bell Hooks', 'Shashi', 'Mrs. Francis', 'Barbara']
print("Due of the unavailability of required resources the guest list has to be cut short to only two guests now.\n")

while (len(people) != 2):
    name = people.pop()
    print(f"Dear {name}, we regret telling you that due to some arrangement issues we have to uninvite you from the dinner night.\n")

for person in people:
    print(f"\nDear {person}, we are delighted to let you know that you are still on our guest list")

del people[0]
del people[0]

print(people)
