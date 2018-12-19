#!/usr/bin/env python2
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_START = "bkouw:Open-Twitter-friends"
INTENT_NEXT = "bkouw:Next-question"
INTENT_STOP = "bkouw:Stop_the_twitter_feed"
INTENT_ARTICLE = "bkouw:article_open"

INTENT_FILTER_GET_ANSWER = [
    INTENT_NEXT,
    INTENT_STOP,
    INTENT_ARTICLE
]

def feed():

    question = "Julia Felt of her bike"

    return question


def user_request_twitter(hermes, intent_message):
    session_id = intent_message.session_id

    # parse input message, NOTE extra space to append question
    friends = int(intent_message.slots.friends.first().value)
    if friends == "friends":
        response = "Opening your friends Twitter feed "
    elif friends == "followers":
        response = "Opening your followers Twitter feed "
    else:
        response = "I can only give a positive number of questions."
        hermes.publish_end_session(session_id, response)

    # create first question
    feed()

    hermes.publish_continue_session(session_id, response + question, INTENT_FILTER_GET_ANSWER)


def user_quits(hermes, intent_message):
    session_id = intent_message.session_id

    # clean up
    del SessionsStates[session_id]
    response = "Alright. Let's play again soon!"

    hermes.publish_end_session(session_id, response)

with Hermes(MQTT_ADDR) as h:

    hermes.publish_continue_session(session_id, "bla", INTENT_FILTER_GET_ANSWER)
    h.subscribe_intent(INTENT_START, user_request_twitter) \
        .subscribe_intent(INTENT_STOP, user_quits) \
        .start()
