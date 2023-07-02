# Tuple Unpacking: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
data = [("John", 25), ("Jane", 30)]

for name, age in data:
    print(f"{name} is {age} years old.")


# Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary


class Mani:
    def __init__(self):
        self.l=[]

    def add(self,n,a):
        obj={}
        obj[n]=a
        self.l.append(obj)

    def update_age(self,name,age):
        for i in range(len(self.l)):
            if name in self.l[i]:
                self.l[i][name]=age
                return
        print(f"{name} name is not in the list")


    def delete_name(self,name):
        for obj in self.l:
            if name in obj:
                del obj[name]
                return
        print(f"{name} is not in the list")




    


instance=Mani()
instance.add("ram",14)
instance.add("papa",29)
instance.update_age("papa",12)
instance.delete_name("papa")

print(instance.l)


#3
def twoSum(k,a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==k:
                print(i,j)
                return
        



a=[2,3,4,5,6]
twoSum(9,a)


# 4
def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()

    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return f"The word {word} is a palindrome."
    else:
        return f"The word {word} is not a palindrome."

# Test the function
word = "madam"
result = is_palindrome(word)
print(result)




#5
def selection_sort(arr):
    # Traverse through each element in the list
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Test the function
input_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(input_list)
print(sorted_list)





#6
from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.put(value)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.empty():
            return self.q1.get()

# Test the Stack class
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1











#7
for i in range(1,101):
    if i%3==0:
        print("Fizz")
    else:
        print(i)








#8
def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
        word_count = len(content.split())

    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Test the function
input_file = "input.txt"
output_file = "output.txt"
count_words(input_file, output_file)





#10
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function
num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
print(result)


