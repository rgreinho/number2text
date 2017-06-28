"""Define the conversion module."""

from collections import deque

from number2text.utils import chunk

UNITS = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

TENS = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'fourty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety',
}

SPECIAL_TENS = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
}

BIG_NUMBERS = ['', 'thousand', 'million', 'billion', 'trillion']


def convert(number):
    """
    Convert a number to its string representation.

    :param int number: number to convert
    :return: the string representation of this number.
    """

    # Zero is a very special case.
    if number == 0:
        return 'zero'

    # Split the number.
    chunks = [c for c in chunk(str(number), 3, True)]

    # Prepare the big number.
    big_numbers_adjusted = BIG_NUMBERS[0:len(chunks)]
    big_numbers_deque = deque(big_numbers_adjusted)

    # Empty list to store the result.
    res = []

    # Go though each chunk.
    for c in chunks:
        # Skip the chunks full of zeros.
        if c == '000':
            continue

        # Prepare the deque.
        d = deque(c)

        # Convert the hundreds.
        if len(d) == 3:
            h = d.popleft()
            if h != '0':
                res.append(UNITS[h])
                res.append('hundred')

        # Convert the tens.
        if len(d) == 2:
            t = d.popleft()

            # Take care of the special tens.
            if t == '1':
                t += d.popleft()
                res.append(SPECIAL_TENS[t])
            elif t != '0':
                res.append(TENS[t])

        # Convert the units.
        if len(d) == 1:
            u = d.popleft()
            if u != '0':
                res.append(UNITS[u])

        # Add the big number.
        res.append(big_numbers_deque.pop())

    return ' '.join(res).strip()
