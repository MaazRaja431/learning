#Osama = 123

#for item in [Osama,"john","Brad"]:  # item here is loop variable so we donot need to initialize it
  #      print(item)


#for item in range (0,101):
 #           print(item)       


#Quick Exercise:

#cart=[10,20,30]
#Calculate total cost of all the items in the shopping cart 
#without using sum function'''
#cart = [10, 30, 30]

#total = 0
#for price in cart:
  #  total = total + price

#print("Total cost of items:", total)

# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a 
# given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

num = int(input("Enter a number: "))

total = 0
expression = ""

for i in range(1, num + 1):
    total += i
    expression += str(i)
    if i != num:
        expression += "+"

print("Sum is:", expression, "=", total)



        