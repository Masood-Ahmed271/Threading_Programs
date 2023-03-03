# Producer Consumer Problem using Multi-threading

## Contributors:
---
Author: Masood Ahmed <br>
Email: masood20@connect.hku.hk<br>

---

## Main Observations:

time.sleep() for consumer is 0.5 and time.sleep() for producer is 0.1, hence the Producer Thread operates faster than Consumer Thread. 

## Test 1: (1 Producer and 1 Consumer)

```terminal/cmd
Producer 0 produced :  1
Consumer 0 consumed item :  1
Producer 0 produced :  2
Producer 0 produced :  3
Producer 0 produced :  4
Producer 0 produced :  5
Consumer 0 consumed item :  2
Producer 0 produced :  6
Producer 0 produced :  7
Producer 0 produced :  8
Producer 0 produced :  9
Producer 0 produced :  10
Consumer 0 consumed item :  3
Producer 0 produced :  11
Producer 0 produced :  12
Producer 0 produced :  13
Consumer 0 consumed item :  4
Producer 0 produced :  14
Consumer 0 consumed item :  5
Producer 0 produced :  15
Consumer 0 consumed item :  6
Producer 0 produced :  16
Consumer 0 consumed item :  7
Producer 0 produced :  17
Consumer 0 consumed item :  8
Producer 0 produced :  18
Consumer 0 consumed item :  9
Producer 0 produced :  19
Consumer 0 consumed item :  10
Producer 0 produced :  20
Producer 0: Done
ALL PRODUCERS FINISHED
Consumer 0: Done
Simulation Done
```

## Conclusions and Findings

As mentioned in the observation section, we already know that producer is running faster than consumer. In our test, we can clearly observe that by looking at the rate at which the producer is producing new items and putting them into the buffer. But as it progresses further .i.e when we reach to item number 14 produced by the consumer, we can see that the rate of producer and consumer seems to be equal. The reason for this is that the we are using a bounded buffer with a Capacity of 10 hence by the time producer produced item 13, the buffer became full and now producer can only add new items if there is space and this can only happen when consumer has consumed at-least one item. 

Therefore, the producer thread will be waiting unless until buffer has space for other items. Producer thead finally stops when all 20 items have been added. Once producers stops, a signal is sent to consumers and the consumer thread also stops consuming. In addition to that, in the test case 1, we can see that the producer has successfully generated a total of 20 elements, whereas the consumer has consumed 10 elements.


## Test 2: (2 Producer and 1 Consumer)

```terminal/cmd
Producer 0 produced :  1
Producer 1 produced :  1
Consumer 0 consumed item :  1
Producer 0 produced :  2
Producer 1 produced :  2
Producer 0 produced :  3
Producer 1 produced :  3
Producer 0 produced :  4
Producer 1 produced :  4
Producer 1 produced :  5
Producer 0 produced :  5
Consumer 0 consumed item :  1
Producer 1 produced :  6
Producer 0 produced :  6
Consumer 0 consumed item :  2
Producer 1 produced :  7
Consumer 0 consumed item :  2
Producer 0 produced :  7
Consumer 0 consumed item :  3
Producer 1 produced :  8
Consumer 0 consumed item :  3
Producer 0 produced :  8
Consumer 0 consumed item :  4
Producer 1 produced :  9
Consumer 0 consumed item :  4
Producer 0 produced :  9
Consumer 0 consumed item :  5
Producer 1 produced :  10
Consumer 0 consumed item :  5
Producer 0 produced :  10
Consumer 0 consumed item :  6
Producer 1 produced :  11
Consumer 0 consumed item :  6
Producer 0 produced :  11
Consumer 0 consumed item :  7
Producer 1 produced :  12
Consumer 0 consumed item :  7
Producer 0 produced :  12
Consumer 0 consumed item :  8
Producer 1 produced :  13
Consumer 0 consumed item :  8
Producer 0 produced :  13
Consumer 0 consumed item :  9
Producer 1 produced :  14
Consumer 0 consumed item :  9
Producer 0 produced :  14
Consumer 0 consumed item :  10
Producer 1 produced :  15
Consumer 0 consumed item :  10
Producer 0 produced :  15
Consumer 0 consumed item :  11
Producer 1 produced :  16
Consumer 0 consumed item :  11
Producer 0 produced :  16
Consumer 0 consumed item :  12
Producer 1 produced :  17
Consumer 0 consumed item :  12
Producer 0 produced :  17
Consumer 0 consumed item :  13
Producer 1 produced :  18
Consumer 0 consumed item :  13
Producer 0 produced :  18
Consumer 0 consumed item :  14
Producer 1 produced :  19
Consumer 0 consumed item :  14
Producer 0 produced :  19
Consumer 0 consumed item :  15
Producer 1 produced :  20
Producer 1: Done
Consumer 0 consumed item :  15
Producer 0 produced :  20
Producer 0: Done
ALL PRODUCERS FINISHED
Consumer 0: Done
Simulation Done
```

