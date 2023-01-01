# key : value
pets = {
    "name": "Bubba",
    "age": 11,
    "is_good_boy": "Sometimes"}

print(pets["name"])
print(pets["age"])

pets["age"]+= 1

print(pets["age"])

pets["quiet"] = "If it's not dinner"

print(pets["quiet"])

key_to_create = "counter"

pets[key_to_create] = 1
pets[key_to_create] = pets[key_to_create] + 1

print(pets[key_to_create])

print("-" * 50)

for toast, moreToast in pets.items():
    print(toast, moreToast)