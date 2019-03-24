import random
print("I am thinking of a number between 1 and 10.")
ask = "yes"
while ask == 'yes':
    num = random.randint(1, 10)
    for x in range (5):
        use =input("Take a guess :")
        while not use.isdigit() or not 0<int(use)<11:
            print("Wrong value, re-enter:")
            use =input("Take a guess :")
        user = int(use)
        while user>num or user<num:
            if x == 4 and user != num:
                print("You guessed wrong, the number I was thinking of was",num)
                ask = str(input("Enter yes to try again else enter no to stop:"))
                break
            if user>num:
                print("Your guess is too high.")
                break
            if user<num:
                print("Your guess is too low.")
                break
        else:
            print("Good job, you got it with",x+1,"guesses")
            ask = "no"
            break

