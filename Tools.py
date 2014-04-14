# -*- coding: utf-8 -*-
#Kronos - 0.1 [Abstract Anion] - Alpha
#Copyright (C) 2014 Blaise M Crowly  - All rights reserved
#Created at Xincoz [xincoz.com]
#GPL v3

"""This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.)"""

"""This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details."""



#Import necessary modules
import ping, socket
from colorama import init
init()
from colorama import Fore, Back, Style
import os

#Class to handle few operations on nodes list
class Nodes:
#Load a list of all nodes in the Nodes.Kronos file
  def GetList(self):
    if not os.path.isfile('Nodes.Kronos'):
        return {}
    else:
         Nodelist = {}
         NodeFile = open('Nodes.Kronos','r')
         for line in NodeFile:
             line = line.split('|')
             line[1] = line[1].replace('\n','')
             Nodelist.update({line[0]:line[1]})
         NodeFile.close()
         return Nodelist
#Add a node to the Nodes.Kronos file
  def NodeAdd(self,Remote):
    try:
      NodesFile = open('Nodes.Kronos','a')
    except:
      print "Could not open nodes file"
      return False
    NodesFile.write(str(Remote[0]+'|'+Remote[1]+'\n'))
    NodesFile.close()
    print "Added"
    return True





#Connection class to handle connection with the nodes
class Connection:
  Kon = ""
  SSLx = ""
  def Close(self):
    try:
      self.SSLx.close()
      return True
    except :
      return False
  
  def Send(self,Message):
    try:
      self.Kon.write(Message)
      return True
    except Exception,e:
      return False


  def Recieve(self):
    try:
      Response = self.Kon.read(10240)
      return Response
    except Exception,e:
      return False

#Conenct Function Makes a SSL connection with the node
  def Connect(self,Link):
    self.SSLx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Ip = Link[0].replace("'",'')
    Port = int(Link[1])
    try:
      self.SSLx.connect((Ip,Port)) 
      self.Kon = socket.ssl(self.SSLx)
      return True
    except Exception,e:
      print "Connection Attempt Failed"
      return False
  



#Network class with few network operations
class Network:
#chekc if a string represents an IP
  def IsIP(self,Remote):
    try:
      socket.inet_aton(addr)
      return True
    except:
      return False


#Ping operation checks if the a host is up using the Kronos PING request

  def Ping(self,Remote,AMODE = False):
#if AMODE is true the function will return the Connection object it creates instead of destroyit
#it will also abstain from printing the status if the host is up
        if not self.IsIP(Remote[0]):
            try:
              Ip = repr(socket.gethostbyname(Remote[0]))
            except:
              print "Could not resolve host "+Remote[0]
              return Fasle
        else:
            Ip = Remote[0]
        Host = (str(Ip),1984)
        Kon = Connection()
        if not Kon.Connect(Host):
           print "REMOTE HOST: " + Fore.RED + Remote[0] + Fore.RESET + "     STATUS: " + Fore.RED + "Down" + Fore.RESET
           return False
        if not Kon.Send(Remote[1] + ' PING'):
            print "Ping failed."
            return False
        Response = Kon.Recieve()
        if Response == 'BAD COMMAND':
            print str("REMOTE HOST: " + Fore.GREEN  + Remote[0] + Fore.RESET  + "     STATUS: " + Fore.GREEN + "Up" + Fore.RESET   
              + "    PING:" + Fore.RED + "Failed"  + Fore.RESET)
            return False
        if Response == 'BAD SECRET':
            print "REMOTE HOST : " + Response
            return False
        if AMODE is False:
          print str("REMOTE HOST: " + Fore.GREEN  + Remote[0] + Fore.RESET  +"     STATUS: " + Fore.GREEN + "Up" + Fore.RESET  
            + "    PING RESPONSE: " + Fore.GREEN + Response + Fore.RESET)
          return True
        else:
            return Kon
        
    


