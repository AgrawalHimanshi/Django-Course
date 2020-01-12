from random import shuffle

SUITE='H D S C'.split()
RANKS= '2 3 4 5 6 7 8 9 10 J Q K A'.split()



class Deck:
    """
    this is the deck class. it will create deck of cards and divide
    it into 2 halves and give to players. it will use SUITE and RANKS
    to create the deck. it also has method for shuffling and splitting
    in halves
    """

    def __init__(self):
        print("creating new deck of cards")
        self.allcards=[(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING CARDS")
        shuffle(self.allcards)

    def split_in_halves(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    """
    each player can add and remove cards from the Hand
    """

    def __init__(self,cards):
        self.cards=cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()

class Player:
    """
    it takes in name and instance of Hand class object.
    the player can take cards and check if they still
    have CARDS
    """
    def __init__(self, name,hand):
        self.name=name
        self.hand=hand #hand is Hand object

    def play_card(self):
        drawn_card=self.hand.remove_cards()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_card=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_card.append(self.hand.remove_cards())

        return war_card

    def still_in_hand(self):
        """
        return true if player still has cards left
        """
        return len(self.hand.cards)!=0

#begin game #

#create a new deck and split in half

d=Deck()
d.shuffle()
half1, half2=d.split_in_halves()

#create both players!

comp=Player("computer",Hand(half1))
name=input("what is your name ")

user=Player(name, Hand(half2))
total_round=0
war_count=0

while user.still_in_hand() and comp.still_in_hand():
    total_round+=1
    print("time for new round")
    print("Here are current standing")
    print(user.name+" has the count "+str(len(user.hand.cards)))
    print(comp.name+" has the count "+str(len(comp.hand.cards)))
    print("\n")

    table_cards=[]
    c_card=comp.play_card()
    p_card=user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1]==p_card[1]:
        war_count+=1;
        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
#if there is no war
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("GAME OVER !, NO. OF ROUNDS "+str(total_round))
print("A WAR HAPPENED ",str(war_count)+" times")
print("Does the computer still has card? ")
print(str(comp.still_in_hand()))
print("Does the user still has card? ")
print(str(user.still_in_hand()))
