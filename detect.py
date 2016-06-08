#!/usr/bin/python3

import os , socket

# local IP adress of your computer
own_ip = socket.gethostbyname(socket.gethostname()) 
listener_port = 12345

def init_server():
    # Server to listen for any active machines 

    #TCP Socket
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    other_clients = []

    try:
        listener.bind((own_ip,listener_port))
        #Listen to upto 5 connections simultaneously
        listener.listen(5)
        while True:
            (client_socket,client_addr)=listener.accept()

            #Add code to add the client_addr to the list of online users.
            #Temporarily adding code to append everything to a list

            other_clients.append(client_addr)
            print("Client detected : ",client_addr)
            break
    except:
        raise

init_server()