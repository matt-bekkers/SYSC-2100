# SYSC 2100 Winter 2024 Lab 2: Unit tests for class ListBag.

import unittest

from lab2_listbag import ListBag

import random

# The first seven classes test the methods in the ListBag class
# presented in lectures.


class InitTestCase(unittest.TestCase):
    """Test __init__."""

    # The tests in this class access the "private" list in the ListBag object
    # directly, because __init__ is the first method we implement, so the other
    # methods won't be available.

    def test_init1(self):
        """Test __init__: no iterable passed to to ListBag()."""
        bag = ListBag()
        self.assertEqual(bag._elems, [])

    def test_init2(self):
        """Test __init__: empty iterable passed to ListBag()."""
        bag = ListBag([])
        self.assertEqual(bag._elems, [])

    def test_init3(self):
        """Test __init__: non-empty iterable with no duplicate elements passed to ListBag()."""
        bag = ListBag([1, 4, 3, 6])

        # Create a sorted list from the ListBag's list. This means that the
        # test doesn't depend on the bag's elements being stored in any
        # particular order.

        self.assertEqual(sorted(bag._elems), [1, 3, 4, 6])

    def test_init4(self):
        """Test __init__: non-empty iterable with duplicate elements passed to ListBag()."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertEqual(sorted(bag._elems), [1, 1, 4, 4, 4, 6, 6, 9])


class AddTestCase(unittest.TestCase):
    """Test add."""

    # These tests assume that __init__ can create an empty ListBag.
    # The tests access the "private" list in the ListBag object directly.
    # This means that no other ListBag methods need to be implemented in
    # order to test add.

    def test_add1(self):
        """Add items (no duplicates) to an empty bag."""
        bag = ListBag()
        for x in [1, 4, 3, 6]:
            bag.add(x)
        self.assertEqual(sorted(bag._elems), [1, 3, 4, 6])

    def test_add2(self):
        """Add items (some duplicated) to an empty bag."""
        bag = ListBag()
        for x in [1, 4, 4, 1, 9, 4, 6, 6]:
            bag.add(x)
        self.assertEqual(sorted(bag._elems), [1, 1, 4, 4, 4, 6, 6, 9])


class IterTestCase(unittest.TestCase):
    """Test __iter__."""

    def test_iter1(self):
        """Test iteration over an empty bag."""
        bag = ListBag()
        elems = []
        for elem in bag:
            elems.append(elem)
        self.assertEqual(elems, [])

    def test_iter2(self):
        """Test iteration over a bag containing some duplicate elements."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        elems = []
        for elem in bag:
            elems.append(elem)
        self.assertEqual(sorted(elems), [1, 1, 4, 4, 4, 6, 6, 9])


class StrTestCase(unittest.TestCase):
    """Test __str__.

    Verify that __str__ returns a string representation of the ListBag
    in the expected format.
    """

    def test_str1(self):
        """Test __str__ with an empty bag."""
        bag = ListBag()
        self.assertEqual(str(bag), '{}')

    def test_str2(self):
        """Test __str__ with a bag containing one element."""
        bag = ListBag([10])
        self.assertEqual(str(bag), '{10}')

    def test_str3(self):
        """Test __str__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertEqual(str(bag), '{2, 2, 2, 2, 2}')

    # We don't test the case in which the bag contains elements that aren't
    # duplicates, because elements in a bag are unordered, so we don't know
    # the order in which the elements will be listed in the string returned
    # by __str__.


class ReprTestCase(unittest.TestCase):
    """Test __repr__.

    Verify that __repr__ returns a string representation of the ListBag
    in the expected format.
    """

    def test_repr1(self):
        """Test __repr__ with an empty bag."""
        bag = ListBag()
        self.assertEqual(repr(bag), 'ListBag([])')

    def test_repr2(self):
        """Test __repr__ with a bag containing one element."""
        bag = ListBag([10])
        self.assertEqual(repr(bag), 'ListBag([10])')

    def test_repr3(self):
        """Test __repr__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertEqual(repr(bag), 'ListBag([2, 2, 2, 2, 2])')

    # We don't test the case in which the bag contains elements that aren't
    # duplicates, because elements in a bag are unordered, so we don't know
    # the order in which the elements will be listed in the string returned
    # by __repr__.


class LenTestCase(unittest.TestCase):
    """Test __len__."""

    def test_len1(self):
        """Test __len__ with an empty bag."""
        bag = ListBag()
        self.assertEqual(len(bag), 0)

    def test_len2(self):
        """Test __len__ with a bag containing 1 element."""
        bag = ListBag([10])
        self.assertEqual(len(bag), 1)

    def test_len3(self):
        """Test __len__ with a bag containing no duplicate elements."""
        bag = ListBag([1, 4, 3, 6])
        self.assertEqual(len(bag), 4)

    def test_len4(self):
        """Test __len__ with a bag containing some duplicate elements."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertEqual(len(bag), 8)

    def test_len5(self):
        """Test __len__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertEqual(len(bag), 5)


