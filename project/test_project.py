from project import get_card, card_emoji, play_game, computer_game

from io import StringIO
import unittest
from unittest.mock import MagicMock

def test_computer_game():
    assert computer_game() < 22
    assert computer_game() > 16


def test_get_card():
    assert get_card() < 11
    assert get_card() > 0


def test_card_emoji():
    assert card_emoji(1) == "🃏"
    assert card_emoji(2) == "🤴"

def test_play_game():
    user_input = ['n']
    mock_input = MagicMock(side_effect=user_input)
    expected_output =[ 'Better luck next time!\n', ""]
    with StringIO() as mock_output:
        with MagicMock(stdin=mock_input, stdout=mock_output):
            play_game()
            result = mock_output.getvalue()
            assert result in expected_output

    user_input = ['y', 'n']
    mock_input = MagicMock(side_effect=user_input)
    with StringIO() as mock_output:
        with MagicMock(stdin=mock_input, stdout=mock_output):
            result = play_game()
            if result == 0:
                expected_output = ''
            else:
                expected_output in ['Your score is %s.\n' % result, ""]
            assert mock_output.getvalue() in expected_output
