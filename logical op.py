#high_income = input("Is your income high or low :").lower() 
#good_credit = input("Is your credit good or bad :").lower()
#criminal_record = input("Do you have a criminal record :").lower()



#if high_income=="high" and good_credit=="good" and not criminal_record=="yes": 

 #   print("Eligible for loan ") 
#else:  
     #   print("not eligible for loan") 






weather = input("Enter weather (good/bad): ").lower()
day = input("Was your day productive? (yes/no): ").lower()


if weather == "good" and day == "yes":
    mood = "good"
elif weather == "bad" and day == "yes":
    mood = "okay"
else:
    mood = "bad"

print("Your mood is:", mood)

