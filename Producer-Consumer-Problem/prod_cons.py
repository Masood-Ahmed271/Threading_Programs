'''
  Description: 
      Simulation of Producer Consumer Problem using Semaphores
  Author: 
      Masood Ahmed

'''
import threading
import time

# Shared Memory variables
CAPACITY = 10
finished = False
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
n_producers = 5
n_consumers = 5

barrier = threading.Barrier(n_producers)# This barrier is used to make sure that all producers finish at the same time. 

#  Declare the required semaphores here (mutex, empty, full) and initialize them with the proper values.
#  Declaring Semaphores
mutex = threading.Semaphore() # default value is 1
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

# Producer Thread Class
class Producer(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self, id=0):

        global CAPACITY, buffer, in_index, out_index, barrier, finished
        # mark the semaphores as global here
        global mutex, empty, full

        items_produced = 0
        counter = 0

        while items_produced < 20:
            # acquire one of the declared semaphores here
            empty.acquire()
            # acquire one of the declared semaphores here
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print(f"Producer {self.id} produced : ", counter)

            # release the semaphores here accordingly
            mutex.release()
            full.release()

            time.sleep(0.1)

            items_produced += 1

        print(f"Producer {self.id}: Done")
        # wait for all producers to finish
        barrier.wait()
        # signal that there are no further items
        if self.id == 0:
            print("ALL PRODUCERS FINISHED")
            finished = True


# Consumer Thread Class
class Consumer(threading.Thread):
  def __init__(self, id):
    super().__init__()
    self.id = id

  def run(self):
    global CAPACITY, buffer, in_index, out_index, counter
    # mark the semaphores as global here
    global mutex, empty, full

    items_consumed = 0
    while True:
      if finished == True:# if all producers are done, then we can stop consuming
        break;
      # use one of the declared semaphores here
      full.acquire()
      # use one of the declared semaphores here
      mutex.acquire()

      item = buffer[out_index]
      out_index = (out_index + 1) % CAPACITY

      print(f"Consumer {self.id} consumed item : ", item)

      # release the semaphores here accordingly
      mutex.release()
      empty.release()  

      time.sleep(0.5)

      items_consumed += 1
    print(f"Consumer {self.id}: Done")
    
      


# Creating Threads

producers = [Producer(id=i) for i in range(n_producers)] # to create n_producers threads
consumers = [Consumer(id=i) for i in range(n_consumers)] # to create n_consumers threads


# start the producers
# Starting Threads
# Loop through the producers and start them
for producer in producers:
  producer.start()

# Loop through the consumers and start them
for consumer in consumers:
  consumer.start()

# Waiting for threads to complete
# loop through the producers and join them using join() function
for producer in producers:
  producer.join()
# loop through the consumers and join them using join() function
for consumer in consumers:
  consumer.join()

print("Simulation Done")
