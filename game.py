'''
Question: 
Here is the description of the game simulation.

this is a two player card game
the game starts with a deck of cards
the cards are dealt out to both players
on each turn:
both players turn over their top-most card
the player with the higher valued card takes the cards and puts them in their scoring pile (scoring 1 point per card)
this continues until the players have no cards left
the player with the highest score wins
It's considered a simulation because the players don't have any choice, dont worry about inputHere is the description of the game simulation.

this is a two player card game
the game starts with a deck of cards
the cards are dealt out to both players
on each turn:
both players turn over their top-most card
the player with the higher valued card takes the cards and puts them in their scoring pile (scoring 1 point per card)
this continues until the players have no cards left
the player with the highest score wins
It's considered a simulation because the players don't have any choice, dont worry about input
'''

import random

class Card:
    suits_order = {"Clubs": 0, "Diamonds": 1, "Hearts": 2, "Spades": 3}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = int(rank)  # Ensure rank is an integer for proper comparison
    
    def __str__(self):
        return f"{self.rank}{self.suit[0]}"
    
    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank > other.rank:
            return False
        else:
            return Card.suits_order[self.suit] < Card.suits_order[other.suit]
    
    def __eq__(self, other):
        pass

class Deck:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        random.shuffle(self.deck)

    def prepare_decks(self, player_count: int):
        # Distribute the deck as evenly as possible among the players
        decks = [[] for _ in range(player_count)]
        while self.deck:
            for i in range(player_count):
                if self.deck:
                    decks[i].append(self.deck.pop())
                else:
                    break
        return decks
    
    def __len__(self):
        return len(self.deck)

class Player:
    def __init__(self, name: str, deck: list[Card]):
        self.name = name
        self.history = []
        self.score = 0
        self.deck = deck
        self.current_card = None
    
    # We record the card in history and use current_card to compare with others
    def deal_from_deck(self):
        if self.deck:
            self.current_card = self.deck.pop()
            self.history.append(self.current_card)
            return self.current_card
        return None

class Game:
    def __init__(self, players: list[str]):
        full_deck = Deck()
        player_decks = full_deck.prepare_decks(len(players))
        self.players = [Player(name, player_decks[i]) for i, name in enumerate(players)]

    def start(self):
        while self.fight():
            pass
        self.game_winner() 
            
    def fight(self):
        cards = [player.deal_from_deck() for player in self.players]
        if None in cards: # If any player has no cards left, end the game
            return False

        max_player = max(self.players, key= lambda player: player.current_card)
        max_player.score += 1
        return True

    def game_winner(self):
        self.current_status()

        highest_score = max(player.score for player in self.players)
        winners = [player.name for player in self.players if player.score == highest_score]
        
        if len(winners) == len(self.players):
            print("Draw!!")
        print(f"Winners: {winners}; Score board: {[player.score for player in self.players]}")

    def current_status(self):
        for player in self.players:
            self.print_deck(player)
            print()

    def print_deck(self, player: Player):
        print("player : ", player.name)
        print("score  : ", player.score)
        print("history: ", [str(card) for card in player.history])
        # For debugging
        if player.deck:
            print("remain cards : ", len([str(card) for card in player.deck]))
            print("deck         : ", [str(card) for card in player.deck])

if __name__ == "__main__":
    name_lst = ['austin', 'cindy', 'fu', 'Kevin']
    game = Game(name_lst)
    game.start()
