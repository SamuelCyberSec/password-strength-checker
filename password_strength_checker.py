import re


def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for digits
    if re.search(r"\d", password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1


    # Determine strength level
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"



if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

