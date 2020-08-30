with open("test_output.txt", "w") as writer:
    with open("data1.pgn") as reader:
        lines = reader.readlines()
        fen = ""
        answer = ""
        for line in lines:
            if line[:4] == "[FEN":
                fen = line 
            if line[:2] == "1.":
                answer = line
                writer.writelines(fen.split("\"")[1])
                writer.write(answer)
        
reader.close()
writer.close()