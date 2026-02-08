while True:
    print("\n--- Mini Notes App ---")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        note = input("Write your note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        print("✅ Note saved successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()

            if len(notes) == 0:
                print("No notes found.")
            else:
                print("\nYour Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes file found. Add a note first.")

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")