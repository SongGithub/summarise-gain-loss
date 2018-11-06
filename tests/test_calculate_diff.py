from summarise_gain_loss import calculate_diff

from decimal import Decimal
import pytest
# tests for underlaying plumbings


MINIMAL_INPUT_GAIN = [1.12, 2.45]
MINIMAL_INPUT_LOSS = [2.23, 1.32]


def test_calculate_diff_minimal_gain():
    assert calculate_diff(
        MINIMAL_INPUT_GAIN[0], MINIMAL_INPUT_GAIN[1]
        ) == round(Decimal(1.33), 2)


def test_calculate_diff_minimal_loss():
    assert calculate_diff(
        MINIMAL_INPUT_LOSS[0], MINIMAL_INPUT_LOSS[1]
        ) == round(Decimal(-0.91), 2)

def test_output_digits():
    '''ensure there are 2 digits after decimal point'''
    number_gain = calculate_diff(
        MINIMAL_INPUT_GAIN[0],
        MINIMAL_INPUT_GAIN[1]
        )
    assert len(str(number_gain-int(number_gain))[2:]) == 2

    number_loss = calculate_diff(
        MINIMAL_INPUT_LOSS[0],
        MINIMAL_INPUT_LOSS[1]
        )

    assert len(str(number_gain-int(number_loss))[2:]) == 2

