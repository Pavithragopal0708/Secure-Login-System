import bcrypt

password = input("Enter Password: ")

hashed_password = bcrypt.hashpw(
    password.encode('utf-8'),
    bcrypt.gensalt()
)

print("Hashed Password:")
print(hashed_password)

if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
    print("Login Successful")
else:
    print("Login Failed")
