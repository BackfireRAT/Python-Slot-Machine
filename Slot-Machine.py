import os
from random import randint
import time
def DigitCheck(String, WantedLen, AddChar, Direct):
    while True:
        count = list(String)
        if (len(count) < WantedLen):
            if (Direct == "front"):
                String = AddChar + String
            else:
                String = String + AddChar
        else:
            if (len(count) == WantedLen):
                break
            else:
                if (len(count) > WantedLen):
                    print("String too big")
                    raw_input("Enter any key to exit : ")
    return String
def Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3):
    os.system('cls')
    print("-------------------------------------------------------------------")
    print("|-----------------------------------------------------------------|")
    print("|                                                                 |")
    print("|         __.--~~.,-.__                   __.--~~.,-.__           |")
    print("|   `~-._.-(`-.__`-.                `~-._.-(`-.__`-.              |")
    print("|           \    `~~`                       \    `~~`             |")
    print("|      .--./ \                         .--./ \                    |")
    print("|     /#   \  \.--.                   /#   \  \.--.               |")
    print("|     \    /  /#   \                  \    /  /#   \              |")
    print("|      '--'   \    /                   '--'   \    /              |")
    print("|              '--'                            '--'               |")
    print("|                                                                 |")
    print("|-----------------------------------------------------------------|")
    print("-------------------------------------------------------------------")
    print("|-----------------------------------------------------------------|")
    print("|         -------      -------      -------                       |")
    print("|         |     |      |     |      |     |    Bet Amount :  " + str(Bet) + "   |") # 2
    print("| Payline-|  " + Bar1 + "  |------|  " + Bar2 + "  |------|  " + Bar3 + "  |    Credits    : " + str(Credits) + "   |") # 3
    print("|         |     |      |     |      |     |    Win Amount : " + str(Win) + "   |") # 3
    print("|         -------      -------      -------                       |")
    print("|                                              --------------     |")
    print("|  --------------------------                  | __________ |     |")
    print("|  | " + Status  +        " |                  --------------     |")
    print("|  --------------------------                  ^   Collect  ^     |")
    print("|                                                  Ticket         |")
    print("|-----------------------------------------------------------------|")
    print("-------------------------------------------------------------------")
    print("|  ----------   --------   ---------   --------     ------------  |")
    print("|  |        |   |   2  |   |       |   |      |     |          |  |")
    print("|  | Change |   | Cash |   | Bet 1 |   | Spin |     | Play Max |  |")
    print("|  |    1   |   |  Out |   |   3   |   |   4  |     |     5    |  |")
    print("|  |--------|   |------|   |-------|   |------|     |----------|  |")
    print("|                                                                 |")
    print("|-----------------------------------------------------------------|")
    print("-------------------------------------------------------------------")
    print("|-----------------------------------------------------------------|")
    print("| 6           This Machine                     ---------------    |")
    print("|           Accepts Tickets    OR          >>  | - - - - - - |    |")
    print("|  1$   5$   10$   20$   50$  100$ Bills       ---------------    |")
    print("|-----------------------------------------------------------------|")
    print("-------------------------------------------------------------------")
    print("|-----------------------------------------------------------------|")
    print("|                                                                 |")
    print("|         __.--~~.,-.__                   __.--~~.,-.__           |")
    print("|   `~-._.-(`-.__`-.                `~-._.-(`-.__`-.              |")
    print("|           \    `~~`                       \    `~~`             |")
    print("|      .--./ \                         .--./ \                    |")
    print("|     /#   \  \.--.                   /#   \  \.--.               |")
    print("|     \    /  /#   \                  \    /  /#   \              |")
    print("|      '--'   \    /                   '--'   \    /              |")
    print("|              '--'                            '--'               |")
    print("|                                                                 |")
    print("|-----------------------------------------------------------------|")
    print("-------------------------------------------------------------------")
