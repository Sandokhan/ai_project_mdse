binAmount = [0 if i in (6, 13) else 4 for i in range(14)]

playing = True

playerOne = True

msgCode = 0

while playing:

    if playerOne and msgCode == 0:
        message = "Player 1 turn..."
    elif not playerOne and msgCode == 0:
        message = "Player 2 turn..."
    elif playerOne and msgCode == -2:
        message = 'Invalid input. Try again, Player 1!'
    elif not playerOne and msgCode == -2:
        message = 'Invalid input. Try again, Player 2!'
    elif playerOne and msgCode == -1:
        message = 'You must choose a non-empty bin. Try again, Player 1!'
    elif not playerOne and msgCode == -1:
        message = 'You must choose a non-empty bin. Try again, Player 2!'
    print('\n', message, '\n')
    msgCode = 0

    for key, element in enumerate(binAmount):
        binAmount[key] = int(binAmount[key])
        if int(binAmount[key]) < 10:
            binAmount[key] = " " + str(binAmount[key])
        else:
            binAmount[key] = str(binAmount[key])
    if not playerOne:
        print("        a    b    c    d    e    f")
    print('+----+----+----+----+----+----+----+----+')
    print('|    | ' + binAmount[12] + ' | ' + binAmount[11] + ' | ' + binAmount[10] + ' | ' + binAmount[9] + ' | ' +
          binAmount[8] + ' | ' + binAmount[7] + ' |    |')
    print('+ ' + binAmount[13] + ' +----+----+----+----+----+----+ ' + binAmount[6] + ' +')
    print('|    | ' + binAmount[0] + ' | ' + binAmount[1] + ' | ' + binAmount[2] + ' | ' + binAmount[3] + ' | ' +
          binAmount[4] + ' | ' + binAmount[5] + ' |    |')
    print('+----+----+----+----+----+----+----+----+')
    if playerOne:
        print("        f   e    d    c    b    a")
    print("")

    userInput = input("Choose a bin or enter 'q' to QUIT the game: ")

    if userInput == 'q':
        playing = False
        chooseBin = 0
    elif userInput == 'a' and playerOne:
        chooseBin = 5
    elif userInput == 'b' and playerOne:
        chooseBin = 4
    elif userInput == 'c' and playerOne:
        chooseBin = 3
    elif userInput == 'd' and playerOne:
        chooseBin = 2
    elif userInput == 'e' and playerOne:
        chooseBin = 1
    elif userInput == 'f' and playerOne:
        chooseBin = 0
    # player 2
    elif userInput == 'a' and not playerOne:
        chooseBin = 12
    elif userInput == 'b' and not playerOne:
        chooseBin = 11
    elif userInput == 'c' and not playerOne:
        chooseBin = 10
    elif userInput == 'd' and not playerOne:
        chooseBin = 9
    elif userInput == 'e' and not playerOne:
        chooseBin = 8
    elif userInput == 'f' and not playerOne:
        chooseBin = 7
    else:
        chooseBin = -2
        msgCode = - 2  # invalid entry

    if int(chooseBin) >= 0:
        giveawayPile = binAmount[chooseBin]
        binAmount[chooseBin] = 0
        if int(giveawayPile) <= 0:
            msgCode = -1  # empty bin

    recipient = chooseBin + 1
    while int(giveawayPile) > 0:
        if playerOne and int(recipient) == 13:
            recipient = 0
        if not playerOne and int(recipient) == 6:
            recipient = 7

        binAmount[recipient] = int(binAmount[recipient]) + 1
        giveawayPile = int(giveawayPile) - 1
        recipient = int(recipient) + 1
        if int(recipient) > 13:
            recipient = 0

    playerOne = not playerOne

# end while loop
