"""Singly-linked lists."""


from __future__ import annotations # ?
from typing import Generic, TypeVar, Optional # ?

T = TypeVar('T')  # Generic type variable # ?


class Link(Generic[T]):
    """A link in a singly linked list."""

    head: T # something to do with type checking?
    tail: LList[T] # something to do with type checking?

    def __init__(self, head: T, tail: LList[T]):
        """Prepend a new head to tail."""
        self.head = head
        self.tail = tail

    def __repr__(self) -> str:
        """Representation string."""
        return f'Link({self.head}, {self.tail})'


LList = Optional[Link[T]] 


def length(x: LList[T]) -> int:
    """
    Get the length of x.

    >>> length(None)
    0
    >>> length(Link(1, None))
    1
    >>> length(Link(1, Link(2, None)))
    2
    """
    if x == None:
        return 0
    acc = 0
    while x:
        acc += 1
        x = x.tail
    return acc


def drop(x: LList[T], k: int) -> LList[T]:
    """
    Drop the first k elements in the list.

    If length(x) < k, return the empty list (None).

    >>> drop(None, 1) is None
    True
    >>> drop(Link(1, None), 1) is None
    True
    >>> drop(Link(1, Link(2, None)), 1)
    Link(2, None)
    """
    if k > length(x):
        return None
    while k:
        x = x.tail
        k -= 1
    return x


def reverse(x: LList[T]) -> LList[T]:
    """
    Reverse a list.

    You decide whether you are allowed to modify the existing list
    or if you want to return a new list and leave the original one
    intact.

    # return new list.

    >>> reverse(None) is None
    True
    >>> reverse(Link(1, None))
    Link(1, None)
    >>> reverse(Link(1, Link(2, Link(3, None))))
    Link(3, Link(2, Link(1, None)))
    """
    lst = None
    while x:
        lst = Link(x.head, lst)
        x = x.tail
    return lst


def take(x: LList[T], k: int) -> LList[T]:
    """
    Return a list with the first k elements in x.

    If length(x) < k, return the full list. You decide whether you
    want to return a copy of x or the original list.

    # return original list. 

    >>> take(None, 1) is None
    True
    >>> take(Link(1, None), 1)
    Link(1, None)
    >>> take(Link(1, Link(2, Link(3, None))), 2)
    Link(1, Link(2, None))
    """
    lst = None
    for _ in range(k):
        if x is None:
            return x
        lst = Link(x.head, lst)
        x = x.tail
    return reverse(lst)
