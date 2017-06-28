from number2text.utils import chunk


class TestChunk(object):
    """Test the chunk function."""

    def test_chunks_00(self):
        l = '12345678'
        actual = [c for c in chunk(l, 3)]
        expected = ['123', '456', '78']
        assert actual == expected

    def test_chunks_01(self):
        l = '12345678'
        actual = [c for c in chunk(l, 4)]
        expected = ['1234', '5678']
        assert actual == expected

    def test_chunks_reverse_00(self):
        l = '12345678'
        actual = [c for c in chunk(l, 3, True)]
        expected = ['12', '345', '678']
        assert actual == expected

    def test_chunks_reverse_01(self):
        l = '12345678'
        actual = [c for c in chunk(l, 2, True)]
        expected = ['12', '34', '56', '78']
        assert actual == expected
