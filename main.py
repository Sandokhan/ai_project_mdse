binAmount = [0 if i in (6, 13) else 4 for i in range(14)]

playing = True
playerOne = True
msgCode = 0
giveawayPile = -1
lastRecipient = -1
chooseBin = -1

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

    # giveawayPile = 0
    if int(chooseBin) >= 0:
        giveawayPile = binAmount[chooseBin]
        binAmount[chooseBin] = 0
        if int(giveawayPile) <= 0:
            msgCode = -1  # empty bin was chosen

    recipient = chooseBin + 1
    while int(giveawayPile) > 0:
        if playerOne and int(recipient) == 13:
            recipient = 0
        if not playerOne and int(recipient) == 6:
            recipient = 7

        binAmount[recipient] = int(binAmount[recipient]) + 1
        giveawayPile = int(giveawayPile) - 1

        if int(giveawayPile) == 0:
            lastRecipient = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0

    if playerOne and int(lastRecipient) == 6:
        playerOne = True
    elif playerOne and int(binAmount[lastRecipient] == 1) and int(lastRecipient) < 6:
        binAmount[6] = int(binAmount[6]) + int(binAmount[lastRecipient]) + int(binAmount[12 - int(lastRecipient)])
        binAmount[lastRecipient] = 0
        binAmount[12 - int(lastRecipient)] = 0
        playerOne = not playerOne
    elif not playerOne and int(lastRecipient) == 13:
        playerOne = False
    elif not playerOne and int(binAmount[lastRecipient] == 1) and int(lastRecipient) > 6:
        binAmount[13] = int(binAmount[13]) + int(binAmount[lastRecipient]) + int(binAmount[12 - int(lastRecipient)])
        binAmount[lastRecipient] = 0
        binAmount[12 - int(lastRecipient)] = 0
        playerOne = not playerOne
    elif int(msgCode) >= 0:
        playerOne = not playerOne

    # check for the end of the game
    sideOne = 0
    sideTwo = 0
    for j in range(6):
        sideOne = int(sideOne) + int(binAmount[j])
        sideTwo = int(sideTwo) + int(binAmount[j+7])

    if int(sideOne) == 0 or int(sideTwo) == 0:
        playing = False
        binAmount[6] = int(binAmount[6]) + int(sideOne)
        binAmount[13] = int(binAmount[13]) + int(sideTwo)
        for k in range(6):
            binAmount[k] = 0
            binAmount[k+7] = 0
# end while loop
print("")
print("The Game is Over!")
if int(binAmount[13]) < int(binAmount[6]):
    print("Player One has wont the game!")
elif int(binAmount[13]) > int(binAmount[6]):
    print("Player One has wont the game!")
else:
    print("The game ended in a tie.")
print("")

for key, element in enumerate(binAmount):
    binAmount[key] = int(binAmount[key])
    if int(binAmount[key]) < 10:
        binAmount[key] = " " + str(binAmount[key])
    else:
        binAmount[key] = str(binAmount[key])
print('+----+----+----+----+----+----+----+----+')
print('|    | ' + binAmount[12] + ' | ' + binAmount[11] + ' | ' + binAmount[10] + ' | ' + binAmount[9] + ' | ' +
      binAmount[8] + ' | ' + binAmount[7] + ' |    |')
print('+ ' + binAmount[13] + ' +----+----+----+----+----+----+ ' + binAmount[6] + ' +')
print('|    | ' + binAmount[0] + ' | ' + binAmount[1] + ' | ' + binAmount[2] + ' | ' + binAmount[3] + ' | ' +
      binAmount[4] + ' | ' + binAmount[5] + ' |    |')
print('+----+----+----+----+----+----+----+----+')
