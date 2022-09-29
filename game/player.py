from game.card import Card


class Player:
    def __init__(self):
        self.old_card = 0
        self.is_playing = True
        self.guess = True
        self.score = 300
        self.card = []

        card = Card()
        self.card.append(card)

    def start_game(self):
        while self.is_playing:
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        pick_card = input("Play again? [y/n] ")
        self.is_playing = (pick_card == "y")
       
    def do_updates(self):
        if not self.is_playing:
            return 

        if(self.guess == (self.card > self.old_card)):
            self.score += 100
        else:
            self.score -= 75
        self.old_card = self.card

    def do_outputs(self):
        if not self.is_playing:
            return
          
        card = self.card
        card.pick()
        card.value = self.card

        print(f"The card is {self.card}")
        high_low = input("Higher or lower? [h/l] ")
        if (high_low == "h"):
          self.guess = True
        else: 
          self.guess == False

        self.is_playing = (self.score > 0)
        if not self.is_playing:
            print(f"You rolled:")
            print("No 1's or 5's! You lose!")
            print(f"Your final score was: {self.total_score}\n")
            return
        
        print(f"You rolled:")
        print(f"Your score is: {self.total_score}\n")
        
        self.score = 0