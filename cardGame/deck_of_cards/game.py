from classes.deck import Deck

bicycle = Deck()

bicycle.show_cards()


# action = input("What do you want to do?")
# if(action == "draw"):
#     newCard = bicycle.pickCard()

def fight(currentCard):
    bicycle.fight(player, currentCard)
    newCard = currentCard + 1
    goAgain = input("Do you want to fight again?")
    if(len(bicycle.hands[player]) > newCard):
        if(goAgain == ""  or goAgain == "yes"):
            fight(newCard)
    else:
        winOrMore = input("Looks like you wanted to fight again, but you didn't have any more cards... did you want to add more cards or check if you won?\nChoices: end    add\n")
        if(winOrMore == "end"):
            playerPoints = int(bicycle.hands[player + 'points'])
            computerPoints = int(bicycle.hands['computerpoints'])
            print("Your points: %s\nEnemy Points: %s" %(playerPoints, computerPoints))
            if(bicycle.hands[player + 'points'] > bicycle.hands['computerpoints']):
                print("WOW! You beat RNG! Grats mate...")
            elif(bicycle.hands[player + 'points'] < bicycle.hands['computerpoints']):
                print("Looks like you didn't win... maybe try harder next time")
            else:
                print("WHATTTTT...........\ny-you tied?")
            playAgain = input("Wanna play again?")
            if(playAgain == "yes"):
                bicycle.refreshDeck()
                amntOfPoints = input("How many cards do you want?")
                bicycle.newHand(int(amntOfPoints), player)
                bicycle.newHand(int(amntOfPoints), "computer")
                fight(0)
            else:
                print("well...\nThis is awko taco")
        elif(winOrMore == "add"):
            bicycle.refreshDeck()
            amntOfPoints = int(input("How many cards do you want?"))
            bicycle.newHand(amntOfPoints, player)
            bicycle.newHand(amntOfPoints, "computer")
            fight(0)

deal = input("lmk when you want to start the game...")
if(deal == "start"):
    player = input("What's your name?")
    sizeOfHand = input("How many cards do you want?")
    if(int(sizeOfHand) > 25):
        sizeOfHand = input("Save some for the rest of us!")
    bicycle.newHand(int(sizeOfHand), player)
    bicycle.newHand(int(sizeOfHand), "computer")
    wantToFight = input("Are you ready to fight?")
    if(wantToFight == "yes" or wantToFight == ""):
        fight(0)

