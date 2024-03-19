

#1.)Python program to captilalize the first and last character of each word in a string
#2.)Input:128
#ouput:Yes
#128%1==0,128%2==0, and 128%8==0.
#3.)l1=[1,2,3,4],l2=[5,6,7,8]
#add both l1 and l2 and ans=[6,8,10,12]


n = 128
while n!=0:
    rem = n%10
    print (rem)
    n = n/10

s1 = input("enter string: ")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

s1 = (8, 78, 67, 'u')
add()
s1.add(43)
print(s1)

update()
s1.update([9, 0])
print(s1)

s1 = set() # to create empty set
print(type(s1))

s1 = {8, 9, 8}
si.clear()
print(s1)

del s1
print(s1)

#* join the sets
s1 = (9, 0, 8}
s2 = (9.90, "card", 't', 56)
# union()---> to ambine 2 sets
s3 = s1.union(s2)
print (s3)

# * intersection()---> to get common elements inside set
s1 = (4, 5, 6)
s2 = (5, 6, 7, 8)
print(s1.intersection(s2))

# * difference()
s1 = {4, 5, 6,}
s2 = {5, 6, 7, 8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))


isdisjoit(), issubset(), issuperset()
s1 = (8, 9, 8)
s2 = (6, 7, 5, 8, 9, 0)

print(s1.issubset(s2))
print(s2.issuperset(s1))


s1 = {1,2,3,4,5}
s2 = {3,2, 7,8,9}
















































