import os



while True:
  print()
  username = input("Username: ")
  password = input("Password: ")
  if username == os.environ['adminusername'] and password == os.environ['adminpassword']:
    print("You are welcome Admin")
    break
  elif username == os.environ['username'] and password == os.environ['password']:
    print("Welcome", username,"!!!")
    break
  else:
    print("Try again")

