from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_a = deque()
        self.stack_b = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        self.stack_a.append(x)
        while self.stack_b:
            self.stack_a.append(self.stack_b.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack_a.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack_a[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.stack_a)