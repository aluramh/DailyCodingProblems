# Given a deck of cards with values from 1-10, you keep drawing from an infinite deck of cards.

# If you Have between 17 and 21, you win.

# Write an algorithm to minimze the lose probability.

import random

MIN_TARGET = 17
MAX_TARGET = 21
MAX_RISK = 0.5

memo = {}

for i in range(0, 12):
    memo[f"{i}"] = 0


def get_card():
    return random.randint(1, 10)


def game(score, hand, lose_probability):
    if MIN_TARGET <= score and score <= MAX_TARGET:
        return True, score, hand, lose_probability
    elif score >= MAX_TARGET:
        return False, score, hand, lose_probability
    else:
        if lose_probability <= MAX_RISK:
            new_card = get_card()
            new_hand = hand + [new_card]
            new_score = score + new_card

            if new_score < 12:
                new_probability = 0
            else:
                new_probability = (10 - (MAX_TARGET - new_score)) / 10

            memo[f"{new_score}"] = new_probability
            return game(new_score, new_hand, new_probability)
        else:
            # We will not draw and end here
            return True, score, hand, lose_probability

    return


did_win, score, hand, lose_probability = game(0, [], 0)

print("CONGRATULATIONS!" if did_win is True else "You lost 😭")
print('score', score)
print('hand', hand)
print('lose_probability', lose_probability)
