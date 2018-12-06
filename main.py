from commands import commands
import functions
import random


def compute(msg):
	for cmd in commands:
		if any(word.lower() in msg.lower() for word in cmd['catchers']):
			if "command" in cmd:
				return getattr(functions, cmd['command'])(msg)
			else:
				return random.choice(cmd['answers'])
	return "What are you talking about?"


while True:
	print(compute(input("> ")))
