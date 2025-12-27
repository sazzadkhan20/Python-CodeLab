list1 = ['Dragon','Mango','Licchi']
fruits = ['Banna','Graps','Orange',list1,'Apple']
print(fruits[2])
print(fruits[3][2])
fruits[3][2] = 'Guava'
print(fruits[3][2])
# fruits.remove("Apple")
# fruits.append("cherry")
# fruits.pop(1)
# del fruits[0:2]
fruits.insert(2,'Malta')
fruits.remove(list1)
fruits.sort()
veg = ['Alu','Tomato']
fruits = fruits + veg
print(fruits)