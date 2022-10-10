from unittest import TestCase

from lib.networks import Side


class TestSide(TestCase):
    def test_opposite(self):
        """
        Test that opposite returns the correct side
        """
        expected = [Side.DOWN, Side.SOUTH, Side.EAST, Side.UP, Side.NORTH, Side.WEST]
        cases = [Side.UP, Side.NORTH, Side.WEST, Side.DOWN, Side.SOUTH, Side.EAST]

        for i in range(len(cases)):
            msg = f"Case: {cases[i].name}, Expected: {expected[i].name}"
            with self.subTest(msg=msg):
                self.assertEqual(expected[i], Side.opposite(cases[i]))
