import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = input("Enter password length (default 12): ")
    if length.isdigit():
        length = int(length)
    else:
        length = 12
    print("Generated password:", generate_password(length))

if __name__ == "__main__":
    main()
