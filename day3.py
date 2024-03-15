# ! Eg:4
# Python program to check whether the
# given integer is a multiple of both 5 and 7

n = int(int("enter the number: "))
if n%5=0 and n%7==0:
    print("yes")
else:
    print("no")


# Eg:5
# Write a program to accept the cost price of a bike and display the
#road tax to be paid
#according to the following criteria :

#        Cost price (in Rs)                             Tax
         > 100000                                          15% discount 6%.
         > 50000 and <- 100000                             10%
         <= 50000                                          5%


price = int(input("eenter the price: "))
amount = 0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    amount=value*(15/100)
    total=value+amount
else:
    tax = price*(15/100)
    total = price+tax
print("the onroad cost of bike is: ",total)


char = input("enter the chare: ")

for val in range(1, 10):
    if val ==6:
        continue
    print(val)




    
