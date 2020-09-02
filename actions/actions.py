from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import random
import os

from constants import *
from fen2png import Board, DrawImage
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

        # choose random quiz
        rand_id = random.randint(0,3335)
        quiz = quizzes.find_one({"_id":rand_id})

        print(quiz['fen'].split())
        fen = Board(quiz['fen'].split())
        if fen.isvalid:
            fmt = "png"
            if not os.path.isdir(OUTPUT):
                # Handle if directory is not valid
                os.mkdir(OUTPUT)
                print("Creating new directory: {}".format(OUTPUT))
            boardImg = DrawImage(fen, fmt, OUTPUT, "result")
            boardImg.create()
            boardImg.to_image()
            print(
                "Completed! File created in {}/{}.{}".format(
                    OUTPUT, "result", fmt
                )
            )
        else:
            print("Invalid FEN. No Image file was generated.")

        dispatcher.utter_template('utter_image', tracker, output="./result.png")

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
