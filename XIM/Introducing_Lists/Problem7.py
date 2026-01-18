"""Think of at least five places in the world you’d like to visit.
a. Store the locations in a list. Make sure the list is not in alphabetical order.
b. Print your list in its original order. Don’t worry about printing the list
neatly, just print it as a raw Python list.
c. Use sorted() to print your list in alphabetical order without modifying the
actual list.
d. Show that your list is still in its original order by printing it.
e. Use sorted() to print your list in reverse alphabetical order without
changing the order of the original list.
f. Show that your list is still in its original order by printing it again.
g. Use reverse() to change the order of your list. Print the list to show that its
order has changed.
h. Use reverse() to change the order of your list again. Print the list to show it’s
back to its original order.
i. Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
j. Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed."""

locations = ['Paris', 'New York', 'Edinburgh', 'Denmark', 'Amsterdam', 'Spain']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse = True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)