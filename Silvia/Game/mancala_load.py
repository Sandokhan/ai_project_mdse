import numpy as np

pit_init = int(input("\n" + "Enter number of pits: "))
seed = int(input("Enter number of seeds: "))
pit=pit_init *2 +2
store1 = pit_init
store2 = pit -1


binAmount = np.array([seed]*pit)
#binAmount2 = np.array([seed]*pit)

binAmount[store1] = 0
binAmount[store2] = 0


playing = True
playerOne = False
invalide_bin = False
message = 0
give_away =0

while(playing):
    
    if playerOne and message == 0:
        message = "Player One's turn "
    elif not(playerOne) and message == 0:
        message = "Player Two's turn "
    else:
        message = "Invalide input, Try again"

    print ("\n" +message )
    message = 0
    line_1 =("|    | ")
    line_2 =("|    | ")
    line_3 = ("+ ")
    pit_head_1= "    "
    pit_head_2= "    "

    #i= pit-1
    #for element in reversed(binAmount):
    for i in range(pit, pit_init -1, -1):
        #binAmount[i] = int(binAmount[i])
        if i > store1  and i < store2:
            if i < 10:
                pit_head_1+= "    " + str(i)
            else :
                pit_head_1+= "   " + str(i)

            if binAmount[i] <10:
                line_1 += " " + str(binAmount[i]) +" | "
            else:
                line_1 += str(binAmount[i]) +" | "
        elif  i == store1  :
            line_1 +=  "   |"
            if binAmount[i] <10:
                line_3 += " " +str(binAmount[store1]) +"  +" 
            else :
                line_3 += " " +str(binAmount[store1]) +" +" 

        elif i == store2:
            if binAmount[i] <10:
                line_3 += " " + str(binAmount[i]) +" +" +"----+"* pit_init
            else:
                line_3 += str(binAmount[i]) +" +" +"----+"* pit_init
            
        
        #i -=1

    #for i, element in enumerate(binAmount):
    for i in range (pit_init+1):
        binAmount[i] = int(binAmount[i])
        if  i < store1 : 
            if i < 10:
                pit_head_2+= "    " + str(i)
            else :
                pit_head_2+= "   " + str(i)

            if binAmount[i] <10:
                line_2 += " " + str(binAmount[i]) +" | "
            else:
                line_2 += str(binAmount[i]) +" | " #binAmount[i]

        elif  i == store1 :
            line_2 +=  "   |"
            

    
    if not(playerOne):
        print("\n" + pit_head_1)


    corner = store1 +1
    corner_2 = store1 -1
    print("+----+" + "----+" * corner + "\n" + line_1 + "\n" + 
          line_3 + "\n" + line_2 + "\n" + "+----+" + "----+" * corner  )
 
    if playerOne:
        print( pit_head_2  )

     # Validate the binChosen :
    UserInput = input("\n" + "Enter 'q' to quit the game or your next move to continue: ")

    if UserInput == 'q':
        playing = False
        break
    else :
        binChosen = int(UserInput)
        if (binAmount[binChosen] ==0):
            message = -1
        else:
            if playerOne :
                for i, element in enumerate(binAmount):
                    if binChosen == i and i < store1 and binAmount[i] !=0 :
                        give_away = binAmount[binChosen]
                        binAmount[binChosen] = 0 
                            
            elif not(playerOne):
                for i, element in enumerate(binAmount):
                    if binChosen == i and i < store2  and i > store1 and binAmount[i] !=0 :
                        give_away = binAmount[binChosen]
                        binAmount[binChosen] = 0

    recipient = binChosen + 1
    while (give_away > 0) :
        if playerOne and recipient == store2:
            recipient = 0
        if not(playerOne) and recipient == store1:
            recipient = 0
        binAmount[recipient] += 1
        give_away -=1
        if give_away == 0:
            last_recipient = recipient
        else :
            recipient += 1
            if recipient > store2:
                recipient = 0

    if (playerOne and binAmount[last_recipient]== store1):
        playerOne = True
    elif (playerOne and binAmount[last_recipient] == 1 and last_recipient < store1):
        binAmount[store1] += binAmount[last_recipient] + binAmount[store2 - 1 - last_recipient]
        binAmount[last_recipient] = 0
        binAmount[store2 - 1 - last_recipient] = 0
        playerOne = not(playerOne)
    elif (not(playerOne) and last_recipient == store2):
        playerOne = False
    elif (not(playerOne) and binAmount[last_recipient] == 1 and last_recipient > store1):
        binAmount[store2] += binAmount[last_recipient] + binAmount[store2 - 1 - last_recipient]
        binAmount[last_recipient] = 0
        binAmount[store2 - 1 - last_recipient] = 0
        playerOne = not(playerOne)
    elif (message >= 0):
        playerOne = not(playerOne)  

    
    # Creating the end of game 
    sideOne = 0
    sideTwo = 0
    for j in range (store1) :
        sideOne += binAmount[j]
        sideTwo += binAmount[j + store1 +1]

    if sideOne == 0 or sideTwo == 0 :
        playing = False
        binAmount[store1] += sideOne
        binAmount[store2] += sideTwo
        for k in range (store1):
            binAmount[k] = 0
            binAmount[k+store1+1] = 0

# end while loop
print ("\n" +"Game Over!")
if binAmount[store1] > binAmount[store2]:
    print("Player One Won!")
if binAmount[store1] < binAmount[store2]:
    print("Player Two Won!")
else :
    print("It's a tie.")
        

       







        

        




