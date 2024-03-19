

print(max(11))
print(min(11))
11 = [6, 8, 9, "p", "u"]
print(max(11)) #--> error coz its a combination of int and string
print(min(11)) #--> error coz its a combination of int and string

11 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
print(min(11)) #-5

11 [6, 7, 8, 9, 8, 8.89, -5, 0.78]
# index()-> to get index value of specific element
print(11.index(9))

11 = [6,6,6, 7, 8, 9, 8, 8.89, -5, 0.78]
#count()-> how many num of times an element is repeated
print(11.count(6))

#! some functions which is specifically used for list

 To add element inside list
? insert(index_value, element)---> to add element at specific index position
11 = [6,6,6, 7, 8, 9, 8, 8.89, -5, 0.78]
11.insert(2, "cars")
print(11)

# ? To delete element from list
11 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
pop() ---> last element will be deleted
11.pop()
print(11)


#* clear() --> to complete delete all element in list
11.clear()
print(11)
del to delete the list
del 11 #or del(11)
print(11)

# ? ----> Join 2 lists
11 = [9, 0, 8]
12 = ["p", "o", "t", 34]
print(11+12)


S1 = how are you
iam fine
hey there
# # * splilines()-> used to split the string hased on lines
print(s1.splitlines())

#* finds to find the index based on a charachter
s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))

#* join() -->
11 = ["hey", "there"]
print(" ".join(11))
print("$".join(11))


s1 = "Welcome to all"
*print(sl.endswith('1'))
*print(sl.startswith('W'))

s1 = "67"
print(type(s1))
print(s1.isdigit())


words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

space = 0
for val in s1:
    if val ==" ":
       space=space+1
print(space)






