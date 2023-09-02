friends = ["Kevin", "Karen", "Jim"]
#negative index starts from the end of the list
# friends[0]= "Joey" #replaces Kevin with Joey
lucky_numbers = [4, 8, 15, 16, 23, 42]
# print(friends[1])

#List Functions
#extend: adds a list to another list
friends.extend(lucky_numbers)
#append: adds a single element to the end of a list
friends.append("Creed")
#insert: adds an element to a specific index
friends.insert(1, "Kelly")
# print(friends)

#remove: removes an element from a list
friends.remove("Jim")
# print(friends)

# #clear: removes all elements from a list
friends.clear()
# print(friends)

#pop: removes the last element from a list
friends.pop()
# print(friends)

#index: returns the index of the first element with the specified value
# print(friends.index("Kevin"))

#count: returns the number times the element is shown in the list with the specified value
# print(friends.count("Jim"))

#sort: sorts the list in ascending order
lucky_numbers.sort()


#reverse: reverses the order of the list
lucky_numbers.reverse()

#copy: returns a copy of the list
friends2 = friends.copy()
print(friends2)

