import random


class Deck:
    def __init__(self, seed=None):
        self.cards = [i for i in range(1, 10)] * 4 + [10] * 16
        random.seed(seed)
        random.shuffle(self.cards)

    def deal(self, start, n):
        return self.cards[start:start + n]


class Player:
    def __init__(self, hand):
        self.hand = hand
        self.total = 0

    def deal(self, cards):
        self.hand.extend(cards)
        self.total = sum(self.hand)


def cmp(x, y):
    return (x > y) - (x < y)


def play(deck, start, scores):
    player = Player(deck.deal(start, 2))
    dealer = Player(deck.deal(start + 2, 2))

    results = []

    # The player can hit as many times as there are cards left.
    for i in range(49 - start):
        count = start + 4
        player.deal(deck.deal(count, i))
        count += i

        # Once a player busts, there is no point in exploring further hits, so we skip to evaluation.
        if player.total > 21:
            results.append((-1, count))
            break

        # The dealer responds deterministically, only hitting if below 17.
        while dealer.total < 17 and count < 52:
            dealer.deal(deck.deal(count, 1))
            count += 1

        # If the dealer busts, the player wins. Else, compare their totals.
        if dealer.total > 21:
            results.append((1, count))
        else:
            results.append((cmp(player.total, dealer.total), count))

    options = []
    for score, next_start in results:
        options.append(score +
                       scores[next_start] if next_start <= 48 else score)

    scores[start] = max(options)


def blackjack(seed=None):
    deck = Deck(seed)
    scores = [0 for _ in range(52)]
    for start in range(48, -1, -1):
        play(deck, start, scores)
    return scores[0]


r = blackjack()
print(r)
