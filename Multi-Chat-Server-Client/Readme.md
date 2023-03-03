# README

This is a simple chat server implemented in Python that allows multiple clients to connect and exchange messages with the server. The server listens on port 5000 and accepts incoming connections from clients.

## Prerequisites

    Python 3.x

## Getting started

- Open a terminal or command prompt and navigate to the project directory.

- Run the following command to start the server: *python chat_server.py*

- Open two additional terminals or command prompts and navigate to the project directory.

- In each terminal or command prompt, run the following command to start a client: *python client.py* 
This will create two client instances that will connect to the server.

- Start typing messages in each client terminal and see how the messages are sent and received by the server and other connected clients.


## Simulation Screenshot
</br>

![Getting Started](./simulation_screenshot.png)

## Conclusion

In this simulation, we used a single instance of the chat server and two client instances to demonstrate how clients can connect to the server and exchange messages with each other. Each client instance was implemented using the ClassThread class, which allowed multiple clients to connect to the server simultaneously and communicate with each the server independently. The server was able to handle multiple connections using a list of connections that stored each client's socket connection.

During the simulation, we were able to see how messages sent by one client were received by the server and how server replied to the messages sent from the respective clients. We also saw how the server was able to handle multiple connections and manage the exchange of messages between clients. Overall, this simple chat server provides a good starting point for implementing more complex chat applications that require multiple clients to connect and communicate with each other.

Among some other things observed, we can see that if server initiates the first message, then that message reaches to the first client after the client has sent a message to the server. Moreover, if a client sends two messages at the same time, then the second message will be sent to the server only after server has replied to the first message and so on.