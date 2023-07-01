
# 1 Hello, World!: Write a Python program that prints "Hello, World!" to the console.

print("Hello World")



# 2 Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

# integer
num=10

#float
pi=2.23

# string
name="Shubham Kumar"

# boolean
is_true=True

# list
my_list = [1,2,3,4,5]

# typle
my_tuple=(5,3,5,6)


# dictionary
my_dict={"apple":3 ,"banana":5, "orange":2}

# set
my_set={1,2,3,4,5}


# Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.


number = list(range(1,11))

number.remove(10)
number.append(20)
number.append(10)

number.sort()

print(number)




# Write a Python program that calculates and prints the sum and average of a list of numbers.

number = [10,20,30,40]

sum_of_number=sum(number)

avg_of_number=sum_of_number/len(number)

# print("sum:",sum_of_number, ", Average:",avg_of_number)



# Write a Python function that takes a string and returns the string in reverse order.

def reverse_string(s):
  reverse_string=""
  for char in s:
   reverse_string=char+reverse_string
  return reverse_string


ans=reverse_string("python")
# print(ans)



# Write a Python program that counts the number of vowels in a given string.

def count (s):
  vowels="aeiouAEIOU"
  c=0
  
  for char in s:
   if char in vowels:
     c+=1

  return c




# print("number of vowels:", count("shubham") )



# Write a Python function that checks whether a given number is a prime number.

def is_prime(n):
  if n<=1:
    return False
  
  for i in range(2, int(n ** 0.5)+1):
    if n%i==0:
      return False

  return True

num=18
if is_prime(num):
  print(num,"is a prime number")
else:
  print(num,"not a prime number")



# Write a Python function that calculates the factorial of a number.

def fac(n):
  if n<0:
    return None
  elif n==0:
    return 1
  else:
    result=1
    for i in range(1, n+1):
      result*=i
      return result


print(fac(3))


# Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    sequence = []

    # Check if n is valid
    if n <= 0:
        return sequence

    # Generate the Fibonacci sequence
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)

    return sequence

count = 10
fib_sequence = fibonacci(count)
print("Fibonacci sequence of", count, "numbers:", fib_sequence)


# Use list comprehension to create a list of the squares of the numbers from 1 to 10.

squares = [num ** 2 for num in range(1, 11)]
print(squares)