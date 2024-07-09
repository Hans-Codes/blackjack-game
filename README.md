# Console-based Blackjack Game

This is a simple console-based blackjack game implemented in Python. It allows players to play blackjack against a dealer, with customizable settings such as starting money, minimum and maximum bets, and optional game features like double down and insurance.

## Features

- **Blackjack Gameplay**: Play blackjack against the dealer.
- **Customizable Settings**: Adjust starting money, bet limits, and enable/disable double down and insurance through `config.json`.
- **Tip the Dealer**: Optionally tip the dealer with a cool Easter egg included.

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of how to run Python scripts from the command line.

## Setup

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Modify `config.json` to adjust game settings if desired:
   - `username`: Your preferred player name.
   - `starting_money`: Amount of money you start with.
   - `min_bet`: Minimum bet allowed.
   - `max_bet`: Maximum bet allowed.
   - `enable_double_down`: `true` or `false` to enable or disable double down.
   - `enable_insurance`: `true` or `false` to enable or disable insurance.

## Usage

1. Open your command prompt or terminal.
2. Navigate to the directory where you saved the `blackjack.py` and `config.json` files.
3. Run the game with the command: `python blackjack.py`.
4. Follow the on-screen instructions to play the game.

## Gameplay Instructions

- Place your bet within the specified limits.
- Choose to hit, stand, or double down during your turn.
- The dealer will play their hand according to standard blackjack rules.
- Win by having a higher hand value than the dealer without exceeding 21.
- Optionally tip the dealer with a funny Easter egg included in the game.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
