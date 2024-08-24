# Two-Player Card Game Simulation

## Overview

This project is a Python simulation of a simple two-player card game. The game is designed to be fully automated, where the players don't make any decisions—the game runs entirely based on the rules provided. The goal is to simulate a game where two players compete by drawing cards from their respective decks, and the player with the higher-valued card wins that round. The game continues until all cards have been played, and the player with the most points wins.

## How the Game Works

1. **Deck of Cards**: The game begins with a standard deck of 52 cards, consisting of 4 suits (Spades, Hearts, Diamonds, Clubs) and 13 ranks (1 through 13).

2. **Dealing Cards**: The deck is shuffled and then evenly distributed between the two players.

3. **Playing the Game**:
   - Each player draws the top card from their deck.
   - The player with the higher-ranked card wins the round and scores points equivalent to the number of cards in play (1 point per card).
   - If the ranks are the same, the suit is used as a tiebreaker, with the order from highest to lowest being Spades > Hearts > Diamonds > Clubs.
   - The game continues until both players have no cards left in their decks.

4. **Winning the Game**: The player with the most points at the end of the game is declared the winner. In the event of a tie, the game is declared a draw.

## Project Structure

- `Card`: A class representing a single card in the deck, with a suit and rank. Includes methods for comparison (`<`, `==`).
- `Deck`: A class that initializes a full deck of 52 cards, shuffles them, and distributes them between the players.
- `Player`: A class representing a player in the game. Each player has a name, a deck of cards, a score, and a history of the cards they've played.
- `Game`: The main class that handles the game logic, including dealing cards, running rounds, and determining the winner.

### Example result

``` Text
# main function
name_lst = ['austin', 'cindy', 'fu', 'Kevin']
game = Game(name_lst)
game.start()

output
player :  austin
score  :  5
history:  ['13H', '2S', '9C', '9S', '12S', '2H', '9D', '2C', '3S', '13C', '8C', '4H', '3H', 'None']

player :  cindy
score  :  1
history:  ['3C', '12H', '4D', '5H', '11C', '5S', '3D', '4S', '7H', '11D', '5C', '12D', '2D', 'None']

player :  fu
score  :  4
history:  ['1H', '10C', '13S', '6D', '8S', '10S', '10H', '8D', '4C', '6S', '11S', '8H', '10D', 'None']

player :  Kevin
score  :  3
history:  ['7D', '11H', '6H', '7S', '13D', '9H', '12C', '1D', '1C', '5D', '1S', '6C', '7C', 'None']

Winners: ['austin']; Score board: [5, 1, 4, 3]
```
