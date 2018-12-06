# import various things for random purposes
from commands import commands
import functions
import random

# You know you're fine when your chatbot is written in 5 lines
def compute(msg):
	#
	for cmd in commands:
		# Wow, such one line python
		if any(word.lower() in msg.lower() for word in cmd['catchers']):
			if "command" in cmd:
				# Can certainly cause a security issue, but who care, it's just a bot
				return getattr(functions, cmd['command'])(msg)
			else:
				return random.choice(cmd['answers'])
	return "What are you talking about?"


while True:
	print(compute(input("> ")))
