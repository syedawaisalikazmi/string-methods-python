username=input("enter your username:")
if len(username)>12:
    print("please enter 12 digits in username")
elif " " in username:
    print("please don't use space")
elif not username.isalpha():
    print("digits or other symbols not allowed ")
else:
    print(f"WELCOME {username}")
