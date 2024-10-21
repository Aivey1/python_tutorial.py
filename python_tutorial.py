# This is my first Python program.
# It will print a message, ask if you're ready, ask for your name, and ask a fun question before saying goodbye.

# Print a welcome message to the screen
print("Hello, World!")

# Ask the user if they are ready to continue
ready = input("Are you ready to continue? (Y/N): ")

# Check if the user typed 'Y' or 'N'
if ready == "Y":
    # If the user typed 'Y', print a message and continue
    print("Great! Let's keep going!")
elif ready == "N":
    # If the user typed 'N', print a message and stop
    print("Okay, maybe next time!")
else:
    # If the user typed something other than 'Y' or 'N', still continue
    print("You didn't type Y or N, but let's continue anyway!")

# Ask the user for their name and store it in a variable called 'name'
name = input("What's your name? ")

# Print a greeting using the name the user typed
print("Hi, " + name + "! Nice to meet you!")

# Ask the user a fun question (favorite color)
color = input("What's your favorite color? ")

# Print a response using their favorite color
print("Wow! " + color + " is a really nice color!")

# End the program with a goodbye message that includes the user's name
print("Goodbye, " + name + "! Have a great day!")