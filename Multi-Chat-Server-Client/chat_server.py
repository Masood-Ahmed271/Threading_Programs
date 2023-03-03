'''
    Description: 
        This is a simple chat server that can handle multiple clients. 
        We have used socket programming and threading to implement this server.
        The server will be able to receive messages from the clients and send them back to the clients.
        The server will be able to handle multiple clients at the same time.
    Author:
        Masood Ahmed

'''

import socket
import threading

clients = [] # new clients will be added to this list

# contain the logic of each client. Each client should
# be able to exchange messages with the server. 
class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr
    
    # The function will contain the logic of each client
    # connected to the server. "run()" function will be called after you create 
    # a new instance of the ClientThread and calling the "start()" function.
    def run(self):
        while True:

            # receive data stream from client. 
            # it won't accept data packet greater than 1024 bytes
            data = self.conn.recv(1024).decode()

            # if no data is received from the client, break this loop
            if not data:
                break

            # print the data received from the client
            print("from connected user: " + str(data))

            # now it's the server's turn to reply to the client's message.
            # take input from the console screen using "input()" function then, send
            # the message to the client using "self.conn.send()" function. 
            reply = input(' -> ')
            self.conn.send(reply.encode())
        
        # close the connection "self.conn" and remove it from the list
        # that stores all the client's connections. 
        self.conn.close()
        clients.remove(self.conn)





def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(100)

    while True:
        
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        # create a new instance of ClientThread
        new_client = ClientThread(conn, address)

        # add the newly created instance to the client's list
        clients.append(new_client)

        # start the thread of the newly created instance of 
        # ClientThread using "start()" function.
        new_client.start() 


if __name__ == '__main__':
    server_program()