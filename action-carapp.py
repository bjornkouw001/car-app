# #!/usr/bin/env python2
# from hermes_python.hermes import Hermes
#
# MQTT_IP_ADDR = "localhost"
# MQTT_PORT = 1883
# MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))
#
# INTENT_START = "bkouw:Open-Twitter-friends"
# INTENT_NEXT = "bkouw:Next-question"
# INTENT_STOP = "bkouw:Stop_the_twitter_feed"
# INTENT_ARTICLE = "bkouw:article_open"
#
#
# INTENT_FILTER_GET_ANSWER = [
#     INTENT_START,
#     INTENT_NEXT,
#     INTENT_STOP,
#     INTENT_ARTICLE
#
# ]
#
#
# SessionsStates = {}
#
#
# def user_request_twitter(x,y):
#     ans = x+y
#
#     if ans == 4:
#         answer = "Jacob said in his tweet that his car crashed in an wall.  "
#
#     elif ans == 7:
#         answer = "Jessica said her mother cooked some pasta  "
#
#     else:
#         answer = "Henk said he his car was broken."
#
#     return answer
#
#
#
# def user_request_quiz(hermes, intent_message):
#     session_id = intent_message.session_id
#
#     # parse input message, NOTE extra space to append question
#     friends = int(intent_message.slots.friends.first().value)
#     if friends == "followers":
#         response = "Nice let's go to the first tweet  "
#         user_request_twitter(1,3)
#     elif friends == "Best friends":
#         response = "Nice let's go to the first tweet. "
#         user_request_twitter(2,5)
#     elif friends == "friends":
#         response = "Nice let's go to the first tweet. "
#         user_request_twitter(6,2)
#
#     else:
#         response = "I can only give a positive number of questions."
#         hermes.publish_end_session(session_id, response)
#
#
#
#
#
#
#
#     # create first question// Hier ga ik mijn Twitter feed aanroepen
#     # question, answer = create_question()
#     #
#     # # initialize session state// hier word de session state gekoppeld aan de session is
#     # session_state = {
#     #     "ans": answer,
#     #     "good": 0,
#     #     "bad": 0,
#     #     "step": 0,
#     #     "n_questions": n_questions
#     # }
#
#     SessionsStates[session_id] = session_state
#
#     hermes.publish_continue_session(session_id, response + question, INTENT_FILTER_GET_ANSWER)
#
#
# # def user_gives_answer(hermes, intent_message):
# #     session_id = intent_message.session_id
# #
# #     # parse input message
# #     answer = intent_message.slots.answer.first().value
# #
# #     # check user answer, NOTE the extra space at the end since we will add more to the response!
# #     if answer == SessionsStates[session_id]["ans"]:
# #         response = "Correct! "
# #         SessionsStates[session_id]["good"] += 1
# #     else:
# #         response = "Incorrect. The answer is {}. ".format(SessionsStates[session_id]["ans"])
# #         SessionsStates[session_id]["bad"] += 1
# #
# #     # create new question or terminate if reached desired number of questions
# #     response, cont = continue_lesson(response, session_id)
# #     if cont:
# #         hermes.publish_continue_session(intent_message.session_id, response, INTENT_FILTER_GET_ANSWER)
# #     else:
# #         hermes.publish_end_session(session_id, response)
# #
# #
# # def user_does_not_know(hermes, intent_message):
# #     session_id = intent_message.session_id
# #
# #     response = "That's quite alright! The answer is {}. ".format(SessionsStates[session_id]["ans"])
# #
# #     # create new question or terminate if reached desired number of questions
# #     response, cont = continue_lesson(response, session_id)
# #     if cont:
# #         hermes.publish_continue_session(intent_message.session_id, response, INTENT_FILTER_GET_ANSWER)
# #     else:
# #         hermes.publish_end_session(session_id, response)
#
#
# def user_quits(hermes, intent_message):
#     session_id = intent_message.session_id
#
#     # clean up
#     del SessionsStates[session_id]
#     response = "Alright. I will stop the Twitter feed"
#
#     hermes.publish_end_session(session_id, response)
#
#
# with Hermes(MQTT_ADDR) as h:
#
#     h.subscribe_intent(INTENT_START, user_request_twitter) \
#         .subscribe_intent(INTENT_STOP, user_quits) \
#         .subscribe_intent(INTENT_DOES_NOT_KNOW, user_does_not_know) \
#         .subscribe_intent(INTENT_ANSWER, user_gives_answer) \
#         .start()



from hermes_python.hermes import Hermes
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_START = "bkouw:Open-Twitter-friends"
INTENT_NEXT = "bkouw:Next-question"
INTENT_STOP = "bkouw:Stop_the_twitter_feed"
INTENT_ARTICLE = "bkouw:article_open"

INTENT_FILTER_GET_ANSWER = [
    INTENT_START,
    INTENT_NEXT,
    INTENT_STOP,
    INTENT_ARTICLE

]


SessionsStates = {}



def the_Tweet():
    twitter_message = "Jesse said he is going to Spain in a few weeks. "

    return twitter_message




def user_request_twitter(hermes, intent_message):
    session_id = intent_message.session_id
    i_friends = int(INTENT_START.slots.friend.first().value)

    if i_friends == "friends":
        response = "Nice opening {} their tweets. ".format(i_friends)


    elif i_friends == "friend":
        response = "Nice opening your {} his tweet ".format(i_friends)


    else:
        response = "Sorry ask again"
        hermes.publish_end_session(session_id, response)

    twitter_message, another_tweet = the_Tweet()

    session_state = {
        "ans": answer,
        "Twitter messages": 0,
        "step": 0,
        "i_friends": i_friends
    }
    SessionsStates[session_id] = session_state

    hermes.publish_continue_session(session_id, response + twitter_message, INTENT_FILTER_GET_ANSWER)



def user_quits(hermes, intent_message):
    session_id = intent_message.session_id

    # clean up
    del SessionsStates[session_id]
    response = "Alright. I will stop the Twitter feed"

    hermes.publish_end_session(session_id, response)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intent(INTENT_START, user_request_twitter) \
        .subscribe_intent(INTENT_STOP, user_quits) \
        .start()
        # .subscribe_intent(INTENT_NEXT, user_wants_next) \
        # .subscribe_intent(INTENT_ARTICLE, user_asks_an_article) \

