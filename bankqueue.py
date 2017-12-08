import queue_
import person
import counter
import numpy as np
import matplotlib.pyplot as plt

each_hour_quan = np.zeros(8,'int64')
waitingtime_each_hour = np.zeros(8,'float64')
for k in range(300):
    number_persons = person.get_number_persons()
    person_queue = person.init_prepareing_queue(number_persons)
    queue_line = queue_.Queue_()
    counter_ = list()
    for i in range(3):
        counter_.append(counter.counter())
    time = person.time_(9,0)
    end_time = person.time_(17,0)
    while not person_queue.isEmpty() or not queue_line.isEmpty():
        while not person_queue.isEmpty():
            if person_queue.top().entertime == time:
                queue_line.enque(person_queue.deque())
            else:
                break
        for i in range(len(counter_)):
                if counter_[i].available() is True:
                    if queue_line.isEmpty():
                        break
                    else:
                        customer = queue_line.deque()
                        counter_[i].set_workingtime(customer.affairtime)
                        each_hour_quan[customer.entertime.hour-9] += 1
                        waitingtime_each_hour[customer.entertime.hour-9] += customer.waitingtime
        time.increment()
        for i in range(len(counter_)):
            if not counter_[i].available():
                counter_[i].decrement_workingtime()
        first = queue_line.get_first_index()
        for i in range(queue_line.size()):
            queue_line.data[first+i].increment_waiting()
waitingtime_each_hour /= each_hour_quan
plt.plot(range(9,17),waitingtime_each_hour)
plt.title("The average waiting time during a day")
plt.savefig('The average waiting time during a day')
plt.show()


