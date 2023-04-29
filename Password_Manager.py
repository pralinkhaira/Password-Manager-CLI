import json

def load_passwords():
    try:
        with open('passwords.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

def add_password():
    passwords = load_passwords()
    name = input('Enter password name: ')
    password = input('Enter password: ')
    passwords[name] = password
    save_passwords(passwords)
    print(f'{name} password added successfully')

def view_passwords():
    passwords = load_passwords()
    for name, password in passwords.items():
        print(f'{name}: {password}')

def search_password():
    passwords = load_passwords()
    name = input('Enter password name: ')
    if name in passwords:
        print(f'{name}: {passwords[name]}')
    else:
        print(f'{name} password not found')

def delete_password():
    passwords = load_passwords()
    name = input('Enter password name: ')
    if name in passwords:
        del passwords[name]
        save_passwords(passwords)
        print(f'{name} password deleted successfully')
    else:
        print(f'{name} password not found')

while True:
    print('1. Add password')
    print('2. View passwords')
    print('3. Search password')
    print('4. Delete password')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        add_password()
    elif choice == '2':
        view_passwords()
    elif choice == '3':
        search_password()
    elif choice == '4':
        delete_password()
    elif choice == '5':
        break
    else:
        print('Invalid choice')
