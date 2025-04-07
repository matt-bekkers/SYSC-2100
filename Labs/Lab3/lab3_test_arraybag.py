# SYSC 2100 Winter 2024 Lab 3: Unit tests for class ArrayBag.

import unittest

from lab3_arraybag import ArrayBag

# The first seven classes test the methods that are in the ArrayBag class that
# is provided to students.


class InitTestCase(unittest.TestCase):
    """Test __init__."""

    # The tests in this class access the "private" attributes in the ArrayBag
    # object directly, because __init__ is the first method we implement,
    # so the other methods won't be available.

    def test_init1(self):
        """Test __init__: no iterable passed to to ArrayBag()."""
        bag = ArrayBag()

        # The new bag should have 0 elements and the capacity of its
        # backing array should be 1.

        self.assertEqual(bag._num_items, 0)
        self.assertEqual(len(bag._elems), 1)

    def test_init2(self):
        """Test __init__: empty iterable passed to ArrayBag()."""
        bag = ArrayBag([])

        # The new bag should have 0 elements and the capacity of its
        # backing array should be 1.

        self.assertEqual(bag._num_items, 0)
        self.assertEqual(len(bag._elems), 1)

    def test_init3(self):
        """Test __init__: non-empty iterable with no duplicate elements passed to ArrayBag()."""
        bag = ArrayBag([1, 4, 3, 6])

        self.assertEqual(bag._num_items, 4)

        # Create a sorted list from the ArrayBag's backing array.
        # This means that this test doesn't depend on the bag's elements being
        # stored in any particular order.

        # The n items in the bag are stored in the first n elements of its
        # backing array.
        elems = []
        for i in range(bag._num_items):
            elems.append(bag._elems[i])
        self.assertEqual(sorted(elems), [1, 3, 4, 6])

    def test_init4(self):
        """Test __init__: non-empty iterable with duplicate elements passed to ArrayBag()."""
        bag = ArrayBag([1, 4, 4, 1, 9, 4, 6, 6])

        self.assertEqual(bag._num_items, 8)

        # Create a sorted list from the ArrayBag's backing array.
        # This means that this test doesn't depend on the bag's elements being
        # stored in any particular order.

        # The n items in the bag are stored in the first n elements of its
        # backing array.
        elems = []
        for i in range(bag._num_items):
            elems.append(bag._elems[i])
        self.assertEqual(sorted(elems), [1, 1, 4, 4, 4, 6, 6, 9])


class AddTestCase(unittest.TestCase):
    """Test add."""

    # These tests assume that __init__ can create an empty ArrayBag.
    # The tests access the "private" attributes in the ArrayBag object directly.
    # This means that no other ArrayBag methods need to be implemented in
    # order to test add.

    def test_add1(self):
        """Add items (no duplicates) to an empty bag."""
        bag = ArrayBag()
        for x in [1, 4, 3, 6]:
            bag.add(x)

        # The n items in the bag are stored in the first n elements of its
        # backing array.

        elems = []
        for i in range(bag._num_items):
            elems.append(bag._elems[i])
        self.assertEqual(sorted(elems), [1, 3, 4, 6])

    def test_add2(self):
        """Add items (some duplicated) to an empty bag."""
        bag = ArrayBag()
        for x in [1, 4, 4, 1, 9, 4, 6, 6]:
            bag.add(x)

        # The n items in the bag are stored in the first n elements of its
        # backing array.

        elems = []
        for i in range(bag._num_items):
            elems.append(bag._elems[i])
        self.assertEqual(sorted(elems), [1, 1, 4, 4, 4, 6, 6, 9])


class IterTestCase(unittest.TestCase):
    """Test __iter__."""

    def test_iter1(self):
        """Test iteration over an empty bag."""
        bag = ArrayBag()
        elems = []
        for elem in bag:
            elems.append(elem)
        self.assertEqual(elems, [])

    def test_iter2(self):
        """Test iteration over a bag containing some duplicate elements."""
        bag = ArrayBag([1, 4, 4, 1, 9, 4, 6, 6])
        elems = []
        for elem in bag:
            elems.append(elem)
        self.assertEqual(sorted(elems), [1, 1, 4, 4, 4, 6, 6, 9])


