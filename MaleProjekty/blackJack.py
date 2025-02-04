import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
loop = True
BlackJack = 21
playerDeck = []
compDeck = []

def RandomCard():
    random_item = random.choice(cards)
    newCard = cards[random_item]
    return newCard
choice = input("do u wanna play black jack? y =yes, n = no " )
while loop:
    if choice == "y":
        newCard = RandomCard()
        playerDeck.append(newCard)
        newCard = RandomCard()
        playerDeck.append(newCard)
        newCard = RandomCard()
        compDeck.append(newCard)
        newCard = RandomCard()
        compDeck.append(newCard)
        sumaP = int(playerDeck[0]) + int(playerDeck[1])
        sumaC = int(compDeck[0]) + int(compDeck[1])
        print("twoje karty")
        print(playerDeck)
        print(sumaP)
        print("-------")
        print("karty przeciwnika")
        print(compDeck)
        print(sumaC)
        take = input("do u wanna take card or pass? c = card, p = pass ")
        while take == "c":
            newCard = RandomCard()
            playerDeck.append(newCard)
            newCard = RandomCard()
            compDeck.append(newCard)
            i = 2
            sumaP = sumaP + int(playerDeck[i])
            sumaC = sumaC + int(compDeck[i])
            i = i + 1
            print("dobierasz karte")
            print(playerDeck)
            print(sumaP)
            print("-------")
            print("komputer dobiera karte")
            print(compDeck)
            print(sumaC)
            if sumaP == BlackJack:
                print("u win")
                take = "p"
            elif sumaP > BlackJack:
                print("u lose")
                take = "p"
            elif sumaC == BlackJack:
                print("u lose")
                take = "p"
            elif sumaC > BlackJack:
                print("u win")
                take = "p"
            elif sumaC < BlackJack and sumaP < BlackJack:
                take = input("do u wanna take card or pass? c = card, p = pass ")
        playerDeck = []
        compDeck = []
        again = input("do u wanna play again? y or n ")
        if again == "n":
            loop = False
    elif choice =="n":
        loop = False