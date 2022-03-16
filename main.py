#!/bin/python3

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *
from random import random


AMOUNT = 200
LIKE_THRESHOLD = 0.3 # 70% chance of liking
MESSAGE = '<Your message here 🇺🇦>'
email = "<GOOGLE_EMAIL>"
password = "<GOOGLE_PASSWORD>"

# creates instance of session
session = Session()

# >>> <CHOOSE THE CITY>
session.set_custom_location(latitude=55.762504, longitude=37.6167764) # Moscow
# session.set_custom_location(latitude=59.940117, longitude=29.8145045) # St Petersburg

# login using your google account with a verified email!
session.login_using_google(email, password)

def liking_disliking(amount, like_threshold):
  for i in range(0, amount):
    score = random()

    if (score > like_threshold):
      session.like()
    else:
      session.dislike()


def messaging_new_matches(message, amount=10):
  # Getting matches takes a while, so recommended you load as much as possible from local storage
  # get new matches, with whom you haven't interacted yet
  # Let's load the first 10 new matches to interact with later on.
  # quickload on false will make sure ALL images are stored, but this might take a lot more time
  new_matches = session.get_new_matches(amount=10, quickload=False)
  # get already interacted with matches (matches with whom you've chatted already)
  messaged_matches = session.get_messaged_matches()
  
  # you can store the data and images of these matches now locally in data/matches
  # For now let's just store the messaged_matches
  for match in messaged_matches:
    session.store_local(match)

  # loop through my new matches and send them the first message of the conversation
  for match in new_matches:
    # send pick up line with their name in it to all my matches
    session.send_message(chatid=match.get_chat_id(), message=message)


liking_disliking(AMOUNT, LIKE_THRESHOLD)
messaging_new_matches(MESSAGE)
