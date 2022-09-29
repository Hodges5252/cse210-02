from game.card import Card


class Player:
    def __init__(self):
        self.current_card = 0
        self.old_card = 0
        self.is_playing = True
        self.guess = True
        self.score = 300
        card = Card()
        self.card = card


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

        if(self.guess == (self.current_card > self.old_card)):
            self.score += 100
        else:
            self.score -= 75
        self.old_card = self.current_card

    def do_outputs(self):
        if not self.is_playing:
            return

##This part below has some issues
        card = self.card
        card.pick()
        self.current_card = card

        print(f"The card is {self.current_card}")
        high_low = input("Higher or lower? [h/l] ")
        if (high_low == "h"):
          self.guess = True
        else: 
          self.guess == False

        self.do_updates()

        self.is_playing = (self.score > 0)
        if not self.is_playing:
            print("Your score is 0! You lose!")
            return
        
        print(f"Next card was: {self.card}")
        print(f"Your score is: {self.score}\n")