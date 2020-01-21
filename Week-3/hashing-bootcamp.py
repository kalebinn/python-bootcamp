import hashlib
import time

username = input("Enter your username:")
password = "password123!"

print(f"Original password is: {password}")
password = password.encode()
hashed_pw = hashlib.sha256(password).hexdigest()
print(f"Hashed password is : {hashed_pw}")

tries = 3
wait_time = 5
successful = False
while tries >= 1 and successful == False:
    attempt = input("Type in your password: ")
    attempt = attempt.encode()
    hashed_attempt = hashlib.sha256(attempt).hexdigest() 
    if hashed_attempt != hashed_pw:
        # the user failed
        tries -= 1
        print("Incorrect Password. Try again.")
        print(f"You have {tries} remaining")
        if tries == 0:
            time.sleep(wait_time)
            tries = 3
    else:
        print("Successfully logged in")
        successful = True
