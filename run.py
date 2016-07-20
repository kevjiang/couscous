from flask import Flask, request, redirect
import twilio.twiml
import os
from adventure import *

app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""

#     resp = twilio.twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)

# Try adding your own number to this list!

# callers = {
#     "+17816402658": "Kevin",
#     "+14158675310": "Boots",
#     "+14158675311": "Virgil",
# }

# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond and greet the caller by name."""
#     print 'hi'
#     from_number = request.values.get('From', None)
#     print request.values
#     if from_number in callers:
#         message = callers[from_number] + ", thanks for the message!"
#     else:
#         message = "Monkey, thanks for the message!"

#     resp = twilio.twiml.Response()
#     resp.message(message)

#     return str(resp)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    body = body.lower()
    print body

    if body == 'start':
        message = classroom0()
    elif body == 'take a nap':
        message = take_nap()
    elif body == 'take notes':
        message = take_notes()
    elif body == 'turn around':
        message = turn_around()
    elif body == 'notes':
        message = notes()
    else:
        message = rogue()
 
    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.  For Heroku deployment
	# http://stackoverflow.com/questions/17260338/deploying-flask-with-heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)