card_deck = [4,5,9,10,5,6,16]
hand = []
while sum(hand) < 17:
  hand.append(card_deck.pop())
print(hand)