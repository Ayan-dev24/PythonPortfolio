while True:
    print("\n1. Add Notes")
    print("2. View Notes")
    print("3. Clear All Notes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_notes = input("Enter the note: ")
        with open("notes.txt", "a") as file:
            file.write(add_notes + "\n")
        print("Notes Saved Successfully ✅")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                sv = file.readlines()

            if not sv:
                print("No notes saved yet.")
            else:
                print("\nYour Notes:")
                for i, note in enumerate(sv):
                    print(f"{i+1}. {note.strip()}")

        except FileNotFoundError:
            print("No files added yet.")

    elif choice == "3":
        inp = input("Are you sure (yes/no): ")

        if inp.lower() == "yes":
            with open("notes.txt", "w") as file:
                pass
            print("Your Notes are removed.")

        elif inp.lower() == "no":
            print("Your Notes are safe.")

        else:
            print("Type the answer in Yes or No")

    elif choice == "4":
        print("GoodBye 👋")
        break

    else:
        print("Invalid Choice ❌")
