"""
Given an Iterator class interface with methods: next() and hasNext(),
design and implement a PeekingIterator that support the peek() operation -- it essentially 
peek() at the element that will be returned by the next call to next()

https://leetcode.com/problems/peeking-iterator/
"""

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.store = self.iterator.next() if self.iterator.hasNext() else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.store
        

    def next(self):
        """
        :rtype: int
        """
        temp=self.store
        self.store = self.iterator.next() if self.iterator.hasNext() else None
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.store!=None

        