from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.vccquiz
quizzes = db.quizzes


class ActionGiveTacticQuiz(Action):

    def name(self) -> Text:
        return "action_give_tactic_quiz"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rand_id = random.randint(0,3335)
        quiz = quizzes.find_one({"_id":rand_id})
        dispatcher.utter_message(text=quiz["fen"])

        return []

class ActionCheckAnswer(Action):
    def name(self):
        return "action_check_answer"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="check answer")

        return [SlotSet("answer_quiz",None)]

class ActionGiveAnswer(Action):
    def name(self):
        return "action_give_answer"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="give answer")

        return []
