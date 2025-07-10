import random
from random import choice
pickCardNo = int(input('Pick a card number between 2 to 10: '))
pickCardSuit = str(input('Pick a suit of cards: '))
legalSuits = ["Hearts", "Diamonds", "Spades", "Clubs", "hearts", "diamonds", "spades", "clubs"]
while not 2 <= pickCardNo <= 10:
  pickCardNo = int(input('Only numbers between 2 to 10: '))
while pickCardSuit not in legalSuits:
  print ("Choose a suit from the list: " + str(legalSuits))
  pickCardSuit = input('I choose: ')

#BadMagician chooses random card and has to get it wrong
cardNo = random.randint(2,10)
cardSuit = choice(legalSuits)
if (cardSuit.lower() == pickCardSuit.lower()) and (cardNo == pickCardNo):
  print("Uh oh, Bad Magician has failed its desitny. Your card was the " + str(cardNo) + ' of ' + str(cardSuit) + '...')
else:
 print("Mwahahahaha \nMWAHAHAHAHA")
 print ("The one, the only Bad Magician strikes again!")
 print ('Your card WAS NOT the ' + str(cardNo) + ' of ' + str(cardSuit) + '!')
