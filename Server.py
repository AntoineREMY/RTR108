
import threading
import socketserver
import time







HOST, PORT = "localhost", 4000
server = None
serverTH = None
Online = False 


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for TCP server.
    """
    def TaskHandle(self,Data,Ip):
        if str(Data) == "b'1'":
            print("{} : send a 1".format(str(Ip)))
            try:
                self.request.sendall(bytes("Ok\n", "utf-8"))
            except Exception as e:
                print("Error message couldn't be sent : {}".format(e))
        else:
            print("Unknow Task :",end=' ')
            print(Data)
    
    
    def handle(self):
        global Task1TH
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # Do the operation in a other thread
        Task1TH = threading.Thread(target=self.TaskHandle,args=(self.data,self.client_address[0]))
        Task1TH.daemon = True
        Task1TH.start()
    
    

def CommandInput():
    print("------Server version 0.01-------\ntype Help to see all the command")
    
    while(True):
        temp = input()
        if(len(temp) == 4 and temp.lower() == "stop"):
            ServerStop()
        elif(len(temp) == 5 and temp.lower() == "start"):
            ServerStart()
        elif(len(temp) == 5 and temp.lower() == "close"):
            CloseServer()
            return
        elif(len(temp) == 4 and temp.lower() == "help"):
            print("List of command:\n-Start : start/restart the server\n-Stop : stop the server\n-Close : close the server\n-Send -s : Send a message to all connected socket(not working)")
        elif(temp.lower().startswith("send")):
            try:
                server.BaseRequestHandler.request.sendall(bytes(temp[4:], 'ascii'))
            except Exception as e:
                print("Error message couldn't be sent : {}".format(e))
        else:
            print("Invalid command")

def ServerStop():
    global server
    global Online
    if(Online):
        server.socket.close()
        Online = False
        print("Server stoped")
    else:
        print("Server is not ONLINE")
def CloseServer():
    global server
    global Online
    global Task1TH
    if(Online):
        server.socket.close()
        Online = False
    print("Server is closing in 3s ...")    
    time.sleep(3)
    
    
def ServerStart():
    global server
    global serverTH
    global Online
    global Task1TH
    try:
        if(Online):
            print("Server is already ONLINE")
            return
        Online = True
        print("Server binding ...")
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
        serverTH = threading.Thread(target=server.serve_forever)
        serverTH.daemon = True
        print("Server starting ...")
        serverTH.start()
    except Exception as e:
        print("Server Crashed ;(\n{}".format(e))
        Online = True
        CloseServer()

def exit_handler():
    ServerStop()

CommandInput()