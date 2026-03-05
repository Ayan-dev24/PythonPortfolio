expenses = []


try:
    with open("expenses.txt") as file:
        for line in file:
            expenses.append(float(line.strip()))
except FileNotFoundError:
    pass

def add_expenses(amount):
    expenses.append(amount)
    with open("expenses.txt" , "a") as file:
        file.write(str(amount) + "\n")

def show_stats():
    total = sum(expenses)
    count = len(expenses)

    if count == 0:
        print("No Expenses yet.")
    
    else:
        average = total/count
        print("Total Expenses" , total)
        print("Number of Expenses" , count)
        print("Average Expenses" , average)

while True:
    print("\n1. Add Expenses")
    print("2. Show Statistics")
    print("3. Exit")

    choice = input("Enter your choice:      ")
    
    if choice == "1":
        try:
            amount = float(input("Enter your amount:      "))
            add_expenses(amount)
            print("Amount Saved Successfully")
        except ValueError:
            print("Invalid Number")

    elif choice == "2":
        show_stats()

    elif choice == "3":
        print("GoodBye👋")
        break

    else:
        print("Invalid Option")



