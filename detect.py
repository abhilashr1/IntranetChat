#!/usr/bin/python3

#https://www.olafrv.com/?p=450 !important
import threading
import os , socket
import neighbour
import time

class detect(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):

        self.own_ip = neighbour.get_address() 
        listener_port = 12345
        other_clients = []

        if self.name == 'server':
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            try:
                listener.bind((self.own_ip,listener_port))
                #Listen to upto 5 connections simultaneously
                listener.listen(5)
                while True:
                    (client_socket,client_addr)=listener.accept()

                    #Add code to add the client_addr to the list of online users.
                    #Temporarily adding code to append everything to a list

                    other_clients.append(client_addr)
                    print(">>>> Client detected : ",client_addr)
                    print('In thread : ',self.name)
            except:
                raise

        elif self.name == 'client':
            # Send signal to other systems to indicate presence   
            while True:
                all_connected = []
                all_connected = neighbour.neighbours()
                print('All Connected devices: ')
                print(all_connected)
                for mac,ip in all_connected:
                    client_notify = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    # Set timeout to prevent waiting for too long
                    client_notify.settimeout(15)
                    flag=1
                    print(ip)
                    time.sleep(10)
                    try:
                        client_notify.connect((ip,listener_port))
                    except Exception as e:
                        print('Error => ',e)
                        flag=0
                        pass
                    client_notify.close()
                print('>> All other clients notified.')
                return

                    #if flag==1:
                        # Successful connection
                        # Is this required?

if __name__=='__main__':

    server = detect('server')
    notifier = detect('client')

    server.start()
    notifier.start()