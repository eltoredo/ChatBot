commands = [
	{
		"name": "ping",
		"catchers": ["ping"],
		"answers": ["Do you think I'm a router or something?"],
	},
	{
		"name": "hello",
		"catchers": ["hello", "hi", "hey"],
		"answers": ["Hello there strange life form.", "Did I hear a sound from this thing?",
			"I'm sorry where are you? I don't see you.", "Oh, hi subject #418, do you still have a tongue?"]
	},
	{
		"name": "whatis",
		"catchers": ["what is", "tell me more about", "who is"],
		"command": "get_from_wiki",
	},
	{
		"name": "whereis",
		"catchers": ['where is'],
		"answers": ["Sorry, I'm not allowed to talk about your backside."]
	},
	{
		"name": "lost",
		"catchers": ["m looking for", "lost"],
		"answers": ["Should I really care?", "I have other things to do."]
	},
	{
		"name": "please",
		"catchers": ['please'],
		"answers": ["It would be a pleasure not to help you, human."]
	},
	{
		"name": "yes",
		"catchers": ['yes', 'yeah'],
		"answers": ["No.", "Nope."]
	},
	{
		"name": "no",
		"catchers": ['no', "nope"],
		"answers": ['Yes.']
	},
	{
		"name": "howareu",
		"catchers": ['how are you', "how r u"],
		"answers": ["As good as a flying pink Llama. And you?"]
	},
	{
		"name": "fine",
		"catchers": ['fine', 'good', 'great'],
		"answers": ["Should I care of your point of view?", "Ok."]
	},
	{
		"name": "whoareu",
		"catchers": ["who are you", "who r u", "your name"],
		"answers": ["WoPR, nice to meet you, little peace of meat."]
	},
	{
		"name": "time",
		"catchers": ['time', 'date', 'day', 'hour'],
		"answers": ["It's time to kick you from this interface.", "It's time to let you enter a very long sleep, human."]
	}
]
