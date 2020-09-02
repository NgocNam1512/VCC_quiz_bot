## happy path
* greet
  - utter_greet
  - utter_iamabot
  - utter_suggest_feature

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## praise
* praise
  - utter_thanks

## thanks
* thanks
  - utter_welcome

## tatic
* tactic_quiz
  - action_give_tactic_quiz
* answer_quiz
  - action_check_answer

## tactic give up
* tactic_quiz
  - action_give_tactic_quiz
* give_up
  - action_give_answer

## tactic give up after wrong
* tactic_quiz
  - action_give_tactic_quiz
* answer_quiz
  - action_check_answer
* give_up
  - action_give_answer