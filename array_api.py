#!/usr/bin/env python3


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
        return 0 <= index < self.size

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
        empty = sum(x is None for x in self.data)
        chunks_to_remove = empty / self.chunk_size
        print(empty)
        print(chunks_to_remove)

    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        # _check_increase to see if it's full
        if self._check_increase():
            print("allocate more")
            self.data = memcpy(alloc(self.size + self.chunk_size), self.data)
            self.data[self.size] = item
            self.size += 1
        else:
            self.data[self.size] = item
            self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        # _check_increase
        if self._check_increase():
            print("noop")
            # allocate more room
        else:
            print("noop")
            # simply insert the new item in its place and shift the rest over

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.data[index] = item
        else:
            raise ValueError(
                "Error: item not set, index outside of array bounds")
        return None

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            return self.data[index]
        else:
            raise ValueError(
                "Error: item not found, index outside of array bounds")

    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''


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
    new.extend(dest[len(source):])
    print(new)
    return new
