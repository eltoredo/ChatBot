import wikipedia
from commands import commands


def get_from_wiki(truc):
	for catcher in commands[2]['catchers']:
		truc = truc.replace(catcher, "")
	truc.replace("?", "")
	resp = ""
	try:
		resp = wikipedia.summary(truc, sentences=1)
	except wikipedia.exceptions.DisambiguationError as e:
		try:
			resp = wikipedia.summary(e.options[0], sentences=1)
		except:
			pass
	except:
		pass

	if len(resp) > 5:
		return resp + " Little idiot."
	else:
		return "I don't what you're talking about, human."

