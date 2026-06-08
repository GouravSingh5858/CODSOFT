import random
import string

print("===== Strong Password Generator =====")

try:
    password_length = int(input("Enter password length: "))

    if password_length < 6:
        print("Password length should be at least 6.")

    else:
        include_symbols = input("Include special symbols? (y/n): ").lower()
        total_passwords = int(input("How many passwords do you want to generate? "))

        for i in range(total_passwords):

            password = [
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits)
            ]

            if include_symbols == 'y':
                password.append(random.choice(string.punctuation))

            all_characters = string.ascii_letters + string.digits

            if include_symbols == 'y':
                all_characters += string.punctuation

            remaining = password_length - len(password)

            password += random.choices(all_characters, k=remaining)

            random.shuffle(password)

            final_password = "".join(password)

            print(f"\nPassword {i+1}: {final_password}")

            # Password Strength Checker
            if password_length < 8:
                print("Strength: Weak")
            elif password_length < 12:
                print("Strength: Medium")
            else:
                print("Strength: Strong")

except ValueError:
    print("Please enter valid numeric values.")
