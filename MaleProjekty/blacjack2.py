import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
suma = 0 
dalej = True
BlackJack = 21
playerDeck = []
compDeck = []
yes = 1
def randomCard():
    random_item = random.choice(card)
    newCard = card[random_item]
    return newCard
choice = input("do u wanna play black jack? y =yes, n = no " )
while yes == 1:
    
    
    if choice == "y":
        newCard = randomCard()
        playerDeck.append(newCard)
        newCard = randomCard()
        playerDeck.append(newCard)
        newCard = randomCard()
        compDeck.append(newCard)
        newCard = randomCard()
        compDeck.append(newCard)
        sumaP = int(playerDeck[0]) + int(playerDeck[1])
        sumaC = int(compDeck[0]) + int(compDeck[1])
        print(playerDeck)
        print(sumaP)
        print("-------")
        print(compDeck)
        print(sumaC)
        take = input("do u wanna take card or pass? c = card, p = pass")
        if take == "c":
            newCard = randomCard()
            playerDeck.append(newCard)
            suma2p = sumaP + int(playerDeck[2])
            if suma2p > BlackJack:
                print(playerDeck)
                print(suma2p)
                print("u lose")
            elif suma2p == BlackJack:
                print("u win")
            else:
                print(playerDeck)
                print(suma2p)
                print("komputer musi dobrac karte")
                newCard = randomCard()
                compDeck.append(newCard)
                suma2c = sumaC + int(compDeck[2])
                print(compDeck)
                print(suma2c)
                if suma2p < BlackJack:
                    print(take)
                if take == "c":
                    newCard = randomCard()
                    playerDeck.append(newCard)
                    suma3p = suma2p + int(playerDeck[3])
                    print(playerDeck)
                    print(suma3p)
                    if suma3p > BlackJack:
                        print("u lose")
                    elif suma3p == BlackJack:
                        print(" u win")
                    else:
                        print("komputer musi dobrac karte")
                        newCard = randomCard()
                        compDeck.append(newCard)
                        suma3c = suma2c + int(compDeck[3])
                        print(compDeck)
                        print(suma2c)
                elif take == "p":
                    if suma2c > BlackJack:
                         print("u win")
                    elif suma2c == BlackJack:
                     print("u lose")
                    else:
                        print(f"twoja suma {suma2p}")
                        print(f"suma przeciwnika {suma2c}")
                    if suma2p > suma2c:
                        print("u win")
                    else:
                        print("u lose")
        elif take == "p":
                print(playerDeck)
                print(suma2p)
                print("komputer musi dobrac karte")
                newCard = randomCard()
                compDeck.append(newCard)
                suma2c = sumaC + int(compDeck[2])
                print(compDeck)
                print(suma2c)
                if suma2c > BlackJack:
                    print("u win")
                else:
                    print(f"twoja suma {suma2p}")
                    print(f"suma przeciwnika {suma2c}")
                if suma2p > suma2c:
                    print("u win")
                else:
                    print("u lose")      
    
                
    playerDeck = []
    compDeck = [] 
    while dalej:
        again = input("do u wanna play again? y = yes, n = noo")
        if again == "n":
            yes = False
            dalej = False
        elif again == 'y':
            yes = True
            dalej = False
        else:
            print(f"wrong syntax try agaian")
            print(again)
            dalej = True



