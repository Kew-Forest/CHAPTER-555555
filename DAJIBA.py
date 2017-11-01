print("You are an Elfin warrior:")
print("Life: 80	Strength: 76	Speed: 85	Gold: 0")
print("Now")
print("You are in a dungeon and come to a fork.")
print("    1.Right")
print("    2.Left")

newbee = int(input("What is your choice? "))
if newbee== 1:
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("you come to a room with a pot of 200 gold and a magic bracelet which increases your Strength by 10.")
    print("Life: 80	Strength: 760	Speed: 85	Gold: 200")
    print("Inventory Tabs: 1. Magic Bracelet(increases your Strength by 10)")
    print("Then you must go back to the fork and choose again")
    print("You are in a dungeon and come to a fork.")
    print("    1.Right(You had been to)")
    print("    2.Left")
    newbee2 = int(input("What is your choice? "))
    
    if newbee2 == 2:
        print("You are attacked by a Gorgon")
        print("Life: 50	Strength: 85	Speed: 10	Gold: 500")
        print("    1.Fight")
        print("    2.Flee")
        sb = int(input("What is your choice? "))
        if sb == 2:
            print("You retreat back to the fork")
        if sb == 1 :
            print("you win collect the gold and move on")
            print("You get gold:500")
            print("Life: 80	Strength: 760	Speed: 85	Gold: 700")
            print("Inventory Tabs: 1. Magic Bracelet(increases your Strength by 10)")
            print("")
           
if newbee == 2:
    print("You are attacked by a Gorgon")
    print("Gorgon")
    print("Life: 50	Strength: 85	Speed: 10	Gold: 500")
    
    print("    1.Fight")
    print("    2.Flee")
    newbee4 = int(input("What is your choice"))
    if newbee4 == 2:
        print("You retreat back to the fork")
    if newbee4 ==1:
        print("You lose 50 life point")
        print("    1.Fight")
        print("    2.Flee")
        newbee5 =int(input("What is your choice"))
        if newbee5 ==1:
            print("You lose 50 life point")
            print("Life: 0	Strength: 76	Speed: 85	Gold: 0")
            print("You die")
            print("game over")
        if newbee5 ==2:
            print("You retreat back to the fork")
            print("Life: 30	Strength: 76	Speed: 85	Gold: 0")
            
        

    