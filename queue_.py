class Queue_:
    """
    queue class
    fuction
        enque: push an item into the end of the queue
        deque: return and pop the first item of queue
        isEmpty: judge whether the queue is empty or not
        size: return the size of queue
    """
    def __init__(self):
        self.num = 0
        self.data = list()
        self.first = None

    def enque(self,item):
        """

        :param item: the item need to be pushed into queue
        :return:
        """
        self.data.append(item)
        if self.first is None:
            self.first = 0
        self.num += 1

    def deque(self):
        """

        :return: the popped item
        """
        item = self.data[self.first]
        self.data[self.first] = None
        self.first += 1
        self.num -= 1
        if self.num > 0 and self.num == int(len(self.data)/4):
            self.data = self.data[self.first:]
            self.first = 0
        elif self.num == 0:
            self.data = list()
            self.first = None
        return item

    def isEmpty(self):
        """

        :return: whether the queue is empty
        """
        return self.num == 0

    def size(self):
        """

        :return: the size of queue
        """
        return self.num

    def top(self):
        """

        :return: the first item in queue
        """
        return self.data[self.first]

    def get_first_index(self):
        return self.first