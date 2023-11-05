animals = ["cow", "donkey", "rabbit", "horse"]

#to append to the list
animals.append("Leopard")
animals.append("Lion")
print(animals)

#to retrieve items by indices and slice
print(animals[0:3])
print(animals[2])
print(animals[:3]) #Print from item 0 to 2 but not including 3
print(animals[::2]) #step Jump by 1
print(animals[::1]) #print all the items
print(animals[::-1]) #print the whole list backwards
print(animals[::-2]) #print the list backwards jumping by 1

#To perform additions to the List
prime = [2,4,5,6,8,7]

print(sum(prime))

