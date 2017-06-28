import pytest

from number2text.conversion import convert


class TestConversion(object):
    """Test the conversion function."""

    # Scenario list.
    # Each entry is a tuple composed of
    #     1. The number to convert.
    #     2. Its string representation (human readable)
    scenarios = [
        ((0, 'zero'), 'zero'),
        ((7, 'seven'), 'units'),
        ((16, 'sixteen'), 'special tens'),
        ((34, 'thirty four'), 'tens'),
        ((748, 'seven hundred fourty eight'), 'hundreds'),
        ((4952, 'four thousand nine hundred fifty two'), 'thousands'),
        ((593782, 'five hundred ninety three thousand seven hundred eighty two'), 'hundred thousands'),
        ((956974389, 'nine hundred fifty six million nine hundred seventy four thousand three hundred eighty nine'),
         'millions'),
        ((480632894175,
          'four hundred eighty billion six hundred thirty two million eight hundred ninety four thousand one hundred seventy five'
          ), 'billions'),
    ]

    # Lambdas to parse the scenarios and feed the data to the test functions.
    scenario_inputs = lambda scenarios: [test_input[0] for test_input in scenarios]
    scenario_ids = lambda scenarios: [test_input[1] for test_input in scenarios]

    @pytest.mark.parametrize("test_input", scenario_inputs(scenarios), ids=scenario_ids(scenarios))
    def test_conversion(self, test_input):
        """Ensure a number has the correct representation"""
        actual = convert(test_input[0])
        expected = test_input[1]
        assert actual == expected