Bet = "00"
Credits = "000"
Win = "000"
Status = "Add 0.25$ to Start"
Status = DigitCheck(Status, 22, " ", "back")
Bar1 = "7"
Bar2 = "7"
Bar3 = "7"
while True:
    Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
    Action = raw_input("Please enter an action : ")
    if (Action == "1"):
        Bet = "00"
        if ((int(Credits) * 25) > 5000):
            Status = "Call Attendant!"
            Status = DigitCheck(Status, 22, " ", "back")
            Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
            time.sleep((60 * 60) * 24)
        else:
            Status = "Change $" + str((int(Credits) * 25) / float(100))
            Status = DigitCheck(Status, 22, " ", "back")
            Credits = "000"
            Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
    else:
        if (Action == "2"):
            Bet = "00"
            if ((int(Credits) * 25) > 40000):
                Status = "Call Attendant!"
                Status = DigitCheck(Status, 22, " ", "back")
                Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
                time.sleep((60 * 60) * 24)
            else:
                Status = "CashOut $" + str((int(Credits) * 25) / float(100))
                Status = DigitCheck(Status, 22, " ", "back")
                Credits = "000"
                Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
        else:
            if (Action == "3"):
                if (int(Bet) == 99):
                    Status = "99 is the max bet"
                    Status = DigitCheck(Status, 22, " ", "back")
                    Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
                else:
                    Bet = str(int(Bet) + 1)
                    Bet = DigitCheck(Bet, 2, "0", "front")
                    Status = "Bet increased by 1"
                    Status = DigitCheck(Status, 22, " ", "back")
                Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
            else:
                if (Action == "4"):
                    if (int(Bet) > int(Credits)):
                        Bet = "00"
                        Status = "Not Enough Credits!"
                        Status = DigitCheck(Status, 22, " ", "back")
                    else:
                        Credits = str(int(Credits) - int(Bet))
                        Credits = DigitCheck(Credits, 3, "0", "front")
                        for spin in range(9):
                            Bar1 = str(randint(1, 9))
                            Bar2 = str(randint(1, 9))
                            Bar3 = str(randint(1, 9))
                            Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
                            time.sleep(1 / float(4))
                        Bar1 = str(randint(2, 9))
                        Bar2 = str(randint(2, 9))
                        Bar3 = str(randint(2, 9))
                        if (Bar2 == Bar1):
                            if (Bar2 == Bar3):
                                Credits = str(int(Credits) + int(Bet) * int(Bar1))
                                Credits = DigitCheck(Credits, 3, "0", "front")
                                Win = str(int(Bet) * int(Bar1))
                                Win = DigitCheck(Win, 3, "0", "front")
                                Status = "You Won " + str(int(Bet) * int(Bar1)) + " Credits!"
                                Status = DigitCheck(Status, 22, " ", "back")
                                Bet = "00"
                            else:
                                Status = "You Lose!"
                                Status = DigitCheck(Status, 22, " ", "back")
                        else:
                            Status = "You Lose!"
                            Status = DigitCheck(Status, 22, " ", "back")
                        Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
                else:
                    if (Action == "5"):
                        if (int(Credits) > 99):
                            Bet = "99"
                        else:
                            Bet = str(int(Credits))
                            Bet = DigitCheck(Bet, 2, "0", "front")
                        Credits = str(int(Credits) - int(Bet))
                        Credits = DigitCheck(Credits, 3, "0", "front")
                        for spin in range(9):
                            Bar1 = str(randint(1, 9))
                            Bar2 = str(randint(1, 9))
                            Bar3 = str(randint(1, 9))
                            Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
                            time.sleep(1 / float(4))
                        Bar1 = str(randint(2, 9))
                        Bar2 = str(randint(2, 9))
                        Bar3 = str(randint(2, 9))
                        if (Bar2 == Bar1):
                            if (Bar2 == Bar3):
                                Credits = str(int(Credits) + int(Bet) * int(Bar1))
                                Credits = DigitCheck(Credits, 3, "0", "front")
                                Win = str(int(Bet) * int(Bar1))
                                Win = DigitCheck(Win, 3, "0", "front")
                                Status = "You Won " + str(int(Bet) * int(Bar1)) + " Credits!"
                                Status = DigitCheck(Status, 22, " ", "back")
                                Bet = "00"
                            else:
                                Status = "You Lose!"
                                Status = DigitCheck(Status, 22, " ", "back")
                        else:
                            Status = "You Lose!"
                            Status = DigitCheck(Status, 22, " ", "back")
                        Show_Machine(Bet, Credits, Win, Status, Bar1, Bar2, Bar3)
                    else:
                        if (Action == "Dev"):
                            Bet = "00"
                            Credits = str(input("Enter Credits : "))
                            Credits = DigitCheck(Credits, 3, "0", "front")
                            Win = "000"
                            Status = "Dev Chip Set"
                            Status = DigitCheck(Status, 22, " ", "back")
                            Bar1 = str(input("Enter Bar 1 : "))
                            Bar2 = str(input("Enter Bar 2 : "))
                            Bar3 = str(input("Enter Bar 3 : "))
                        else:
                            if (Action == "6"):
                                Insert = input("What dollar value? : ")
                                try:
                                    Credits = str(int(Credits) + ((Insert * 100) / 25))
                                    Credits = DigitCheck(Credits, 3, "0", "front")
                                except:
                                    print("Invalid input!")
