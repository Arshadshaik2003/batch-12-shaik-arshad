#a=7, 8
#print(a)
#print(type(a))


#----> swapping of variable
a = 7
b = 5


temp=a #temp=7
a=b    #a=5
b=temp #b=7

#a=5, b=7
print(a,b)

#Eg:2
a=a+b #a=12
#b=a-b #b=12-7=5
#a=a-b #12-5=7

#print(a,b)

#a, b=b a # only in pyhon

a=a*b #a=35
b=a/b #b=35/7=5,0
a=a/b #a=35/7=7,0
print(int(a),int(b))


#id()--> used to find the memory address of the variable
a=7
b=8
# print(id(a))
# print(id(B))


# ! Assignment --> = +=, /=, *=, //=, **=, &-, |=, &=
# a=8
# a+=2
# print(a)


# a=30
# a-=5
# print(a)

# ! comparison--> ==, >, <, |=, <=, >=
# a=8
# b=7
# print(a==b)

# ! bitwise operator ---> &, |, ^, ~, <<,>>
a = 7
b = 4
print(a&b)

# 2^4 2^3 2^2 2^1 2^0
#  8   4   2   1

#  0   1   1   1   #--->7
#  0   1   0   0   #--->46
# --------------------
#  0   1   0   0

# ~ ----->
# a = 9876
# print(~a)

# a = 9

# 128 64 32 16 8 4 2 1
#  0   0  0  0 1 0 0 1 #---> 9

#  1  1  1  1  0  1  1  0 # ---> -10

#  1  1  1  0  1  0  1  0 --->  10

#  1  1  1  0  1  0  1 ---> is compliment of 10
#                 #  1 ---> 2s compliment
#-----------------------------------
#  1  1  1  1  0  1  1  0 --->  -10

#  256 128 64 32 16 8 4 2 1
#   0   0  0  0  0  0 1 0 1
#   0   0  0  1  0  1 0 0 0 ---> 40
# 107

# <<, >>
# print(5>>1)
# 16>4

# ! Logical ---> used to compare the expression
# and, or, not
 a = 6
# Print(a>3 and a<10)
# print(a>7 or a<30)
# print(not(a>8 and a<10))

# ! identity operator 
# ? it is used to compare the memeory location that the valve
# ? are stored

# Is, is not
a = 8
b = 8
print(a is b)
print(a==b)

a = [1, 2, 3,]
b = [1, 2, 3,]
print(a is not b)

# ! membership operator
# in, not in
11 = [7,8,9,0,6,5]
 # num = 55
# print(num in 11)
# print(num not in 11)

num = 678
#print(8 in num) # error


# a number is even or odd
#nint(input("enter the number: "))
# if n %2==0:
#
print(n, "is even")
# else:
# print(n, "is odd")
#name, age, nationality
# 18 above, Indian


