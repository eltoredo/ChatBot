# Impor the universal knowledge
import wikipedia
from commands import commands


# The only implemented function we got (but it works at least)
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
		# The little comment at the end
		return resp + " Little idiot."
	else:
		# The "error" message (What ? We got errors in our amazing code ?)
		return "I don't what you're talking about, human."

