def get_user_info(*args, **kwargs):
    if len(args) >= 3: 
        name = args[0]
        email = args[1]
        age = args[2]

    additional_info = kwargs.get('more_info', '')

    print("\nUser Information:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Additional Info: {additional_info}")


get_user_info('John Doe', 'john@example.com', 30, more_info='Loves fishing')
#first three parameters are taken as positional arguements and 4th is taken as keywordBased argument 
name1=input("Enter name: ")
email1=input("Enter email: ")
get_user_info(name1, email1, 30, more_info='no info')

