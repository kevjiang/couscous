# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from nyt_scraper import *
from time import *

# Find these values at https://twilio.com/user/account
account_sid = "AC3b871b8dc7bb3785cddda6fd9ad271fe"
auth_token = "6b65df96c48e7d3b99ac574d872af60a"
client = TwilioRestClient(account_sid, auth_token)

needle = "Trump"
total_nyt_count = nyt_all_text_count(needle)

body_text = "%s: nytimes.com homepage currently includes %d mentions of %s" % (strftime("%Y-%m-%d %I:%M:%S"), total_nyt_count, needle)

message = client.messages.create(to="+17816402658", from_="+17815705388", body=body_text)