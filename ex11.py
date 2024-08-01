import time

user_fav_color=input("What is your favorite color? ")
if user_fav_color=="blue":
    time.sleep(1)
    print("You love the sky am I wrong ? ")
    time.sleep(1)
    checkBlue=input("Write 1 and enter If it is true... If It is false write 2 and send it ")
    if checkBlue=="1":
        print("Thats fantastic!")
    if checkBlue=="2":
        blueFantastic=input("I am sorry,tell me your fav thing I will try to keep it in my mind... ")
        print(f"Great!! I will keep in my mind your fav thing: {blueFantastic}")

if user_fav_color=="red":
    time.sleep(1)
    print("You should love red cars huh ?")
    time.sleep(1)
    checkRed=input("Write 1 if it is true... If it is not then write 2 and click enter ")
    if checkRed=="1":
        print("I guess it! fantastic")
    if checkRed=="2":
        redFantastic=input("What is your fav red thing? I will keep it in my ming ")
        print(f"Great!! I will keep in my mind your fav thing: {redFantastic}")


if user_fav_color !="red" or "blue": #if user_fav_color != "red" and user_fav_color != "blue":

    print("I dont know that color")
    