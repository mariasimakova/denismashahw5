import pytest
from card_game import Card, Deck

def test_card_initialization():
    card = Card("Hearts", "A")
    assert card.suit == "Hearts"
    assert card.value == "A"
    assert str(card) == "A of Hearts"

def test_deck_length():
    deck = Deck()
    assert len(deck.cards) == 52 

def test_deck():
    deck = Deck()

    suits = {"Hearts", "Diamonds", "Clubs", "Spades"}
    values = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}

    for card in deck.cards:
        assert card.suit in suits
        assert card.value in values

def test_shuffle():
    deck = Deck()
    original_order = deck.cards.copy() 
    deck.shuffle()
    assert deck.cards != original_order  
    assert len(deck.cards) == 52  

def test_draw(capsys):
    original_deck = Deck()
    original_length = len(original_deck.cards)

    test_deck = Deck()
    
    original_deck.draw()

    captured = capsys.readouterr()
    assert captured.out == f"{test_deck.cards.pop()}\n" 
    
    assert len(original_deck.cards) == original_length - 1 
    for _ in range(original_length - 1):
        original_deck.draw()

    assert len(original_deck.cards) == 0 
    assert original_deck.draw() is None