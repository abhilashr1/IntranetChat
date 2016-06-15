#!/usr/bin/python3

#https://www.olafrv.com/?p=450 !important
import threading
import os , socket
import neighbour
import time

# Changing the purpose of this to act as sender/receiver

class detect(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def addtofile(self,dest,message):

        message = message+'\n'

        path = os.path.join(os.getcwd(), 'data')
        if os.path.isdir(path):
            # Path exists, Fetch item
            self.filepath=os.path.join(path, '')
            self.filepath+=dest
            if os.path.isfile(self.filepath):
                with open(self.filepath,'a') as f:
                    f.write(message)
            else:
                with open(self.filepath,'w') as f:
                    f.write('*****************************************************\n\tCHAT WITH '+dest+'\n*****************************************************\n\n\n'+message)


        else:
            # Create path and create file.
            self.filepath=os.path.join(path, '')
            self.filepath+=dest
            os.mkdir(path)
            with open(self.filepath,'w') as f:
                f.write('*****************************************************\n\tCHAT WITH '+dest+'\n*****************************************************\n\n\n'+message)

        # Add code to refresh convo
        


    def run(self):

        self.own_ip = neighbour.get_address() 
        listener_port = 12345

        if self.name == 'server':
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            try:
                listener.bind((self.own_ip,listener_port))
                #Listen to upto 5 connections simultaneously
                listener.listen(5)
                while True:
                    (client_socket,client_addr)=listener.accept()

                    entire_message=''
                    while True:
                        msg = client_socket.recv(1024)
                        if not msg:
                            break
                        entire_message+=msg.decode(encoding='utf-8')
                    msg = entire_message.split(':::::')
                    dest = msg[0]
                    message = msg[1]

                    self.addtofile(dest,message)

            except:
                raise


def client(dest,message):
    sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # PORT IS NOT 12345 FOR TESTING PURPOSES
    port = 12346
    from_address = neighbour.get_address()
    sender.connect((dest,port))
    #Send the from addr
    entire_message = from_address+':::::'+message;
    sender.sendall(entire_message.encode())
    sender.close()


if __name__=='__main__':

    server = detect('server')

    server.start()
    notifier.start()