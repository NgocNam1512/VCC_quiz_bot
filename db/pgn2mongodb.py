from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.vccquiz
quizzes = db.quizzes

with open("test_output.txt", "w") as writer:
    with open("data1.pgn") as reader:
        lines = reader.readlines()
        fen = ""
        answer = ""
        idx = 1
        for line in lines:
            if line[:4] == "[FEN":
                fen = line 
            if line[:2] == "1.":
                answer = line
                doc = {"_id":idx, "fen":fen.split("\"")[1], "answer":answer}
                quizzes.insert_one(doc)
                idx += 1
        
reader.close()
writer.close()