class StrTestCase(unittest.TestCase):
    """Test __str__.

    Verify that __str__ returns a string representation of the ArrayBag
    in the expected format.
    """

    def test_str1(self):
        """Test __str__ with an empty bag."""
        bag = ArrayBag()
        self.assertEqual(str(bag), '{}')

    def test_str2(self):
        """Test __str__ with a bag containing one element."""
        bag = ArrayBag([10])
        self.assertEqual(str(bag), '{10}')

    def test_str3(self):
        """Test __str__ with a bag containing multiple elements, all identical."""
        bag = ArrayBag([2, 2, 2, 2, 2])
        self.assertEqual(str(bag), '{2, 2, 2, 2, 2}')

    # We don't test the case in which the bag contains elements that aren't
    # duplicates, because elements in a bag are unordered, so we don't know
    # the order in which the elements will be listed in the string returned
    # by __str__.


class ReprTestCase(unittest.TestCase):
    """Test __repr__.

    Verify that __repr__ returns a string representation of the ArrayBag
    in the expected format.
    """

    def test_repr1(self):
        """Test __repr__ with an empty bag."""
        bag = ArrayBag()
        self.assertEqual(repr(bag), 'ArrayBag([])')

    def test_repr2(self):
        """Test __repr__ with a bag containing one element."""
        bag = ArrayBag([10])
        self.assertEqual(repr(bag), 'ArrayBag([10])')

    def test_repr3(self):
        """Test __repr__ with a bag containing multiple elements, all identical."""
        bag = ArrayBag([2, 2, 2, 2, 2])
        self.assertEqual(repr(bag), 'ArrayBag([2, 2, 2, 2, 2])')

    # We don't test the case in which the bag contains elements that aren't
    # duplicates, because elements in a bag are unordered, so we don't know
    # the order in which the elements will be listed in the string returned
    # by __repr__.


class LenTestCase(unittest.TestCase):
    """Test __len__."""

    def test_len1(self):
        """Test __len__ with an empty bag."""
        bag = ArrayBag()
        self.assertEqual(len(bag), 0)

    def test_len2(self):
        """Test __len__ with a bag containing 1 element."""
        bag = ArrayBag([10])
        self.assertEqual(len(bag), 1)

    def test_len3(self):
        """Test __len__ with a bag containing no duplicate elements."""
        bag = ArrayBag([1, 4, 3, 6])
        self.assertEqual(len(bag), 4)

    def test_len4(self):
        """Test __len__ with a bag containing some duplicate elements."""
        bag = ArrayBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertEqual(len(bag), 8)

    def test_len5(self):
        """Test __len__ with a bag containing multiple elements, all identical."""
        bag = ArrayBag([2, 2, 2, 2, 2])
        self.assertEqual(len(bag), 5)


class ContainsTestCase(unittest.TestCase):
    """Test __contains__."""

    def test_contains1(self):
        """Test __contains__ with an empty bag."""
        bag = ArrayBag()
        self.assertFalse(2 in bag)

    def test_contains2(self):
        """Test __contains__ with a bag containing 1 element."""
        bag = ArrayBag([10])
        self.assertTrue(10 in bag)
        self.assertFalse(2 in bag)

    def test_contains3(self):
        """Test __contains__ with a bag containing no duplicate elements."""
        bag = ArrayBag([1, 4, 3, 6])
        self.assertTrue(1 in bag)
        self.assertTrue(4 in bag)
        self.assertTrue(3 in bag)
        self.assertTrue(6 in bag)
        self.assertFalse(2 in bag)

    def test_contains4(self):
        """Test __contains__ with a bag containing some duplicate elements."""
        bag = ArrayBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertTrue(1 in bag)
        self.assertTrue(4 in bag)
        self.assertTrue(6 in bag)
        self.assertTrue(9 in bag)
        self.assertFalse(2 in bag)

    def test_contains5(self):
        """Test __contains__ with a bag containing multiple elements, all identical."""
        bag = ArrayBag([2, 2, 2, 2, 2])
        self.assertTrue(2 in bag)
        self.assertFalse(7 in bag)

# The following classes test the ArrayBag methods developed during Lab 3.


class CountTestCase(unittest.TestCase):
    """Test count (Exercise 1)."""

    def test_count1(self):
        """Test counting an empty bag"""
        bag = ArrayBag()
        self.assertEqual(0, bag.count(1))

    def test_count2(self):
        """Test counting on a non-empty bag"""
        bag = ArrayBag([1, 1, 3, 2, 4, 1, 1, 2, 6, 1])
        self.assertEqual(5, bag.count(1))


