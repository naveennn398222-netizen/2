import sys
if len(sys.argv) != 3:
    print("usage: python login.py <username> <password>")
else:
    username = sys.argv[1]
    password = sys.argv[2]

    current_username = "naveen"
    current_password = "123"

    if username == current_username and password == current_password:
        print("login successful")
    else:
        print("login unsuccessful")
