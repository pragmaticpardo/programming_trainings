passwordFile = open('password.txt') # assings a stream object to the variable

# read the content
secretPassword = passwordFile.read()

# always remember to log to check what you are doing
print(secretPassword)
