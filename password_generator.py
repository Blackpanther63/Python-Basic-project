import string
import secrets

def generate_password(length):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with specified length
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def display_passwords(passwords):
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password}")

def main():
    passwords = []
    min_length = 2  # Minimum password length

    num_passwords = int(input("Enter the total number of passwords to generate: "))
    if num_passwords < 1:
        print("Please enter a valid number of passwords.")
        return

    for i in range(num_passwords):
        password_length = int(input(f"Enter the length of password {i + 1} (minimum 2): "))
        if password_length < min_length:
            print("Password length must be at least 2. Skipping...")
            continue
        
        password = generate_password(password_length)
        passwords.append(password)
        print(f"Password {i + 1}: {password}")

    while True:
        choice = input("\nEnter 'D' to delete a password, 'S' to display passwords, or 'Q' to quit: ").upper()
        if choice == 'D':
            index = int(input("Enter the index of the password to delete: "))
            if 1 <= index <= len(passwords):
                del passwords[index - 1]
                print(f"Password {index} deleted successfully.")
            else:
                print("Invalid index. Please enter a valid index.")
        elif choice == 'S':
            display_passwords(passwords)
        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'D', 'S', or 'Q'.")

if __name__ == "__main__":
    main()