## Conclusions and Findings

Again, please. note that producer threads will be running faster then consumer thread as mentioned in the observation section. In this test, first 2 producer threads are produced then 1 consumer thread is produced. First the first 2 producer threads are started and after both producer threads have been started, then the consumer thread starts. The rest of the process is same as observed in Test 1 except that if one producer finishes earlier then it waits for all other producers to finish.

In the above case, producer 1 finishes earlier and it waits for producer 0 to finish as well before terminating all the producer threads which then signals the consumer thread to terminate as well. The test 2 highlights how the problem to signal to the consumer that there are no more tasks expected from any producers when having multiple producers can be solved. It can be solved by keeping track of how many producers have finished and only break the task when last producer alive is terminated. In addition to that, in the test case 2, we can see that the producer has successfully generated a total of 20 elements, whereas the consumer has consumed 15 elements in total. Last thing to notice is that in Test case 2, producer 1 completes before producer 0.


## Test 3: (2 Producer and 2 Consumer)

```terminal/cmd
Producer 0 produced :  1
Producer 1 produced :  1
Consumer 0 consumed item :  1
Consumer 1 consumed item :  1
Producer 0 produced :  2
Producer 1 produced :  2
Producer 0 produced :  3
Producer 1 produced :  3
Producer 0 produced :  4
Producer 1 produced :  4
Producer 0 produced :  5
Producer 1 produced :  5
Consumer 0 consumed item :  2
Consumer 1 consumed item :  2
Producer 1 produced :  6
Producer 0 produced :  6
Producer 1 produced :  7
Producer 0 produced :  7
Consumer 0 consumed item :  3
Producer 1 produced :  8
Consumer 1 consumed item :  3
Producer 0 produced :  8
Consumer 0 consumed item :  4
Consumer 1 consumed item :  4
Producer 1 produced :  9
Producer 0 produced :  9
Consumer 0 consumed item :  5
Producer 1 produced :  10
Consumer 1 consumed item :  5
Producer 0 produced :  10
Consumer 0 consumed item :  6
Producer 1 produced :  11
Consumer 1 consumed item :  6
Producer 0 produced :  11
Consumer 0 consumed item :  7
Producer 1 produced :  12
Consumer 1 consumed item :  7
Producer 0 produced :  12
Consumer 0 consumed item :  8
Producer 1 produced :  13
Consumer 1 consumed item :  8
Producer 0 produced :  13
Consumer 0 consumed item :  9
Producer 1 produced :  14
Consumer 1 consumed item :  9
Producer 0 produced :  14
Consumer 0 consumed item :  10
Producer 1 produced :  15
Consumer 1 consumed item :  10
Producer 0 produced :  15
Consumer 0 consumed item :  11
Producer 1 produced :  16
Consumer 1 consumed item :  11
Producer 0 produced :  16
Consumer 0 consumed item :  12
Producer 1 produced :  17
Consumer 1 consumed item :  12
Producer 0 produced :  17
Consumer 0 consumed item :  13
Producer 1 produced :  18
Consumer 1 consumed item :  13
Producer 0 produced :  18
Consumer 0 consumed item :  14
Producer 1 produced :  19
Consumer 1 consumed item :  14
Producer 0 produced :  19
Consumer 0 consumed item :  15
Producer 1 produced :  20
Consumer 1 consumed item :  15
Producer 0 produced :  20
Producer 1: Done
Producer 0: Done
ALL PRODUCERS FINISHED
Consumer 0: Done
Consumer 1: Done
Simulation Done
```

## Conclusions and Findings

Again, please. note that producer threads will be running faster then consumer thread as mentioned in the observation section. In the third test, we have observed how multiple producers coordinate in the termination of teh system and signalling to consumers that no more task are to be expected as well as this test allows us to observe that how consumers coordinate in the termination of the system ensuring that all consumers shutdown together. 

So, in the given test 3 output, we can see that first the 2 producers are started and then the 2 consumers are started. Producers put items in the buffer while consumers try their best to consume the items from the buffer.

Again as in test 2, as each producer thread finishes, it waits for all other producers to finish. When all producers have finished, they terminate and they signal the consumers to exit the task loop and they start to terminate as well.In addition to that, in the test case 1, we can see that the producer has successfully generated a total of 20 elements, whereas the consumer has consumed 15 elements in total.

*Thank you for reading. Stay happy and stay safe :)*