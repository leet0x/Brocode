# set = collection which is unordered, unindexed and no duplicate values


utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "knife", "cup"}
utensils.add("napkin")
# for x in utensils:
#     print(x)
    
# utensils.remove("fork")

# for x in utensils:
#     print(x)

# utensils.clear()

# for x in utensils:
#     print(x)

dishes.update(utensils)

for x in dishes:
    print(x)