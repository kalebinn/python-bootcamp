my_first_list = [2, 4, 6, 8]
#print(my_first_list[0])

length = len(my_first_list)
#print("The length of the list is", length)

for index in range(0, len(my_first_list)):
    element = my_first_list[index]
    #print(element)

# you can use the print() function instead of a for loop
#print(my_first_list)

# error here
#my_first_list[4]


#print("Original list:",my_first_list)
my_first_list.append(10)
#print("List after append:",my_first_list)

# TODO: make a list of even numbers up to 12 (inclusive)
evens_list = []
for num in range(1,13):
    if num % 2 == 0:
        evens_list.append(num)

#print("List of even numbers up to 12",evens_list)
#evens_list.clear()
#print("List after using clear()", evens_list)

print("list before popping an element", evens_list)
for i in range(0,len(evens_list)-1):
    if evens_list[i] == 10:
        index_of_ten = i
        ten = evens_list.pop(i)

print("list after popping an element", evens_list)
print("the value of the variabl ten = ", ten)

evens_list.insert(index_of_ten, ten)
print("Using insert, to put the 10 back:", evens_list)

print(sorted(evens_list))




