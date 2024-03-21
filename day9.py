
# 2.) Find the uncommon words from 2 strings
s1 "Hello how are you"
s2 "Hello how is"

s1 "Hello how are you"
s2 "Hello how is"

sl = sl.split("")
s2 = s2.split("")

for val in st:
    if val not in s2:
       print(val)
       
for val in s2:
    if val not in s1:
       print(val)

# ? To use the variable inside the constructor in another methods
# class class1:
    # email "sid@gmail.com"        # static variable
#     def _init_(self):
#         self.name = "sid" #instance variable.
#         self.email = "sid@gmail.com™
#         #return name, email # error --> cannot use return with constructor

#     def display(self): # instance method
#         print(self.name, self.email)

# c1 = classl()
# c1.display()


# ! -------> Inheritance
# The process of utilising the methods and attributes of parent class
# throught the object of child class it is called as inheritance

# ? 5 types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance































