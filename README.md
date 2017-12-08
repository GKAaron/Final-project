

# Title: Simple Bank Queuing

## Team Member(s):
Ke Gou

# Monte Carlo Simulation Scenario & Purpose:
Using Monte Carlo Simulation simulates the number of customers for each day in Bank of China in my hometown and the amount of time for each individual individual. Those two simulations will help me to approximately evaluate the average waiting time for customers given a specific amount of counters. 
### Hypothesis before running the simulation:
My simulation is trying to figure out an answer to the above question. Thus I don't do any hypothesis.
### Simulation's variables of uncertainty
Three main variables. The number of customers visiting the bank each day, the amount of time for each individual bussiness and the time each customer arriving at the bank.

For the first variable, the number of customers visiting the bank each day, its distribution is poisson distribution. After I asked my friend who is working in this bank, I got the mean number of customers visiting the bank each day, which is 75.

For the second variable, I also got information from my friend. There are two main kinds of individual businesses.One is simple, which will take 10 minutes on average. The other is complicated, which will take 25 minutes on average. And the probability distribution is approximately like a binonomial distribution in which the probability of simple business is 0.9 and the probability of complicated business is 0.1.

In my simulation, I consider the normal situation for a single day, which means that I only consider the waiting on average in each hour during business hours which are from 9am to 5pm. According to the data I collected from my friend, I approximately considered that the probability for each person to visit the bank during 9am to 10am is 1/3. The probability for each person to visit the bank during 10am to 4pm is 1/18. The probability for each person to visit the bank during 4pm to 5pm is 1/3.
What's more, the number of counters in the bank is 3. At the beginning, every counter is available.
## Instructions on how to use the program:
I set the program to simulate 300 times

In each simulation:

The program will iterate approximately the number of minute during business hours(from 9am to 5pm) times.

I will create a time counter to record the time in simulation, the unit is minute. And each iteration the counter will increment 1 as one minute flees in real world.

First of all, using poisson distributon generates the number of customers who will visit the bank. 

Second, using other two probability distributions I mentioned above to initialize customers in order to determine the time when they will come to bank and how long their individual businesses will take.

Third, using a preparing queue to store all the customers who have not arrived at the bank in the order of their comeing time. And there is another waiting queue for customers who have already arrive at the bank but still wait in line.

In each iteration, if the preparing queue is not empty:
when the top item's entertime in preparing queue equals to the time counter. The waiting queue will push the item which is the top item pushed from preparing queue. Then go through the 3 counters, if any one is available, if the waiting queue is not empty, it will push the top item as the customer in the head of the waiting line will get service from the available counter in real world. And the program will set the customer's business time as the working time of available counter which will start a new business in this iteration.

Every time the waiting queue pops an item, the program will record not only the time when the customer arrives at the bank using hour as unit, but also the customer's waiting time.

After those procedure, the time counter will increment 1. Each item in waiting line will increment their waiting time by 1. And each counter which is occupied will decrement their working time by 1. If the working time becomes 0, the counter will be available again.

After each simulation, the program will get the total number of customers in every hour during business hours and total waiting time in every hour during business hours.

After finishing all simulations, the program will calculate the waiting time on average based on every hour during business hours.
## Sources Used:
All the data is from my friend who is working in the bank.
## Result:
The result is shown in picture
