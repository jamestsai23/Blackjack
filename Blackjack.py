# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_card = []

    def __str__(self):
        s = "Hands have "
        for i in self.hand_card :
            s += str(i.get_suit()) + str(i.get_rank()) + " "
        return s

    def add_card(self, card):
        self.hand_card.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        self.have_ace = False 
        for i in self.hand_card :
            if i.get_rank() == "A" :
                self.have_ace = True 
        
        if self.have_ace == False :
            for i in self.hand_card :
                self.value += VALUES[str(i.get_rank())]
                
        else :
            for i in self.hand_card :
                self.value += VALUES[str(i.get_rank())]
            if self.value <= 11 :
                self.value += 10
                    
        return self.value
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        
        pass	# draw a hand on the canvas, use the draw method for cards

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []
        for i in SUITS :
            for j in RANKS :
                self.deck_list.append(Card(i, j))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_list)
        pass    # use random.shuffle()

    def deal_card(self):
        self.topcard = self.deck_list.pop()
        return self.topcard
        pass	# deal a card object from the deck
    
    def __str__(self):
        s = "Deck contains "
        for i in self.deck_list :
            s += str(i.get_suit()) + str(i.get_rank()) + " "
        return s
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, dealer_hand, player_hand, deck_now, score
    
    if in_play :
        score -= 1
    
    outcome = ""
    deck_now = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck_now.shuffle()
    dealer_hand.add_card(deck_now.deal_card())
    dealer_hand.add_card(deck_now.deal_card())
    player_hand.add_card(deck_now.deal_card())
    player_hand.add_card(deck_now.deal_card())
    
    #print "Player have"
    #print player_hand
    #print  "Dealer have "
    #print dealer_hand
    
    
    in_play = True

def hit():
    pass	# replace with your code below
    global outcome, in_play, dealer_hand, player_hand, deck_now, score
    # if the hand is in play, hit the player
    if in_play == True :
        player_hand.add_card(deck_now.deal_card())
        #print player_hand
        #print str(player_hand.get_value())
        if player_hand.get_value() > 21 :
            in_play = False
            outcome = "You have busted."
            #print outcome 
            score -= 1
        
    # if busted, assign a message to outcome, update in_play and score
    else :
        pass
        #print score
        
def stand():
    pass	# replace with your code below
    global outcome, in_play, dealer_hand, player_hand, deck_now, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if player_hand.get_value() > 21 :
        outcome = "You have busted"
    if in_play :
        while dealer_hand.get_value() < 17 :
            dealer_hand.add_card(deck_now.deal_card())
            #print dealer_hand
            #print dealer_hand.get_value()
        if dealer_hand.get_value() > 21:
            outcome = "Dealer have busted."
            in_play = False
            score += 1
            #print score
        else :
            if dealer_hand.get_value() >= player_hand.get_value() :
                outcome = "You lose."
                in_play = False
                score -= 1
                #print score
            else :
                outcome = "You win."
                in_play = False
                score += 1
                #print score
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, in_play, dealer_hand, player_hand, deck_now, score
    
    canvas.draw_text("Blackjack", [50, 120], 50, "aqua")
    canvas.draw_text(outcome, [250, 170], 30, "black")
    canvas.draw_text("Score:", [300, 120], 30, "balck")
    canvas.draw_text(str(score), [380, 120], 30, "black")
    canvas.draw_text("Dealer", [60, 170], 30, "black")
    canvas.draw_text("Player", [60, 380], 30, "black")
    if in_play :
        canvas.draw_text("Hit or stand?", [250, 380], 30, "black")
    else :
        canvas.draw_text("New deal?", [250, 380], 30, "black")
    
    j = 0
    k = 1
    for i in player_hand.hand_card :
        i.draw(canvas,[30 + j * 90, 400])
        j += 1
    if in_play == False:
        dealer_hand.hand_card[0].draw(canvas, [30 , 200])
    else :
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [30+CARD_CENTER[0], 200+CARD_CENTER[1]], CARD_SIZE)
    for i in dealer_hand.hand_card[1:] :
        i.draw(canvas,[30 + k * 90, 200])
        k += 1
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric