from random import *
All_Cards = ['Hearts_6','Diamonds_6','Clubs_6','Spades_6','Hearts_7','Diamonds_7','Clubs_7','Spades_7','Hearts_8','Diamonds_8','Clubs_8','Spades_8','Hearts_9','Diamonds_9','Clubs_9','Spades_9','Hearts_10','Diamonds_10','Clubs_10','Spades_10','Hearts_Jack','Diamonds_Jack','Clubs_Jack','Spades_Jack','Hearts_Queen','Diamonds_Queen','Clubs_Queen','Spades_Queen','Hearts_King','Diamonds_King','Clubs_King','Spades_King','Hearts_Ace','Diamonds_Ace','Clubs_Ace','Spades_Ace']
Hearts = ['Hearts_6','Hearts_7','Hearts_8','Hearts_9','Hearts_10','Hearts_Jack','Hearts_Queen','Hearts_King','Hearts_Ace']
Diamonds = ['Diamonds_6','Diamonds_7','Diamonds_8','Diamonds_9','Diamonds_10','Diamonds_Jack','Diamonds_Queen','Diamonds_King','Diamonds_Ace']
Clubs = ['Clubs_6','Clubs_7','Clubs_8','Clubs_9','Clubs_10','Clubs_Jack','Clubs_Queen','Clubs_King','Clubs_Ace']
Spades = ['Spades_6','Spades_7','Spades_8','Spades_9','Spades_10','Spades_Jack','Spades_Queen','Spades_King','Spades_Ace']
Hearts_Copy = Hearts.copy()
Diamonds_Copy = Diamonds.copy()
Clubs_Copy = Clubs.copy()
Spades_Copy = Spades.copy()
My_Cards = []
for i in range(6):
     Card = choice(All_Cards)
     My_Cards.append(Card)
     All_Cards.remove(Card)
     if Card in Hearts:
          Hearts.remove(Card)
     elif Card in Diamonds:
          Diamonds.remove(Card)
     elif Card in Clubs:
          Clubs.remove(Card)
     else:
          Spades.remove(Card)
print(My_Cards)
Rival_Cards = []
for i in range(6):
     Card = choice(All_Cards)
     Rival_Cards.append(Card)
     All_Cards.remove(Card)
     if Card in Hearts:
          Hearts.remove(Card)
     elif Card in Diamonds:
          Diamonds.remove(Card)
     elif Card in Clubs:
          Clubs.remove(Card)
     else:
          Spades.remove(Card)

Trump_Card = choice(All_Cards)
if Trump_Card in Hearts_Copy:
     Trump_Suit = Hearts_Copy.copy()
elif Trump_Card in Diamonds:
     Trump_Suit = Diamonds_Copy.copy()
elif Trump_Card in Clubs_Copy:
     Trump_Suit = Clubs_Copy.copy()
else:
     Trump_Suit = Spades_Copy.copy()
     
print('Trump card is', Trump_Card)
def Card1(a, b, c):
     global y
     y = str(input('Please, enter a card:'))
     b.remove(y)
     f = 0
     for t in range(len(Hearts_Copy)):
          if Hearts_Copy[t] == y:
               for r in range(t + 1, len(Hearts_Copy)):
                    for w in range(len(c)):
                         if Hearts_Copy[r] == c[w]:
                              print(Hearts_Copy[r])
                              j = Hearts_Copy[r]
                              c.remove(Hearts_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
               
     for t in range(len(Diamonds_Copy)):
          if Diamonds_Copy[t] == y:
               for r in range(t + 1,len(Diamonds_Copy)):
                    for w in range(len(c)):
                         if Diamonds_Copy[r] == c[w]:
                              print(Diamonds_Copy[r])
                              j = Diamonds_Copy[r]
                              c.remove(Diamonds_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
               
               
     for t in range(len(Clubs_Copy)):
          if Clubs_Copy[t] == y:
               for r in range(t + 1,len(Clubs_Copy)):
                    for w in range(len(c)):
                         if Clubs_Copy[r] == c[w]:
                              print(Clubs_Copy[r])
                              j = Clubs_Copy[r]
                              c.remove(Clubs_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
               
     for t in range(len(Spades_Copy)):
          if Spades_Copy[t] == y:
               for r in range(t + 1,len(Spades_Copy)):
                    for w in range(len(c)):
                         if Spades_Copy[r] == c[w]:
                              print(Spades_Copy[r])
                              j = Spades_Copy[r]
                              c.remove(Spades_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break

                    
     z = 0          
     if f == 0:
          if y not in Trump_Suit:
               for g in Trump_Suit:
                    for h in c:
                         if g == h:
                              print(h)
                              j = h
                              z += 1
                              c.remove(h)
                              break
                    if z != 0:
                         break
          else:
               c.append(y)
               
     print(My_Cards)

def Card2():
     s = str(input('Please, enter a card:'))
     if s == "No Card to come" or s == "":
          for i in range(6 - len(My_Cards)):
               l = choice(All_Cards)
               My_Cards.append(l)
               All_Cards.remove(l)
               m = choice(All_Cards)
               Rival_Cards.append(m)
     b.remove(s)
     f = 0
     for t in range(len(Hearts_Copy)):
          if Hearts_Copy[t] == s:
               for r in range(t + 1,len(Hearts_Copy)):
                    for w in range(len(c)):
                         if Hearts_Copy[r] == c[w]:
                              print(Hearts_Copy[r])
                              c.remove(Hearts_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
               
     for t in range(len(Diamonds_Copy)):
          if Diamonds_Copy[t] == s:
               for r in range(t + 1,len(Diamonds_Copy)):
                    for w in range(len(c)):
                         if Diamonds_Copy[r] == c[w]:
                              print(Diamonds_Copy[r])
                              c.remove(Diamonds_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
               
               
     for t in range(len(Clubs_Copy)):
          if Clubs_Copy[t] == s:
               for r in range(t + 1,len(Clubs_Copy)):
                    for w in range(len(c)):
                         if Clubs_Copy[r] == c[w]:
                              print(Clubs_Copy[r])
                              c.remove(Clubs_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
               
     for t in range(len(Spades_Copy)):
          if Spades_Copy[t] == s:
               for r in range(t + 1,len(Spades_Copy)):
                    for w in range(len(c)):
                         if Spades_Copy[r] == c[w]:
                              print(Spades_Copy[r])
                              c.remove(Spades_Copy[r])
                              f += 1
                              break
                    if f != 0:
                         break
                    
     z = 0          
     if f == 0:
          if s in Trump_Suit:
               c.append(s)
               c.append(y)
               c.append(j)
          else:
               for g in Trump_Suit:
                    for h in c:
                         if g == h:
                              print(h)
                              z += 1
                              c.remove(h)
                              break
                    if z != 0:
                         break
          
     print(My_Cards)
Card1(All_Cards, My_Cards, Rival_Cards)
if len(Rival_Cards) == 5:
     Card2()
else:
     q = choice(All_Cards)
     My_Cards.append(q)
     print('I took the card')
     print(My_Cards)
     Card1(All_Cards, My_Cards, Rival_Cards)
