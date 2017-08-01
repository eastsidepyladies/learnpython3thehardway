from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Would you swipe right on my profile?")
likes = input(prompt)

print("Do you take the red pill or the blue pill?")
pill = input(prompt)

print(f"{user_name}, what is the title of your favorite movie?")
movie = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You said you would take {pill}. Nice.
Your favorite movie is {movie}. Mine too! What a crazy random happenstance.
Will you be my best friend?
""")
friend = input(prompt)

if friend == "yes":
    print("Awesome! This is going to be great.")
elif friend == "no":
    print("I am sorry you feel that way, I will respect your wishes.")
else:
    print("Thank you. You seem like a really intersting person. I am glad I got to know you.")