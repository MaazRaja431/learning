#numbers = [12, 20, 158, 180, 244, 525, 45]

#for i in numbers:
 #   if 500>i>150:
  #          continue
   # elif i>500:
    #        break
    #else:
     #       if i%5==0:
      #              print(i)


# print the following pattern using nested loops 

#'''
#xxxxx
#xx
#xxxxx
#xx
#xx'''                    

for i in range(1, 6):
    if i == 1 or i == 3:
        for j in range(5):
            print("x", end="")
    else:
        for j in range(2):
            print("x", end="")
    print()
