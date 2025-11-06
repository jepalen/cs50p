def main():
    moves =[]
    while True:
        move = input("Give me your move: ")
        if move == "restart":
            moves.clear()
        elif move == "undo":
            undo = moves.pop() 
            print(f"Undoing move: {undo}")
        else:
            moves.append(move)
        print(moves)

main()