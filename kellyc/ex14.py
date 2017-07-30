from sys import argv

script, user_name = argv
prompt = '> '

# Reminder: The f preceding string stands for format
print(f"Hi {user_name} I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.
And you have a {computer} computer.
""")


print(f"Nice to meet you, {user_name}.)
print("I just need to ask you a few quick questions in order to customize your rollercoaster ride.")

print(f"On a scale of one to ten, with ten being petrified, how nervous are you?")
nervousness = input(prompt)

print(f"Here are some headphones for you to wear, {user_name}. We can play music to pump you up or calm you down. What song would you like to hear?")
song = input(prompt)

print("What letter does your favorite rollercoaster track shape match?")
track = input(prompt)

print(f"""
Woowee! {user_name}, you are in for a good time. Can you hear {song} in your ears yet? Good. Brace you for those {track}s! This ride will last {nervousness} minutes.
""")
