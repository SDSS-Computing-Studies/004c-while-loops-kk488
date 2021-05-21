#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
print("enter correct username and password")
inputName=""
inputPW=""
while inputName!="admin" and inputPW!="12345":
    inputName=input("enter username:")
    inputPW=input("enter password:")
    if inputName=="admin" and inputPW=="12345":
        print("Access granted.")
        break
    else:
        print("Access denied.")
        inputName=input("enter username:")
        inputPW=input("enter password:")