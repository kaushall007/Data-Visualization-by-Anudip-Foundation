#Insert
'''my_list = ["Ram",10,"Shyam",11]
my_list.insert(4,"Megha") # insert(index,element)
print(my_list)
'''

#Append
'''
my_list = ["Ram",10,"Shyam",11,"Megha"]
my_list.append(12)
print(my_list)
'''
#Extend
'''
my_list = ["Ram",10,"Shyam",11,"Megha",12]
my_list.extend(["Mohit",12,"Rohan",11])
print(my_list)
'''

#find a method to insert all the element of another sequence datatype at particular index in the list,but all the element must be inserted one by one

my_list = [1, 2, 3, 4, 5]
other_seq = [6, 7, 8, 9]
index = 2
my_list = my_list[:index] + other_seq + my_list[index:]
print(my_list)


