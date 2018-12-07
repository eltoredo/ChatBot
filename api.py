# things.py

# Let's get this party started!
import falcon
import urllib.parse
import main


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

class ChatRessource(object):
	def on_post(self, req, resp):
		data = urllib.parse.parse_qs(req.stream.read().decode())
		if "msg" in data:
			msg = data['msg'][0]
			resp.status = falcon.HTTP_418
			resp.body = main.compute(msg)
		else:
			resp.status = falcon.HTTP_400
			resp.body = "no message"

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/chat', ChatRessource())