import random

    # internal board logic


boardLogic = {1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ",9: " "}

def spawnBoard():

    # a 3 x 3 board
    # add logic into the board using f strings
    gameboard = [[f"{boardLogic.get(1)}|", f"{boardLogic.get(2)}|", f"{boardLogic.get(3)}"],
                ["―――――"],
                [f"{boardLogic.get(4)}|", f"{boardLogic.get(5)}|", f"{boardLogic.get(6)}"],
                ["―――――"],
                [f"{boardLogic.get(7)}|", f"{boardLogic.get(8)}|", f"{boardLogic.get(9)}"]]


    for row in gameboard:
        for item in row:
            print(item, end = "")
        print("")


# declare player 1 and allow them to input X on gameboard
while True:
    spawnBoard()
    playerMove = int(input('Select 1-9 to make your move: '))
    if playerMove > 0 and playerMove < 10:
        boardLogic[playerMove] = "X"
        print('correct value input')
    else:
        print('Please input 1-9')



