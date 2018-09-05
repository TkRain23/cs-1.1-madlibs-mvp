# Name: Timothy C. Kaing
# Project: Madlibs
#
# Requirements:
# - Display story with blanks for input words with correct type
# - Ask user to input words to fill in the blanks.
# - Output the story with the blanks filled in.
# - The system module (for accessing command-line arguments)
# - A test suite to test user input.

# initialize variables

story = '''
The Potatoes and the Tomatoes: Template

There once was a potato named _____. The potato had _____ friends.
Together they would _____, _____, and _____ the tomatoes. One day the potato
met a tomato named _____. The potato loved how _____ the tomato was. The potato
would then _____ the tomato.
'''

print(story)

noun1 = raw_input("Enter a noun: ")
adj1 = raw_input("Enter a adjective: ")
verb1 = raw_input("Enter a verb: ")
verb2 = raw_input("Enter a verb: ")
verb3 = raw_input("Enter a verb: ")
noun2 = raw_input("Enter a noun: ")
adj2 = raw_input("Enter a adjective: ")
verb4 = raw_input("Enter a verb: ")

story = '''
The Potatoes and the Tomatoes: A story by you

There once was a potato named %s. The potato had %s friends.
Together they would %s, %s, and %s the tomatoes. One day the potato
met a tomato named %s. The potato loved how %s the tomato was. The potato
would then %s the tomato.
'''

print(story) % (noun1, adj1, verb1, verb2, verb3, noun2, adj2, verb4)
