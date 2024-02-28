import random,sys

print("Papier, Kamień, Nożyce")

wins=0
losses=0
ties=0

while True:
    print('%s zwycięstw,%s porażek,%s remisów'%(wins,losses,ties))
    while True:
        print('Podaj swój wybór :(K)amień, (P)apier, (N)ożyce, lub (W)yjście')
        playerChoice= input().lower()
        if playerChoice=='w':
            print("Dziękuję za grę.\n Wynik gry to: ","Wygrane:",wins,"Przegrane:",losses,"Remisy:",ties)
            sys.exit()
        if playerChoice== 'k'or playerChoice== 'p' or playerChoice=='n':
            break
        print('Wpisz literę k,p,n lub w.')

    #wybór gracza
    if playerChoice=='k':
        print('Kamień kontra...')
    elif playerChoice=='p':
        print('Papier kontra...')
    elif playerChoice=='n':
        print('Nożyce kontra...')

    #wybór random komputera
    
    randomNumber=random.randint(1,3)
    if randomNumber==1:
        computerMove='k'
        print('Kamień')
    elif randomNumber==2:
        computerMove='p'
        print('Papier')
    elif randomNumber==3:
        computerMove='n'
        print('Nożyce ')
    
    if playerChoice==computerMove:
        print("Remis")
        ties=ties+1
    elif playerChoice=='k'and computerMove=='n'or playerChoice=='p'and computerMove=='k' or playerChoice=='n'and computerMove=='p':
        print("Wygrałeś")
        wins=wins+1
    
    else:
        print("Przegrałeś")
        losses=losses+1