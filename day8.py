
def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)

def gracemark (object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

# ? Problem:1
def palindrome(n):
    string str(n)
    rev = str(n)[::-1]
if string==rev:
   print(n, "Palindrome")
else:
    print("Not palindrome")
a = int(input("Enter the value: "))
palindrome(a)

#? The position of parameter ahve to be same as position os arguments.
#Eg:1
def profile(name, phone, mark):
txt = "My name is (). My phone number is (). I got {) marks."
print(txt.format(name, phone, mark))
profile(9878776767, "sidhu", 97) # unexpected output
Keyword args

# Eg:1
#? To overcome the disadvantage of position args, we use keyword args
def profile(name, phone, mark):
txt = "My name is {). My phone number is (). I got {} marks." print(txt.format(name, phone, mark))
profile()



# Eg:2
def profile(name, phone,place="kadapa"):
    if place == "kadapa" or place=="kadapa" or place=="kadapa":
       text = "my name is {}. my phone number is {}. I am from {}."
       print(text.format(name, phone,place))
    else:
        print("you are not eligible for signup")
profile("sid ",8767676767)


# ! Eg:2
 def profile("name, age):
     for val in name:
         print("My name is", val, "may age is", age)
     profile("sid", "name2', 'name3', 28) #error age has no args
             
def profile(age, name):
    for val in name:
        print("My name is", val, "may age is", age)
profile(28, "sid", 'name2', 'name3')

# * Keyword variable length args
kwargs --> which is used to provide the args in the form of key value pair.
#! Eg:1
def price(**price_list):
    print(price_list)
    
price(shirt=1000, iphone 80000)
n = 5
{1:1, 2:4, 3:9, 4:16, 5:25}

d1 ("a":100, "b": 200, "c":300)
d1= dict(a=100, b=200, c=300)
print(d1)



# ! Class is a blue print of an object
11 = [1,2,3,4,5,6]
 ? Eg:1
 class c1:
     name1 "sidhu" #
     print(namel)

# ? Eg:2
class person:
    name = "sidhu"
    
c = person() # C OS OBJECT
# The process of creation of an object is called as instantiation
print(c.name)


# ? Eg:4
Method with parameter
class person:
    def display (person, name, age):
        print(name, age)

p = person()
p.display("sidhu", 28)






































