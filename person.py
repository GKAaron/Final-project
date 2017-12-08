import numpy as np
import queue_

def get_number_persons():
    """

    :return: the number of persons who will enter the bank
    """
    return np.random.poisson(75)


def get_entertime():
    """

    :return: a time_ class instance indicating the time when the person enters bank
    """
    hour = np.random.randint(4,22)
    min = np.random.randint(0,60)
    if hour <= 9:
        hour = 9
    elif hour >= 16:
        hour = 16
    return time_(hour,min)


def get_affairtime():
    """

    :return:  the time the person needs to finish the affair
    """
    type = np.random.randint(0,10)
    if type == 0:
        affairtime = 25
    else:
        affairtime = 10
    return affairtime


class time_:
    def __init__(self,hour,min):
        self.hour = hour
        self.min = min

    def __lt__(self,other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour:
            return self.min < other.min
        else:
            return False

    def __eq__(self,other):
        if self.hour == other.hour:
            if self.min == other.min:
                return True
        return False

    def increment(self):
        """
        calculate the time
        :return:
        """
        self.min += 1
        if self.min==60:
            self.hour += 1
            self.min = 0


class person:
    def __init__(self):
        self.entertime = get_entertime()
        self.affairtime = get_affairtime()
        self.waitingtime = 0

    def increment_waiting(self):
        """
        increment the waiting time
        :return:
        """
        self.waitingtime += 1

    def __lt__(self,other):
        return self.entertime < other.entertime


def init_prepareing_queue(number):
    """

    :param number: the number of persons will enter the bank
    :return: a queue of persons who will entering the bank in the order of entertime
    """
    queue_persons = queue_.Queue_()
    for i in range(number):
        queue_persons.enque(person())
    queue_persons.data.sort()
    return queue_persons