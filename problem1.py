##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
print("enter correct username and password")
inputName=""
inputPW=""
count=0
while inputName!="admin" and inputPW!="12345" and count<4:
    inputName=input("enter username:")
    inputPW=input("enter password:")
    if inputName=="admin" and inputPW=="12345":
        print("Access granted.")
        break
    else:
        print("Access denied.")
        inputName=input("enter username:")
        inputPW=input("enter password:")
        count+=1
