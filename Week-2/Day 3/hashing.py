import hashlib
import time

username = "kelvin"
pw = "password123"

# lets say i want to store this password
# but you don't really want to expose the actual password
# or hold onto the plain text version of the password
# as a result, many corporations will store your password as a hash of some sort
# (either that or an encryption). Let's try to hash our password

# lets use SHA-1
pw = pw.encode()
pw_hashed = hashlib.sha1(pw).hexdigest()
#print(pw_hashed)


tries = 3
wait_time = 10

success = False
while(tries >= 1 and success == False):
    user_input = input("Please type your password:").encode()
    hashed_input = hashlib.sha1(user_input).hexdigest()
    if (hashed_input != pw_hashed):
        tries -= 1
        if (tries == 0):
            for i in range(wait_time):
                print(f"Please wait {wait_time-i} seconds before trying again")
                time.sleep(1)
        else:
            print("your password was incorrect, please try again.")
            print(f"you have {tries} tries remaining")
    else:
        print("successfully logged in.")
        success = True