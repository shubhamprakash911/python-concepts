# Write a program to print the following number pattern using a loop.
for i in range(1, 6):

  for j in range(1, i + 1):
    print(j, end=" ")

  print()

# Write a program to display only those numbers from a list that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in range(len(numbers)):
  if numbers[i] > 500:
    break
  elif numbers[i] > 150:
    continue
  elif numbers[i] % 5 == 0:
    print(numbers[i])

# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "ault"
s2 = "kelly"

mid_ind = int(len(s1) / 2)

s3 = s1[:mid_ind] + s2 + s1[mid_ind:]
print(s3)

#Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "abCdE"
l = []
u = []

for i in range(len(str1)):
  if str1[i].islower():
    l.append(str1[i])
  else:
    u.append(str1[i])

print("".join(l + u))

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

ml = min(len(list1), len(list2))
ans = []

for i in range(ml):
  ans.append(list1[i] + list2[i])

if len(list1) > len(list2):
  ans += list1[ml:]
else:
  ans += list2[ml:]

print(ans)

# ### **Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:**
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

ans = []
l = ["Hello ", "take "]
l2 = ["Dear", "Sir"]

for i in range(len(l)):
  for j in range(len(l2)):
    ans.append(l[i] + l2[j])

print(ans)

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

l = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]

length = len(l2)
for i in range(len(l)):
  print(l[i], l2[length - 1 - i])

# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dic = {}

for i in range(len(employees)):
  dic[employees[i]] = defaults

print(dic)

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

s = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
k = ["name", "salary"]

dic = {}

for i in range(len(k)):
  dic[k[i]] = s[k[i]]

print(dic)

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

t = (11, [22, 33], 44, 55)
l = list(t)
l[1][0] = 222
t = tuple(l)
print(t)