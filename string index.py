#a = ("PYTHON")
#print(a[-3])

#print(a[4])

#print(a[0:4:1])

#print(a[0:4:2])

#print(a[::2])



 #weather="it is raiNing"
        #0123456789  indexes 
#print(weather[:14:1])

#print(weather[5:8])


##Q1: you have a string : word = "Paris is my favourite tourist area"
# print the words "Paris" and "my" using string indexing 

#a = ("Paris is my favourite tourist area")
#print(a[0:6:1])
#print(a[9:11:1])



# Q2: Using string indexing/slicing, print out the following:
# data="I love apples, python is a programming language"
# output="I love python language"



data = "I love apples, python is a programming language"


part1 = data[:6]          
part2 = data[15:21]       
part3 = data[-8:]         


output = part1 + " " + part2 + " " + part3
print(output)

