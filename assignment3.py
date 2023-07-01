# Tuple Unpacking: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
data = [("John", 25), ("Jane", 30)]

for name, age in data:
    print(f"{name} is {age} years old.")


# Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary