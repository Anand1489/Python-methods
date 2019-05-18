list_first = [1, 2, 3]

# indexing and slicing of list
print(list_first[2])
print(list_first[-1])
print(list_first[1:])
print(list_first[1:2])

# concatenate list
print(list_first + [1, 2, 3])

# nested list
list_first[1] = [4]
print(list_first)

# to change value of 1st index to show list is mutable
list_first[1] = 4
print(list_first)

# appending with list
list_first.append(6)
print(list_first)

# built-in function len()
print(len(list_first))

# nested list example
list_second = [9, 8, 7, 6]
list_mix = [list_first, list_second]
print(list_mix)

# -----------------------------------------------------------------------------------------------------------------------

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# appending one more value to list named fruits
fruits.append('grape')
print(fruits)
# removing list value from list
fruits.remove('pear')
print(fruits)
if 'mango' in fruits:
    fruits.remove('mango')
print(fruits)

# insert method of list
fruits.insert(2, 'mango')
print(fruits)

# to check index use index method
print(fruits.index('banana'))

# always includes starting position as well and check index in below syntax if there are multiple values in a list
print(fruits.index('apple', 2))

# counts values in a list
print(fruits.count('apple'))

# creates copy of same list but id of both list will be different
fruits_copy = fruits.copy()
print(id(fruits))
print(id(fruits_copy))

# reverse method reverses list in descending order
fruits_copy.reverse()
print(fruits_copy)

# sort along with reverse i.e. descending order
fruits_copy.sort(reverse=True)
print(fruits_copy)

# list.pop(i)
# Remove the item at the given position in the list, and return it. If no index is specified,
# a.pop() removes and returns the last item in the list. (The square brackets around the i in
# the method signature denote that the parameter is optional, not that you should type square
# brackets at that position.)
fruits = ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.pop()
print(fruits)
# to remove 2nd element from list using pop method
fruits.pop(2)
print(fruits)

# sorting with key along with function
def sort_after(tup):
    return tup[2]

before_sort = [(5, 3, 3), (4, 3, 3), (2, 4, 5)]
before_sort.sort(reverse=True,key=sort_after)
print(before_sort)

'''
List Comprehensions.
    List comprehensions provide a concise way to create lists. Common applications are to make new
    lists where each element is the result of some operations applied to each member of another
    sequence or iterable, or to create a subsequence of those elements that satisfy a certain
    condition.
    A list comprehension consists of brackets containing an expression followed by a for clause,
    then zero or more for or if clauses. The result will be a new list resulting from evaluating
    the expression in the context of the for and if clauses which follow it.
'''
fruits = ['grape', 'orange', 'apple', 'apear', 'banana', 'kiwi', 'apple', 'banana']
list_first_a_start=[name+'add' for name in fruits]

print(list_first_a_start)

# to change string from immutable to mutable using same variable name
name = "ananad"
name = name + "pillai"
print(name)


# zip function forms a tuple with transpose of matrices
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
print(list(zip(*matrix)))


print(bool(3))



# Python program to find the factorial of a number provided by the user.


num = 10
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
       print(i)
   print("The factorial of",num,"is",factorial)