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
        if telephone_number.strip() != "" and len(telephone_number) >= 10:
            user_data["telephone_number"] = telephone_number
            break
        else:
            print("Please enter a valid telephone number.")

    # Get email
    while True:
        email = input("Enter your email: ")
        if "@" in email and email.strip() != "":
            user_data["email"] = email
            break
        else:
            print("Please enter a valid email address.")

    # Get password
    while True:
        password = input("Enter your password: ")
        if len(password) >= 8:
            user_data["password"] = password
            break
        else:
            print("Please enter a password with at least 8 characters.")

    # Validate user data
    print("\nRegistration successful!")
    print("Here's your registered data:")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")

register_user()