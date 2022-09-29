import random

class Card: 

  def __init__(card):
    
    card.value = 0

  def pick(card):
  
    card.value = random.randint(1,13)  