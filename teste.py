

binAmount = [1,1,0,1,1,0]
oponent_recipient = 5 - 1 - 1
if (binAmount[1] == 1 and binAmount[oponent_recipient] > 0):
            capture = True
            binAmount[2] += binAmount[1] + binAmount[oponent_recipient]
            binAmount[1] = 0
            binAmount[oponent_recipient ] = 0 

print (binAmount[oponent_recipient])