def ticTacToe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    winningLines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  ]            # Diagonals 
    
    def printBoard():
        print()
        print('', board[0], "|", board[1], "|", board[2])
        print("---|---|---")
        print('', board[3], "|", board[4], "|", board[5])
        print("---|---|---")
        print('', board[6], "|", board[7], "|", board[8])
        print()
        
    def getNumber():
        while True:
            number = input()
            try:
                number = int(number)
                if number in range(1, 10):
                    return number
                else:
                    print("\nNumber not on board")
            except ValueError:
                print("\nThat's not a number")
    
    def turn(player):
        placingIndex = getNumber()-1
        if board[placingIndex] == "X" or board[placingIndex] == "O":
            print("\nBox already occupied")
        else:
            board[placingIndex] = player
            
    def checkWin(player):
        for line in winningLines:
            x, y, z = line
            if board[x] == board[y] == board[z] == player:
                print("Player ", player, " wins!\n")
                return True
    def checkDraw():
        for space in board:
            if space != "X" and space != "O":
                return False
        return True
    
    while not end:
        printBoard()
        print("Choose a box Player X")
        turn("X")
        printBoard()
        end = checkWin("X")
        if end:
            break
        
        end = checkDraw()
        if end:
            printBoard()
            print("draw")
            break
        
        print("Choose a box Player O")
        turn("O")
        printBoard()
        end = checkWin("O")
        if end:
            break
        
        
ticTacToe()