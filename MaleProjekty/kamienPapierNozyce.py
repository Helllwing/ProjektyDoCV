import random
randomliczba = random.randint(1,3) - 1

znak = int(input("wybierz swoj znak 0 = papier, 1 = kamien, 2 = nozyce.\n"))
znaki = ["papier", "kamien", "nozyce"]
znakKompa = znaki[randomliczba]
if znak > 2 or znak < 0:
    print("invalid number")
else:
    print("            ")
if znak == 0:
    {
        
        print(znaki[0])
    }
elif znak > 2 or znak < 0:
    {
        
        
    }  
elif znak == 1:
    {
        print(znaki[1])
    }
elif znak == 2:
    {
        print(znaki[2])
    }


print("VS")
print(znakKompa)
print("            ")

if znak == randomliczba:
    {
        print("DRAW")
    }
elif znak == 2 and randomliczba == 0:
    {
        print("wygrales")
    }
elif znak == 2 and randomliczba == 1:
    {
        print("przegrales")
    }
elif znak == 1 and randomliczba == 0:
    {
        print("przegrales")
    }
elif znak == 1 and randomliczba == 2:
    {
        print("wygrales")
    }
elif znak == 0 and randomliczba == 1:
    {
        print("wygrales")
    }
elif znak == 0 and randomliczba == 2:
    {
        print("przegrales")
    }  
print("            ")    

