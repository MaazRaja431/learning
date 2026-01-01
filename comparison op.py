#temperature=float(input("Enter the temp: "))

#if temperature >30:
 #   print("It's a hot day")

#elif temperature <10:
 #   print("It's a cold day")   
#elif 30> temperature <20:
  #  print("It's a warm day")    
#else:
  #  print("It's neither cold or hot day")    




  #   *** exercise 1 ***
# Create a program for user password creation which takes in input of user's
# desired password. If the password is less than 3 characters long 
# the program should display "Password cannot be less than 3 characters"
# if the password is longer than 8 characters program should display
# "password cannot be more than 8 characters"
# otherwise it should display "password looks good" and display the password
# Hint: use len() function 

#password = input("Enter your desired password: ")

#if len(password) < 3:
 #   print("Password cannot be less than 3 characters")
#elif len(password) > 8:
 #   print("Password cannot be more than 8 characters")
#else:
 #   print("Password looks good")


    # A shop will give discount of 10% if the cost of
#  purchased quantity is more than 1000.
# Ask user for quantity
# take input for cost
# Judge and print total cost after discount for user.

quantity = int(input("Enter quantity: "))
cost_per_item = float(input("Enter cost per item: "))

total_cost = quantity * cost_per_item

if total_cost > 1000:
    discount = total_cost * 0.10
    final_cost = total_cost - discount
    print("You got a 10% discount!")
    print("Total cost after discount:", final_cost)
else:
    print("No discount applied.")
    print("Total cost:", total_cost)

