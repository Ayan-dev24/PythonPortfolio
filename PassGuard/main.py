# Portfolio-Ready Password Strength Checker with Logging

def check_password_strength(password):
    """Check the strength of a password and return score, strength, and suggestions."""
    score = 0

    # Scoring rules
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

    # Determine password strength
    if score == 6:
        strength = "Very Strong Password 🟢"
    elif score >= 4:
        strength = "Strong Password 🟠"
    elif score >= 2:
        strength = "Medium Password 🟡"
    else:
        strength = "Weak Password 🔴"

    # Suggestions for improvement
    suggestions = []
    if not any(c.isupper() for c in password):
        suggestions.append("Add at least one uppercase letter")
    if not any(c.islower() for c in password):
        suggestions.append("Add at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add at least one number")
    if not any(c in "!@#$%^&*()_-+=~`" for c in password):
        suggestions.append("Add at least one special character (!@#$...)")

    return score, strength, suggestions


def log_result(password, score, strength):
    """Save password check results to a log file."""
    with open("passwords_log.txt", "a", encoding="utf-8") as file:
        file.write("Password Checked\n")
        file.write(f"Length: {len(password)}\n")
        file.write(f"Score: {score}/6\n")
        file.write(f"Strength: {strength}\n")
        file.write("-----------------\n")


# Main Program
while True:
    password = input("\nEnter a password: ")

    score, strength, suggestions = check_password_strength(password)

    print(strength)
    print("Score:", score, "/6")

    # Print suggestions if there are any
    if suggestions:
        print("Suggestions to improve your password:")
        for s in suggestions:
            print("-", s)

    # Log the results
    log_result(password, score, strength)

    choice = input("\nDo you want to check another password? (y/n): ").strip().lower()
    if choice not in ["y", "yes"]:
        print("Goodbye 👋")
        break