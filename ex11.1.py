import time

def handle_color(color, guess_message, true_message, false_message):
  time.sleep(1)
  print(guess_message)
  time.sleep(1)
  check = input("Write 1 if it is true... If it is not then write 2 and click enter ")
  if check == "1":
    print(true_message)
  elif check == "2":
    fav_thing = input(f"What is your fav {color} thing? I will keep it in my mind ")
    print(f"Great!! I will keep in my mind your fav thing: {fav_thing}")
  else:
    print("Invalid input. Please enter 1 or 2.")

user_fav_color = input("What is your favorite color? ").lower()  # Convert to lowercase for case-insensitive comparison

if user_fav_color == "blue":
  handle_color("blue", "You love the sky am I wrong ? ", "Thats fantastic!", "")
elif user_fav_color == "red":
  handle_color("red", "You should love red cars huh ?", "I guess it! fantastic", "")
else:
  print("I don't know that color")