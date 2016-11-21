from random import shuffle

values = range(1, 11) + 'J Q K'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]

shuffle(deck)

while deck:
    raw_input(deck.pop())
