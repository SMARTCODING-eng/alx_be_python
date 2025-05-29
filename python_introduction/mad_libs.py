print("Welcome to the mad libs Generator!")
print("Please enter the following words to create your story:\n")


#Get user inputs 
adjective1 = input("Enter an adjective world (describing the day): ")
adjective2 = input("Enter another adjective world (describing a monkey): ")
adjective3 = input("Enter the third ajective world:(descibing a lion): ")
adjective4 = input("Enter the fourth adjective world: (descibing the expirience) ")
animal_sound = input("Enter an animal  sound: ")
time_of_day = input("Enter a time of day: ")

#Conditional statements to check if the user input are valid
if time_of_day.lower() == "morning":
    time_desc = "early in the morning"
elif time_of_day.lower() == "afternoon":
    time_desc = "in the bright afternoon"
elif time_of_day.lower() == "evening":
    time_desc = "as the sun was setting"
else:
    time_desc = "at the perfect time of the day"

if adjective2.lower() in ["funny", "silly", "goofy"]:
    monkey_action = "making funny faces and"
else:
    monjet_action = "playfully"
if adjective3.lower() in ["majestic", "regal", "noble"]:
    lion_desc = "looking like royalty"
else:
    lion_desc = "relaxing comfortably"

#Build the story
story = f"""
on a {adjective1} day, I went to the zoo {time_desc}.
I saw a {adjective2} looking monkey {monkey_action} swinging from the trees.
Then, I spotted a {adjective3} lion {lion_desc} in the sun.
suddenly, I heard a loud '{animal_sound.upper()}!'
What a wild and {adjective4} experience!
"""

#Display the final story 
print("\nHere's your zoo mad libs story:\n")
print(story)
print("Thanks for playing!")