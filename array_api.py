#!/usr/bin/env python3
from math import floor


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = alloc(initial_size)
        self.size = 0
        self.chunk_size = chunk_size

    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data),
                                       ', '.join([str(item) for item in self.data])))

    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        # TODO verify this range is correct for adding to the last element in almost full array
        if 0 <= index < self.size:
            return True
        raise ValueError(
            "{} is not within the bounds of the current array. {}".format(index, self.data))

    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        return sum(x is None for x in self.data) == 0

    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        empty = len(self.data) - self.size
        chunks_to_remove = floor(empty / self.chunk_size)
        # verify that there is at least one chunk to deallocate
        if chunks_to_remove < 1:
            return
        # remove empty elements on right end of the array
        new_array = self.data[:-(self.chunk_size * chunks_to_remove)]
        self.data = new_array

    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        # _check_increase to see if it's full
        if self._check_increase():
            self.data = memcpy(alloc(self.size + self.chunk_size), self.data)
        self.data[self.size] = item
        self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        # _check_increase
        self._check_bounds(index)
        if self._check_increase():
            print("allocate more for insert")
            self.data = memcpy(alloc(self.size + self.chunk_size), self.data)
        self.data = self.data[:index] + [item] + self.data[index:-1]
        self.size += 1

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.data[index] = item
        return None

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            return self.data[index]

    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.data = self.data[:index] + self.data[index+1:] + [None]
            self.size -= 1
            self._check_decrease()

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        self._check_bounds(index1)
        self._check_bounds(index2)
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]


###################################################
# Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    return [None] * size


def memcpy(dest, source, size=0):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    new = source[:]
    new_array = new + dest[len(source):]
    return new_array
