def extend(self, iterable) -> None:
        """Extend this ArrayList with the elements from the iterable.

        >>> list1 = ArrayList([1, 3, 5])
        >>> list2 = ArrayList([2, 4, 6])
        >>> list1.extend(list2)
        >>> list1
        ArrayList([1, 3, 5, 2, 4, 6])

        >>> list1 = ArrayList([10, 20, 30])
        >>> tup = (60, 50, 40)
        >>> list1.extend(tup)
        >>> list1
        ArrayList([10, 20, 30, 60, 50, 40])
        """
        for item in iterable:
            self.append(item)
        self = ArrayList(self)