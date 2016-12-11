import json, requests, random, re
from facebookMessengerConfig import PAGE_ACCESS_TOKEN, VERIFY_TOKEN
from pprint import pprint
from arduino import dot, slash
from apiaiConfig import shaktiman

lights = {'bedroomon': ["""Hello! Manish nice to see you again :) and I am turning on the bedroom lights. Thank you"""],
          'bedroomoff': ["""Hello! Manish nice to see you again :) and I am turning off the bedroom lights. Good Bye"""],
          'kitchenon': ["""Hello! Manish nice to see you again :) and I am turning on the bedroom lights. Thank you"""],
          'kitchenoff': ["""Hello! Manish nice to see you again :) and I am turning off the bedroom lights. Good Bye"""],
          'washroomon': ["""Hello! Manish nice to see you again :) and I am turning on the bedroom lights. Thank you"""],
          'washroomoff': ["""Hello! Manish nice to see you again :) and I am turning off the bedroom lights. Good Bye"""],
          'kidsroomon': ["""Hello! Manish nice to see you again :) and I am turning on the bedroom lights. Thank you"""],
          'washroomoff': ["""Hello! Manish nice to see you again :) and I am turning off the bedroom lights. Good Bye"""],
}


# Helper function
def post_facebook_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', recevied_message).lower().split()
    joke_text = ''
    for token in tokens:
        if token in lights:
            joke_text = random.choice(lights[token])
            break
    if not joke_text:
        joke_text = "I didn't understand! Send 'bedroom on/off', 'kitchen on/off', 'washroom on/off' for switching lights!"
        slash()
    user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    user_details = requests.get(user_details_url, user_details_params).json()
    joke_text = 'Hey ' + user_details['first_name'] + '..! ' + joke_text

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())
    dot()
    slash()




# shaktiman()