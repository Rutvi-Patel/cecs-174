
print("There are currently 20 tickets remaining.")
tickets = 20
ctr = 0
user = 0
while (tickets > 0) and (tickets+user>0):
    user = int(input("How many tickets would you like to purchase? "))
    while (user>4) or ((tickets - user)<0):
        print("Sorry, you can't buy that many.")
        break
    else:
        tickets = tickets - user
        ctr = ctr + 1
        while tickets != 0:
            print("There are currently",tickets,"tickets remaining.")
            break
print("The total number of buyers was",ctr)

