import time, random

money = 1000
timeout = 120.0

def play():
    print("what is your game? Red? Black? Number from 1 till 35?")
    game=input()
    game=game.upper()
    roulette=random.randint(1,35)
    print("Wheel is spinning..."+str(roulette))
    if game.isnumeric() and int(game)==roulette:
        return 35
    elif (game in ["RED","R"] and roulette%2==1) or (game in ["BLACK","B"] and roulette%2==0):
        return 2
    else:
        return 0

clock = time.time()

while money > 0:
    print("Are you in?")
    timer=time.time() - clock
    print("clock is ticking...",int(timer))
    if timer > timeout:
        break
    answer = input()
    if answer.upper() in ["YES","Y"]:
        print("How much money do you bet?")
        bet=input()
        if bet.isnumeric():
            bet=int(bet)
            money-=bet
        else:
            continue
        if bet>money:
                print("You don't have that kind of money")
                continue
        result=play()
        money=money+bet*result
        print("Your winning is " + str(bet*result),"Money = "+str(money))
        continue
    elif answer.upper() in ["NO","N"]:
        break
    else:
        continue
timer=time.time() - clock
if timer > timeout:
    print("time is out")
    money=0
print("Your money = "+str(money))
if money == 0:
    print("You lost!")
print("Thanks for the game")











