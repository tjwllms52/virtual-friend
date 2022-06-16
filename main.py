import time

friend_name = input(str("Whats Your Friends Name? "))

print("Your Texting " + friend_name)
while True:
  Your_text = input(str("You: "))
  if Your_text=="hi" or Your_text=="hello":
    print(friend_name + " Is Typing...")
    time.sleep(0.8)
    print(friend_name + ": hi")
