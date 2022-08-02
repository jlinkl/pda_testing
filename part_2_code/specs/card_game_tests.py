import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        card = Card("spades", 1)
        self.assertEqual(True, CardGame.check_for_ace(self, card))


    def test_highest_card(self):
        card1 = Card("spades", 1)
        card2 = Card("clubs", 3)
        self.assertEqual(card2, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        card1 = Card("spades", 1)
        card2 = Card("clubs", 3)
        cards = [card1, card2]
        self.assertEqual("You have a total of 4", CardGame.cards_total(self, cards))