"""Contains the utility functions."""


def chunk(l, n, reverse=False):
    """Yield successive n-sized chunks from l."""
    start = 0
    stop = len(l)
    step = n

    if reverse:
        first_boundary = len(l) % step
        if first_boundary != 0:
            yield l[start:first_boundary]
            start = first_boundary

    for i in range(start, stop, step):
        yield l[i:i + step]
