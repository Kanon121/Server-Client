from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep
import os
import pygame
import subprocess
from time import gmtime, strftime
class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        print data

    def Network_StartServer(self, data):
        self._server.StartServer()

class GameServer(Server):
    channelClass = ClientChannel
    
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)     
        self.client = None
    
    def StartServer(self):
        print "starting server"
        p = subprocess.Popen("RunServer.bat", cwd= os.getcwd(), creationflags=subprocess.CREATE_NEW_CONSOLE)
        stdout, stderr = p.communicate()   
        
    
    def Connected(self, channel, addr):
        print "new connection at time: " + strftime("%Y-%m-%d %H:%M:%S")
        self.client = channel
        self.client.Send({"action":"ServerOnline"})
        


    
print "LISTENING FOR CONNECTIONS"

mainServer = GameServer(localaddr=("192.168.2.100", 31425))

while True:
    mainServer.Pump()
    sleep(0.01)
    
    
    
    
    