email = input("Enter your email address: ")
username, domain = email.split('@')
email_tuple = (username, domain)
print("Tuple of Username and Domain: ",email_tuple)