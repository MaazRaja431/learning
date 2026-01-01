#numbers=[3,4,5]

#numbers.insert(0,[1,2])

#numbers.remove(4)

#numbers.clear()

#numbers.pop(2) 
#print(numbers)


l=[5,7,5,5,3,9]
#print(l.count(5))

#l.sort()
#l.reverse()
#print(l)


#print(l.sort())
#l.sort(reverse=True)



#numbers = [1, 2, 3, 2, 4, 1, 5]

#unique_numbers = []

#for num in numbers:
  #  if num not in unique_numbers:
   #     unique_numbers.append(num)

#print(unique_numbers)



#numbers = [1, 2, 3, 4, 5, 6, 7]

#squares = [num ** 2 # num in numbers]

#print(squares)


list1 = [1, 6, 7, 4, 5, 6]
list2 = [6, 5, 4, 2, 1, 5]

pairs = []
indexes = []

for i in range(len(list1)):
    if list1[i] + list2[i] >= 11:
        pairs.append([list1[i], list2[i]])
        indexes.append(i)

print("Output:", pairs)
print("Indexes:", indexes)

