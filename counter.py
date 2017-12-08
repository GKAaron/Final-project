class counter:
    """
    bank counter
    function:
        set_workingtime: if there is a customer, working time will be set as the customer's affairtime
        decrement_workingtime: decrement working time, when it becomes zero, the counter is available again
    """
    def __init__(self):
        self.workingtime = 0
        self.avai = True

    def set_workingtime(self,time):
        self.workingtime = time
        self.avai = False

    def decrement_workingtime(self):
        """
        decrement working time, when it becomes zero, the counter is available again
        :return:
        """
        self.workingtime -= 1
        if self.workingtime == 0:
            self.avai = True

    def available(self):
        """

        :return: whether the counter is available
        """
        return self.avai