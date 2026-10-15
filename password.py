import secrets
import string


def generate_password(length=12):
    """Generate a secure random password with at least one of each character type."""
    if length < 4:
        raise ValueError("Length must be at least 4 to include all character types")

    sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    ]
    all_chars = "".join(sets)

    # 1. Guarantee one from each required set
    password = [secrets.choice(s) for s in sets]

    # 2. Fill the rest from the combined pool
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    # 3. Securely shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    try:
        length = int(input("Desired password length [12]: ") or "12")
    except ValueError:
        print("Invalid input, using default length of 12.")
        length = 12

    print(f"Generated password: {generate_password(length)}")   
