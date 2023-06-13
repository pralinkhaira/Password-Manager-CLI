# Password Manager CLI

This is a simple command-line interface (CLI) password manager application that allows you to store and manage passwords.

## Features

The password manager CLI has the following features:

- **Add a new password to the password manager:** You can add a new password to the password manager by entering a password name and password. The password manager will then store the password and associated name.
- **View all the passwords in the password manager:** You can view all the passwords in the password manager by selecting the "View passwords" option in the menu. The password manager will then display a list of all the passwords and their associated names.
- **Search for a specific password by its associated name:** You can search for a specific password by entering its associated name. The password manager will then search for the password and display it if it is found.
- **Delete a password from the password manager:** You can delete a password from the password manager by entering its associated name. The password manager will then delete the password from the list of stored passwords.

## Usage

To use the password manager CLI, follow these steps:

1. Clone the repository: `git clone https://github.com/PralinKhaira/Password-Manager-CLI`
2. Install Python 3.x if you haven't already: [Python Downloads](https://www.python.org/downloads/)
3. Navigate to the directory containing the password_manager.py file in your terminal or command prompt
4. Run the command `python password_manager.py` to start the password manager
5. Follow the prompts in the password manager to add, view, search, or delete passwords
6. There is example `password.json` file in which each password is associated with a name or category (e.g., "Email," "Bank," "Social Media," etc.). When the code loads this JSON file, it will populate the passwords dictionary with these entries.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or pull request.

## Contact

If you have any questions or comments about this project, please feel free to contact me at [be.coder.19@gmail.com].

## Update Note

`Update V1.1`

In the modified code:
- The `PasswordManager` class encapsulates the password management functionality. It includes methods for generating a key, loading and saving passwords, encrypting and decrypting passwords, adding, viewing, searching, and deleting passwords.
- The `generate_key()` method is used to generate a new encryption key using the `Fernet` class from the `cryptography` library.
- The file operations in `load_passwords()` and `save_passwords()` methods now handle encryption and decryption of password data using the encryption key.
- The `add_password()` method validates the password name to ensure it is unique and prompts the user for a password with a minimum length of 8 characters. It utilizes the `getpass` module to hide the password input while typing for enhanced security.
- The `run()` method is responsible for running the password manager program. It generates a new encryption key, loads existing passwords, and presents the menu options to the user.
