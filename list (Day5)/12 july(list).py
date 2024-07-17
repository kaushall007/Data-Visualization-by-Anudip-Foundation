#list creation

#print the element in backward direction using forward index

list1 = [20,10,20,20,98,82,22,100,28,4,21,4,5,13,43,67,88,10,27,99]
print("List element in before backward direction",list1)
print(" ")
print("----------------------------------------------------------------------------------------------")
print("List element in backward direction using Slicing",list1[: :-1])
print("---------------------------------------------------------------------------------------------")


#using for loop
print("List element in backward direction using  Iteration")
for i in range(len(list1)-1, -1, -1):
    print(list1[i],end="  ")

 
