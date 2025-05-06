# Program that draws five cards from a single shuffled deck, printing the drawn cards and checking for a subset of poker hands.
# Author Finbar Dennehy

# Import required package
import requests
from collections import Counter

# Set number of decks and number of cards to be drawn
deck_count = 1
card_count = 5

def main():

    # Shuffle new deck.
    shuffle_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}"
    response = requests.get(shuffle_url)
    deck = response.json()

    # Get the deck ID
    deck_id = deck['deck_id']

    # Draw cards from the shuffled deck.
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={card_count}"
    response = requests.get(draw_url)
    cards = response.json()

    # Print out drawn cards and append values and suits to lists, for checking hand later.
    values = []
    suits = []
    for card in cards['cards']:
        print (f"{card['value']} of {card['suit']}")
        values.append(card['value'])
        suits.append(card['suit'])
    
    # TESTING:

    # flush
    #suits = ['CLUBS', 'CLUBS', 'CLUBS', 'CLUBS', 'CLUBS' ]

    # straight
    #values = ['4', '5', '6', '7', '8' ]

    # triple
    #values = ['4', '4', '4', '7', '9' ]

    # double
    #values = ['4', '5', '5', '7', '9' ]

    # Print poker hand, if drawn
    poker_hand = evaluate_hand(values, suits)
    if poker_hand == "FLUSH":
        print("Congratulations on drawing a FLUSH!")
    elif poker_hand == "STRAIGHT":
        print("Congratulations on drawing a STRTAIGHT!")
    elif poker_hand == "TRIPLE":
        print("Congratulations on drawing a TRIPLE!")
    elif poker_hand == "DOUBLE":
        print("Congratulations on drawing a DOUBLE!")

    
# Function to check poker hand, now that the 5 cards have been drawn from the deck #
def evaluate_hand(values, suits):

# Map picture cards to numerical values for straight checking. 
# Assumes Aces are high.
    
    value_map = {
        "ACE": 14,
        "KING": 13,
        "QUEEN": 12,
        "JACK": 11,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    value_counts = Counter(values) # count occurences of each value. https://docs.python.org/3/library/collections.html#collections.Counter
    numeric_values = sorted([value_map[val] for val in values]) # map picture values to numeric values and order (ascending) with sorted().

    is_flush = len(set(suits)) == 1 # set() gets distint values https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    is_straight = all(numeric_values[i] - numeric_values[i-1] == 1 for i in range(1, card_count)) # check each number is consecutive, i.e. difference between them is 1.
    is_triple = any(count == 3 for count in value_counts.values()) # any() returns True if any element of the iterable is true. If the iterable is empty, return False.
    is_pair = any(count == 2 for count in value_counts.values()) # https://docs.python.org/3/library/functions.html#any

    # order by precedence e.g. so a double is not printed in the event a triple is drawn
    if is_flush:
        return("FLUSH")
    elif is_straight:
        return("STRAIGHT")
    elif is_triple:
        return("TRIPLE")
    elif is_pair:
            return("DOUBLE")


if __name__ == "__main__":
    main()