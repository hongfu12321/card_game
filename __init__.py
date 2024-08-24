import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank}{self.suit[0]}"
    
    # Compare card using __lt__ and __eq__
    def __lt__(self, other):
        suits = {
          "Spades": 3, 
          "Hearts": 2, 
          "Diamonds": 1, 
          "Clubs" :0 
        }

        if self.rank < other.rank:
            return True
        elif self.rank > other.rank:
            return False
        else:
            if suits[self.suit] < suits[other.suit]:
                return True
            else:
                return False
            
    def __eq__(self, other):
        pass

class Deck:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    # Separate desk to player_count decks.
    def prepare_decks(self, player_count: int):
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

    def print_deck(self):
        for card in self.deck:
            print(str(card))

class Player:
    def __init__(self, name: str, deck: list[Card]):
        self.name = name
        self.history = []
        self.score = 0
        self.deck = deck
        self.current_card = None
    
    # We record the card in history and use current_card to compare with others
    def deal_from_deck(self):
        card = self.deck.pop() if self.deck else None
        self.current_card = card
        self.history.append(card)
        return card


class Game:
    def __init__(self, players: list[str]):
        players_len = len(players)
        self.deck = Deck()
        desks = self.deck.prepare_decks(players_len)
        self.players: list[Player] = []
        for i in range(players_len):
            self.players.append(Player(name_lst[i], desks[i]))

    def start(self):
        while self.fight():
            pass
        self.game_winner()
        
            
    def fight(self):
        cards = [player.deal_from_deck() for player in self.players]

        # if no card available, return
        if None in cards:
            return False

        max_player = max(self.players, key= lambda player: player.current_card)
        max_player.score += 1
        # print(max_player.name, [str(card) for card in cards])
        return True

    def game_winner(self):
        self.current_status()

        highest_score = 0
        winners = []
        for player in self.players:
            if player.score > highest_score:
                winners = [player.name]
                highest_score = player.score
            elif player.score == highest_score:
                winners.append(player.name)
        
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
