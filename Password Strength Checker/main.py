while True:
    password = input("\nEnter a password: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_-+=~`" for c in password):
        score += 1

    # Strength evaluation
    if score == 6:
        print("Very Strong Password 🟢")
    elif score >= 4:
        print("Strong Password 🟠")
    elif score >= 2:
        print("Medium Password 🟡")
    else:
        print("Weak Password 🔴")

    print("Score:", score, "/6")

    choice = input("\nDo you want to check another password? (y/n): ").strip().lower()

    if choice not in ["y", "yes"]:
        print("Goodbye 👋")
        break