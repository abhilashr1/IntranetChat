import sys
import time
import UI2 as UI
import neighbour
import pprint
import threading
import os , socket
import detect
from random import randint
import re

# BEGIN UI imports
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
# END UI imports


# UI Loader

class UI_Loader(UI.Ui_MainWindow):
    def __init__(self):
        self.username = {
        0: 'Panda',
        1: 'Popeye',
        2: 'Peacock',
        3: 'Lion',
        4: 'Tiger',
        5: 'Zoidberg',
        6: 'Bugs Bunny',
        7: 'Lola',
        8: 'Monalisa',
        9: 'Schrodinger'
        }

        '''self.own_ip = neighbour.get_address() 
        self.getport = 54321

        # Set up the universal server
        self.uniserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.uniserv.bind((self.own_ip,self.getport))
        self.uniserv.listen(5)
        '''


    def refreshconvo(self,dest):
        path = os.path.join(os.getcwd(), 'data')

        if os.path.isdir(path):
            # Path exists, Fetch item
            self.filepath=os.path.join(path, '')
            self.filepath+=dest
            if os.path.isfile(self.filepath):
                with open(self.filepath,'r') as f:
                    text=f.read()
            else:
                with open(self.filepath,'w') as f:
                    f.write('*****************************************************\n\tCHAT WITH '+dest+'\n*****************************************************\n\n\n')
                text = '*****************************************************\n\tCHAT WITH '+dest+'\n*****************************************************\n\n\n'


        else:
            # Create path and create file.
            self.filepath=os.path.join(path, '')
            self.filepath+=dest
            os.mkdir(path)
            with open(self.filepath,'w') as f:
                f.write('*****************************************************\n\tCHAT WITH '+dest+'\n*****************************************************\n\n\n')
            text = '*****************************************************\n\tCHAT WITH '+dest+'\n*****************************************************\n\n\n'


        # Load the text to GUI

        self.ui.MessageLogs.setPlainText(text)

    def getconvo(self,item):
        self.refreshconvo(item.text())
        


    '''def sendmessage(self,msg,dest):
        # The part which involves sending 

        # 1. Set up the universal server to listen

        (putsocket,recvaddr)=self.uniserv.accept()
        print('>> New message from ',recvaddr)
        username = 
    '''


    def send(self):
        message = self.ui.User_LogRetrieve.toPlainText()
        self.ui.User_LogRetrieve.clear()

        username = self.ui.User.toPlainText()
        if username=='' or username==' ':
            username=self.username[randint(0,9)]
        message = username+' >> '+message+'\n\n';

        with open(self.filepath,'a') as f:
            f.write(message)

        #reload the convoscreen
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', self.filepath )
        dest=ip[0]

        print('>> Destination : ',dest,'\n>> Message: ',message)
        self.client_send = threading.Thread(target=detect.client, args=(dest,message))
        self.client_send.start()

        self.refreshconvo(dest)


    def fillclients(self):
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.statusbar.showMessage(">> Refreshing Clients list ... ")
        ui_list = self.ui.UserList
        list_of_neighbours = neighbour.neighbours()
        no_of_neighbours = len(list_of_neighbours)

        for i in range(no_of_neighbours):
            itemstr = [j for (k,j) in enumerate(list_of_neighbours[i])]
            item = QtGui.QListWidgetItem(itemstr[1])
            print(itemstr[1])
            ui_list.connect(ui_list,SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")),self.getconvo)
            ui_list.addItem(item)

        # Adding own IP for TESTING
        ui_list.addItem('192.168.0.100')

        QtCore.QObject.connect(self.ui.RetrieveLog_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fillclients)

        ipaddress = socket.gethostbyname(socket.gethostname())
        ipfield = self.ui.IP.setPlainText(ipaddress)
        print("refreshed")
        self.ui.statusbar.showMessage(">> Done")

    def load(self):
        app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.fillclients()
        self.ui.User.setPlainText(self.username[randint(0,9)])
        QtCore.QObject.connect(self.ui.RetrieveLog_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fillclients)
        QtCore.QObject.connect(self.ui.RetrieveLog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send)
        self.MainWindow.show()
        sys.exit(app.exec_())




class MAIN(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name



    def run(self):
        if self.name=='ui':
            print('>> Loading...')

            # Wake up the Neighbours

            list_of_neighbours = neighbour.neighbours()
            print(">> Detected list of Neighbours ")

            # Load up the UI
            ui = UI_Loader()
            ui.load()

        elif self.name=='network':
            server = detect.detect('server')
            notifier = detect.detect('client')

            server.start()
            notifier.start()





if __name__=='__main__':

    try:
        runner_ui = MAIN('ui')
        runner_ui.start()

        runner_net = MAIN('network')
        runner_net.start()
    except Exception as e:
        print('>> Exiting. Reason: ',e)