class RemoveTestCase(unittest.TestCase):
    """Test remove (Exercise 2)."""

    def test_remove1(self):
        """Test removing from an empty bag."""
        bag = ArrayBag()
        with self.assertRaises(ValueError):
            bag.remove(10)

    def test_remove2(self):
        """Test removing an item that isn't in the bag."""
        bag = ArrayBag([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(ValueError):
            bag.remove(10)

    def test_remove3(self):
        """Test removing the first element in a bag"""
        bag = ArrayBag([1, 1, 3, 2, 4, 2, 3, 4, 2])
        item = bag.remove(1)
        self.assertEqual(item, 1)
        self.assertEqual(bag.count(1), 1)
        self.assertEqual(len(bag), 8)

    def test_remove4(self):
        """Test removing an element in a bag"""
        bag = ArrayBag([1, 1, 3, 2, 4, 2, 3, 4, 2])
        item = bag.remove(3)
        self.assertEqual(item, 3)
        self.assertEqual(bag.count(3), 1)
        self.assertEqual(len(bag), 8)

    def test_remove5(self):
        """Test removing the last element in a bag"""
        bag = ArrayBag([1, 1, 3, 4, 3, 4, 2])
        item = bag.remove(2)
        self.assertEqual(item, 2)
        self.assertEqual(bag.count(2), 0)
        self.assertEqual(len(bag), 6)


class GrabTestCase(unittest.TestCase):
    """Test grab (Exercise 3)."""

    def test_grab1(self):
        """Test grabbing an item from an empty bag."""
        bag = ArrayBag()
        with self.assertRaises(ValueError):
            bag.grab()

    def test_grab2(self):
        """Test grabbing an item from a full bag"""
        bag = ArrayBag([1, 2, 3, 4, 5, 6, 7])
        item = bag.grab()
        self.assertTrue(item not in bag)
        self.assertEqual(len(bag), 6)


class DunderAddTestCase(unittest.TestCase):
    """Test __add__ (Exercise 4)."""

    def test_dunder1(self):
        """Test adding 2 empty bags"""
        bag1 = ArrayBag()
        bag2 = ArrayBag()
        with self.assertRaises(ValueError):
            bag3 = bag1 + bag2

    def test_dunder2(self):
        """Test adding a non-ArrayBag element"""
        bag1 = ArrayBag([1, 2, 3, 4])
        bag2 = [5, 6, 7, 8]
        with self.assertRaises(TypeError):
            bag3 = bag1 + bag2

    def test_dunder3(self):
        """Test adding an empty self and a populated other"""
        bag1 = ArrayBag()
        bag2 = ArrayBag([5, 6, 7, 8])
        bag3 = bag1 + bag2
        self.assertEqual(len(bag3), 4)

    def test_dunder4(self):
        """Test adding a populated self and an empty other"""
        bag2 = ArrayBag()
        bag1 = ArrayBag([1, 2, 3, 4])
        bag3 = bag1 + bag2
        self.assertEqual(len(bag3), 4)

    def test_dunder5(self):
        """Test adding a populated self and a populated other"""
        bag1 = ArrayBag([1, 2, 3, 4])
        bag2 = ArrayBag([5, 6, 7, 8])
        bag3 = bag1 + bag2
        self.assertEqual(len(bag3), 8)


class EqTestCase(unittest.TestCase):
    """Test __eq__ (Exercise 5)."""

    def test_eq1(self):
        """Test eq on 2 full bags"""
        bag1 = ArrayBag([1, 2, 3, 4])
        bag2 = ArrayBag([1, 2, 3, 4])
        self.assertEqual(bag1 == bag2, True)

    def test_eq2(self):
        """Test eq on 2 empty bags"""
        bag1 = ArrayBag()
        bag2 = ArrayBag()
        self.assertEqual(bag1 == bag2, True)

    def test_eq3(self):
        """Test eq on a non-ArrayBag other"""
        bag1 = ArrayBag([1, 2, 3, 4])
        bag2 = [5, 6, 7, 8]
        self.assertFalse(bag1 == bag2)

    def test_eq4(self):
        """Test eq on non-equal ArrayBags"""
        bag1 = ArrayBag([1, 2, 3, 4])
        bag2 = ArrayBag([5, 6, 7, 8])
        self.assertEqual(bag1 == bag2, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
