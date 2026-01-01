tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

user_item = (input("Enter item to search: "))

found = False

for i in range(len(tuple1)):
    # Check if the element is iterable (list or tuple)
    if isinstance(tuple1[i], (list, tuple)):
        for j in range(len(tuple1[i])):
            if tuple1[i][j] == user_item:
                print([i, j])
                found = True
                break
    else:
        if tuple1[i] == user_item:
            print([i])
            found = True

    if found:
        break

if not found:
    print("item not found")
