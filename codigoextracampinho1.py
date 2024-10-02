"""
Aqui estão as novidades:

Adicionei expressões regulares para validar os formatos de número de telefone e endereço de e-mail.
Usei o módulo getpass para inserir senhas com segurança, para que elas não sejam ecoadas no console.
Adicionei uma etapa de confirmação de senha para garantir que o usuário insira a mesma senha duas vezes.
Forneci uma opção para salvar os dados do usuário em um arquivo (user_data.txt) após o registro.
Observe que este código ainda tem algumas limitações, como:

Ele não lida com casos em que o usuário deseja cancelar o processo de registro.
Ele não armazena os dados do usuário com segurança (por exemplo, as senhas são armazenadas em texto simples).
Ele não fornece uma maneira de recuperar ou atualizar os dados do usuário.
Você pode aprimorar ainda mais este código para abordar essas limitações e adicionar mais recursos conforme necessário.
"""
import re
import getpass

def register_user():
    user_data = {}

    # Get first name
    while True:
        first_name = input("Enter your first name: ")
        if first_name.strip() != "":
            user_data["first_name"] = first_name
            break
        else:
            print("Please enter a valid first name.")

    # Get last name
    while True:
        last_name = input("Enter your last name: ")
        if last_name.strip() != "":
            user_data["last_name"] = last_name
            break
        else:
            print("Please enter a valid last name.")

    # Get age
    while True:
        age = input("Enter your age: ")
        if age.isdigit() and 18 <= int(age) <= 120:
            user_data["age"] = int(age)
            break
        else:
            print("Please enter a valid age (between 18 and 120).")

    # Get telephone number
    while True:
        telephone_number = input("Enter your telephone number: ")
        if re.match(r"^[0-9]{10,15}$", telephone_number):
            user_data["telephone_number"] = telephone_number
            break
        else:
            print("Please enter a valid telephone number (10-15 digits).")

    # Get email
    while True:
        email = input("Enter your email: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            user_data["email"] = email
            break
        else:
            print("Please enter a valid email address.")

    # Get password
    while True:
        password = getpass.getpass("Enter your password: ")
        if len(password) >= 8:
            user_data["password"] = password
            break
        else:
            print("Please enter a password with at least 8 characters.")

    # Confirm password
    while True:
        confirm_password = getpass.getpass("Confirm your password: ")
        if confirm_password == user_data["password"]:
            break
        else:
            print("Passwords do not match. Please try again.")

    # Validate user data
    print("\nRegistration successful!")
    print("Here's your registered data:")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")

    # Save user data to a file (optional)
    save_to_file = input("\nDo you want to save your data to a file? (y/n): ")
    if save_to_file.lower() == "y":
        with open("user_data.txt", "w") as f:
            for key, value in user_data.items():
                f.write(f"{key.capitalize()}: {value}\n")
        print("Data saved to user_data.txt")

register_user()