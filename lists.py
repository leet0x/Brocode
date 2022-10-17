# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti"]


food[0] = "sushi"

# food.append("icecream")
# food.remove("hamburger")
# food.pop()
food.insert(1, "salad")
food.sort()
food.clear()


for item in food:
    print(item)

