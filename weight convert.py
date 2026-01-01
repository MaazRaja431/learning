sel = input("Enter weight in (p) for pounds and (k) for kilo: ")
if sel!="k" and "p":
    print("please enter weight in p or k:")

else:
    weight = float(input("Enter your weight:" ))  
if sel=="k":
    print("weight is {weight * 2.20482} p ")
else:
    print("weight is {weight / 2.20482} k ")