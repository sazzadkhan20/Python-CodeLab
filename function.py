# def hello(name):
#     print(f"Hello, {name}!")
#     print("Hello, ",name)
#
# name = input("Enter a name : ")
# hello(name)

# def my_fun(*child):
#     print("The Oldest Children is: "+child[1])
#
# my_fun("Sazzad","Oni","Sadid")

# def my_fun(child1,child2,child3):
#     print("The Oldest Children is: "+child1)
#
# my_fun("Sazzad","Oni","Sadid")

#Default

# def my_fun(country = "Bangladesh"):
#     print("The Oldest Children is: "+country)
#
# my_fun()
# my_fun("India")

# def my_fun(food):
#     for i in food:
#         print("The Foods is: "+i)
#
# my_fun(['Apple','Orange','Banna'])

def my_fun(food):
    for i,j in food.items():
        print("The Foods is: "+j)

fruits = {
    "xyx" : "Apple",
    "abc" : "Banana"
};
my_fun(fruits)











