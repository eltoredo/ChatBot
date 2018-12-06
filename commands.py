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
	}
]
