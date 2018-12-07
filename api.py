# Let's get this party started!
import falcon
import urllib.parse
import main


# We let the default route of Falcon, because why not
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

# We mixed the spaces and indent here, but Python seems fine, so who care ?
class ChatRessource(object):
	def on_post(self, req, resp):
		data = urllib.parse.parse_qs(req.stream.read().decode())
		if "msg" in data:
			msg = data['msg'][0]
			# I'm a teapot :)
			resp.status = falcon.HTTP_418
			resp.body = main.compute(msg)
		else:
			# What a dumb guy
			resp.status = falcon.HTTP_400
			resp.body = "no message"

# falcon.API instances are callable WSGI apps
app = falcon.API()

# things to randomly handle
app.add_route('/things', ThingsResource())
app.add_route('/chat', ChatRessource())