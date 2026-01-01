while True:
        user_input = input("Enter a number (1-5) or type 'quit' to exit: ")

        if user_input.lower() == "quit":
            print("Program exited.")
        break

        if not user_input.isdigit():
            print("Invalid input! Please enter a number between 1 and 5.")
        continue

        num = int(user_input)

        if num == 1:
            print("one")
        elif num == 2:
            print("two")
        elif num == 3:
            print("three")
        elif num == 4:
            print("four")
        elif num == 5:
            print("five")
        else:
            print("Error: Number out of range (1-5 only).")
