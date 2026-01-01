#temp=input("Hot or cold?").lower() 
#if temp == "hot":  
 #       print("It's a hot day")
  #      print("Drink plenty of water")


#elif temp == "cold":
 #       print("it's a cold day")
  #      print("Wear warm clothes")
#else:
 #       print("it's a lovely day")
  #      print("go out for picnic")


#"""Quick Exercise : Ask the user to enter the price of a house
 #                   If user has good credit 
   #                 price goes down by 20%
   #                 Otherwise
    #                price needs to go down by 10%
     #               Print down the discounted cost 
      #              take input of credit from user as good or bad"""

price = float(input("Enter price of house: "))
credit = input("Good or bad; ")
if credit== "good":
   discount = price * 0.20

else:
   discount = price * 0.10
final_price = discount - price

print(final_price)

