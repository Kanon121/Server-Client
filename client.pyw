import pygame
import os
from Window import Window
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import sys

online = "You have connected!"
offline = "Problem connecting, is MC server running?"
startedServer = "Starting server. If server is stopped: "
startedServer1 = "reopen client, and re-start server. "
startButton = "START SERVER"
serverOnline = False
class Connector(ConnectionListener):
    
    def __init__(self):
        self.Connect(("24.107.238.188", 31425))
        self.running = True
        self.serverOnline = False
        self.MinecraftOnline = False
        
        while not self.running:
            connection.Pump()
            self.Pump()          
            sleep(0.01)
  


    def update(self):
        connection.Pump()
        self.Pump() 
        
        for e in pygame.event.get():
            posx, posy = pygame.mouse.get_pos()
            if e.type == pygame.QUIT:
                connector.running = False
            
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                connector.running = False
                sys.exit()
        
        
        
        
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    if startTextRect.collidepoint(posx, posy):
                        if self.serverOnline:
                            self.Send({'action': 'StartServer'})
                            self.MinecraftOnline = True      
        
        
        if not self.MinecraftOnline:
            if self.serverOnline:
                window.screen.blit(onlineText, (120, 100))
                window.screen.blit(startText, (120, 150))
            else:
                window.screen.blit(offlineText, (5, 100))
        
        else:
            window.screen.blit(startedServerText, (0, 100))
            window.screen.blit(startedServerText1, (0, 120))
        
        pygame.display.flip()
        window.RenderWindow("black")
      
    
    def Network(self, data):
        #print data
        pass
    
    def Network_ServerOnline(self, data):
        self.serverOnline = True
        


    
window = Window()
screen_width = 400
screen_height = 400
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 15)
myfontBig = pygame.font.SysFont("monospace", 20)
onlineText = myfont.render(online, 1, (0,255,0))
offlineText = myfont.render(offline, 1, (255,0,0))
startedServerText = myfont.render(startedServer, 1, (255,255,255))
startedServerText1 = myfont.render(startedServer1, 1, (255,255,255))
startText = myfont.render(startButton, 1, (0,255,0))
startTextRect = pygame.Surface.get_rect(startText)
startTextRect.x = 120
startTextRect.y = 150
connector = Connector()    

      
        
while connector.running:
    connector.update()
    





