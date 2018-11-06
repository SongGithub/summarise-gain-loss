from summarise_gain_loss import summarise_prices

from decimal import Decimal
import pytest

TEST_INPUT = [
    78.41,
    85.18,
    91.09,
    90.57,
    91.02,
    103.61,
    105.88,
    103.77,
    110.13,
    108.89,
    105.09]

# tests for business logic
def test_original_sample():
    assert summarise_prices(TEST_INPUT)["GAIN"] == str("34.35")
    assert summarise_prices(TEST_INPUT)["LOSS"] == str("-7.67")
