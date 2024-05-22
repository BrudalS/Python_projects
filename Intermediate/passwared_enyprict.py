from cryptography.fernet import Fernet

passkey = input("Enter the passkey ")


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
        f.close()


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
        f.close()
    return key


key = load_key()
fer = Fernet(key)


def add(name, pwd):
    with open("passwards.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd) + "\n")
        f.close()


def view():
    with open("passwards.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print(f"Name : {name} Passward : {fer.decrypt(pwd)}")
        f.close()


while True:

    choice = input("Would u like to (add, view) data or type q to quit ")

    if choice == "q":
        print("Exiting the process ")
        break

    if choice == "add":
        name = input("Name : ")
        pwd = input("Passward : ")
        add(name, pwd)

    elif choice == "view":
        view()

    else:
        print("Invalid choice ")
