from core.game.Card import Card
from core.game.PlayerHandCount import PlayerHandCount
from typing import List


class PlayerGameHelper:
    def __init__(self, hand, last_card_played, card_pile, deck_count, opp_hand_count):
        self._hand = hand
        self._last_card_played = last_card_played
        self._card_pile = card_pile
        self._deck_count = deck_count
        self._opp_hand_count = opp_hand_count

    def get_hand(self) -> List[Card]:
        return self._hand

    def get_last_card_played(self) -> Card:
        return self._last_card_played

    def get_card_pile(self) -> List[Card]:
        return self._card_pile

    def get_deck_count(self) -> int:
        return self._deck_count

    def getOpponentsHandCount(self) -> List[PlayerHandCount]:
        return self._opp_hand_count