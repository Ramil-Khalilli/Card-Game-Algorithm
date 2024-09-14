# Card-Game-Algorithm
Interactive Card Game ("Durak") algorithm using Python IDLE
---

# Card Game Simulator

This project is a simple card game ("Durak") simulator written in Python. It uses a standard deck of 36 cards (from 6 to Ace in four suits: Hearts, Diamonds, Clubs, and Spades). The game deals cards to both the player and a rival, selects a trump card, and provides functions for players to play cards in a simulated turn-based card game.

## Features

- **Random Card Dealing**: Each player receives 6 random cards from the deck at the beginning.
- **Trump Card**: A trump card is randomly selected, which determines the trump suit.
- **Game Mechanics**:
  - Players can play cards based on specific logic.
  - Cards are removed from players' hands as they are played.
  - Cards are automatically added back to hands when necessary (e.g., when the player has fewer than 6 cards).
- **Suit and Card Matching**: Logic for card comparison based on suits, trump cards, and matching.

## How the Code Works

1. **Initialization**: 
    - A deck of 36 cards is created and split into suits (Hearts, Diamonds, Clubs, Spades).
    - Players (the user and a rival) are dealt 6 random cards each from the deck.
    - A trump card is chosen, which determines the trump suit for the game.

2. **Player Actions**: 
    - The `Card1` function allows the player to play a card. The logic checks if there is a higher-ranking card or a trump card that can be used to win the round.
    - The `Card2` function lets the player respond to the rival’s move.

3. **Game Flow**: 
    - The game continues by comparing the cards played and replenishing hands when necessary.
    - Cards played are removed from the players' hands, and the game logic ensures players follow suit or play a trump card when required.

## How to Run

1. Install Python 3.x on your machine.
2. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/card-game-simulator.git
    ```
3. Run the Python script:
    ```bash
    python card_game.py
    ```

## Example Output

```python
['Hearts_6', 'Diamonds_8', 'Clubs_9', 'Spades_Ace', 'Hearts_Jack', 'Clubs_7']
Trump card is Diamonds_Queen
Please, enter a card: Hearts_6
Diamonds_Queen
```

## To-Do/Improvements

- Add a graphical interface for better interaction.
- Implement more complex game rules and strategies.
- Refactor the code for better modularity and readability.
