
my_list = [7, 77, 28]
my_dict = {"name": "Sneha", "age": 21}
my_set = {20, 70, 177}

print("Original List:", my_list)

my_list.append(4)  
print("After Append:", my_list)

my_list.remove(77)  
print("After Remove:", my_list)

my_list[1] = 5  
print("After Modification:", my_list)


print("\nOriginal Dictionary:", my_dict)

my_dict["city"] = "New York"  
print("After Adding a Key-Value Pair:", my_dict)

del my_dict["age"] 
print("After Deleting a Key-Value Pair:", my_dict)

my_dict["name"] = "Bob"  
print("After Modifying a Value:", my_dict)


print("\nOriginal Set:", my_set)

my_set.add(40) 
print("After Adding an Element:", my_set)

my_set.remove(70) 
print("After Removing an Element:", my_set)

my_set.update([50, 60])  
print("After Adding Multiple Elements:", my_set)


print("\nFinal List:", my_list)
print("Final Dictionary:", my_dict)
print("Final Set:", my_set)