class ContainsTestCase(unittest.TestCase):
    """Test __contains__."""

    def test_contains1(self):
        """Test __contains__ with an empty bag."""
        bag = ListBag()
        self.assertFalse(2 in bag)

    def test_contains2(self):
        """Test __contains__ with a bag containing 1 element."""
        bag = ListBag([10])
        self.assertTrue(10 in bag)
        self.assertFalse(2 in bag)

    def test_contains3(self):
        """Test __contains__ with a bag containing no duplicate elements."""
        bag = ListBag([1, 4, 3, 6])
        self.assertTrue(1 in bag)
        self.assertTrue(4 in bag)
        self.assertTrue(3 in bag)
        self.assertTrue(6 in bag)
        self.assertFalse(2 in bag)

    def test_contains4(self):
        """Test __contains__ with a bag containing some duplicate elements."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertTrue(1 in bag)
        self.assertTrue(4 in bag)
        self.assertTrue(6 in bag)
        self.assertTrue(9 in bag)
        self.assertFalse(2 in bag)

    def test_contains5(self):
        """Test __contains__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertTrue(2 in bag)
        self.assertFalse(7 in bag)

# The following classes test the ListBag methods developed during Lab 2.


class CountTestCase(unittest.TestCase):
    """Test count (Exercise 1)."""

    def test_count0(self):
        """Test count on an empty bag"""
        bag = ListBag([1, 2, 3, 4, 5, 6])
        self.assertTrue(bag.count(7) == 0)
    def test_count1(self):
        """Test count on 1 element bag"""
        bag = ListBag([1])
        self.assertTrue(bag.count(1) == 1)
    def test_count2(self):
        """Test count on n element bag"""
        bag = ListBag([1, 2, 2, 3, 2])
        self.assertTrue(bag.count(2) == 3)


class RemoveTestCase(unittest.TestCase):
    """Test remove (Exercise 2)."""

    def test_remove1(self):
        """Test removing from an empty bag."""
        bag = ListBag()
        with self.assertRaises(ValueError):
            bag.remove(10)

    def test_remove2(self):
        """Test removing an item that isn't in the bag."""
        bag = ListBag([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(ValueError):
            bag.remove(10)
    
    def test_remove3(self):
        """Test removing an item present in a bag"""
        bag = ListBag([1, 3, 4, 4, 7, 2, 3])
        self.assertTrue(bag.remove(4) == 4)


class GrabTestCase(unittest.TestCase):
    """Test grab (Exercise 3)."""

    def test_grab1(self):
        """Test grabbing an item from an empty bag."""
        bag = ListBag()
        with self.assertRaises(ValueError):
            bag.grab()
    
    def test_grab2(self):
        """Test grabbing on a non-empty bag"""
        bag = ListBag([4, 2, 1, 3])
        self.assertTrue(bag.grab() in [1, 2, 3, 4])
        self.assertEqual(len(bag), 3)


class DunderAddTestCase(unittest.TestCase):
    """Test __add__ (Exercise 4)."""

    def test_dunder1(self):
        """Test an incorrect type for other"""
        other = [1, 2, 3, 4]
        bag = ListBag([5, 6, 7, 8])
        with self.assertRaises(TypeError):
            bag.add(self, other)
    
    def test_dunder2(self):
        """Test an empty self"""
        other = ListBag([1, 2, 3, 4])
        bag = ListBag([])
        new_bag = bag + other
        self.assertEqual(repr(sorted(new_bag)), '[1, 2, 3, 4]')
    
    def test_dunder3(self):
        """Test an empty other"""
        other = ListBag([])
        bag = ListBag([1, 2, 3, 4])
        new_bag = bag + other
        self.assertEqual(repr(sorted(new_bag)), '[1, 2, 3, 4]')

    def test_dunder4(self):
        """Test bag and other pre-sorted"""
        other = ListBag([5, 6, 7, 8])
        bag = ListBag([1, 2, 3, 4])
        new_bag = bag + other
        self.assertEqual(repr(sorted(new_bag)), '[1, 2, 3, 4, 5, 6, 7, 8]')

    def test_dunder5(self):
        """Test bag and other unsorted"""
        other = ListBag([5, 7, 6, 8])
        bag = ListBag([4, 3, 2, 1])
        new_bag = bag + other
        self.assertEqual(repr(sorted(new_bag)), '[1, 2, 3, 4, 5, 6, 7, 8]')


class EqTestCase(unittest.TestCase):
    """Test __eq__ (Exercise 5)."""
    
    def test_eq1(self):
        """Test on 2 equal bags"""
        bag1 = ListBag([1, 2, 3, 4])
        bag2 = ListBag([1, 2, 3, 4])
        return bag1 == bag2
    
    def test_eq2(self):
        """Test on 2 unequal bags"""
        bag1 = ListBag([1, 2, 3, 4, 5])
        bag2 = ListBag([1, 2, 3, 4])
        return bag1 == bag2
    
    def test_eq3(self):
        """Test on 1 empty bags"""
        bag1 = ListBag([])
        bag2 = ListBag([1, 2, 3, 4])
        return bag1 == bag2
    
    def test_eq4(self):
        """Test on 2 empty bags"""
        bag1 = ListBag([])
        bag2 = ListBag([])
        return bag1 == bag2


if __name__ == '__main__':
    bag = ListBag([1, 2, 3, 2, 4, 1, 2, 3, 1])
    item = random.randint(1, len(bag._elems) - 1)
    print(item)
    bag._elems.remove(bag._elems[item])
    print(bag)
    unittest.main(verbosity=2)
    