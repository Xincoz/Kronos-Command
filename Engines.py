

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


##########################################################################
#  This file contains the functions that execute the required operations #
#  based on the input fromt he main program.                             #
#                                                                        #
#--------------------------IMPORTANT-------------------------------------#
#                                                                        #
# May find repeating operations and outputs that could be put into a     #
# functions and called at need but this has not been done to allow better#
# flexibility if more actions are decided to be added to independent     #
#                               functions                                #
##########################################################################

#Importing necessary modules
import Tools
from colorama import init
init()
from colorama import Fore, Back, Style
import time
import os


#Change secret function [ Recieves nodename and new secret]
def ChSecret(Commands):
  #Get list of nodes
  Nodes = Tools.Nodes().GetList()
#if given host name is not in the Nodes.Kronos file
  if Commands[0] not in Nodes:
      print "No such node"
      return False
  else:
        #update the dictionary and then write it into Nodes.Kronos
        Nodes.update({Commands[0]:Commands[1]})
        File = open('Nodes.Kronos','w')
        for each in Nodes:
          File.write(each + '|' + Nodes[each] + '\n')
        File.close()
        print "Done"


#Remove a node [ Recieves nodename]
def ChSecret(Commands):
  #Get list of nodes
  Nodes = Tools.Nodes().GetList()
#if given host name is not in the Nodes.Kronos file
  if Commands[0] not in Nodes:
      print "No such node"
      return False
  else:
        #update the dictionary and then write it into Nodes.Kronos
        Nodes.pop(Commands[0])
        File = open('Nodes.Kronos','w')
        for each in Nodes:
          File.write(each + '|' + Nodes[each] + '\n')
        File.close()
        print "Done"





#Get the machine status of the hosts [ Recieves Nothing, or the list of host]
def GetStatus(Commands):
  #load list of nodes
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  print "Fetching status of " + str(len(Nodes)) + " nodes."
  #if no host list is passed get status of all nodes ind Nodes.Kronos
  if Commands == "NULL":
      for each in Nodes:
        #Get a object for communication after checking if the node is up
        Kon = Net.Ping((each,Nodes[each]),True)
        if Kon != False:
          if not Kon.Send(Nodes[each] + " GETSTAT"):
             print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
             continue
          Response = Kon.Recieve()
          Kon.Close()
          del Kon
          if Response == "BAD COMMAND":
              print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
              continue
          print "================= HOST:" + each + " ==============="
          print Response
  else:
  #If host list is provided get status of the given hosts
      Hosts = Commands[0].split(',')
      print "Fetchig status of " + str(len(Hosts)) + " nodes."
      for each in Hosts:
          if not each in Nodes:
              print "REMOTE HOST: " + each + Fore.RED + " - No such node" + Fore.RESET
              continue
          #Get a object to communicate after checking if the node is up
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
            if not Kon.Send(Nodes[each]+ " GETSTAT"):
               print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
               continue
            Response = Kon.Recieve()
            Kon.Close()
            del Kon
            if Response == "BAD COMMAND":
              print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
              continue
            print "================= HOST:" + each + " ==============="
            print Response



#Print the list of nodes in the Nodes.Kronos file
def ListNodes(Commands):
  if not os.path.isfile('Nodes.Kronos'):
    print "No nodes found"
    return False
  else:
      Nodes = Tools.Nodes().GetList()
      if len(Nodes) == 0:
        print "No nodes found"
        return False
      for each in Nodes:
          print each
      return True

#Send the SETDNS request to the hosts [ Recieves DNS list and Hosts name]
def SetDNS(Commands):
  #Load list of nodes
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  if len(Commands) == 1:
#If no host list is given all nodes are used
    for each in Nodes:
        Kon = Net.Ping((each,Nodes[each]),True)
        if Kon != False:
          if not Kon.Send(Nodes[each] + " SETDNS " + Commands[0]):
             print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
             continue
          Response = Kon.Recieve()
          Kon.Close()
          del Kon
          if Response == "BAD COMMAND":
              print Response

              print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
              continue
          if Response == "Done":
              Color = Fore.GREEN
          else:
              Color = Fore.RED
          print "REMOTE HOST: " + each + Color + " " + Response + Fore.RESET
  else:
      #If host list is provided use it
      Hosts = Commands[1].split(',')
      for each in Hosts:
          if each not in Nodes:
              print "REMOTE HOST: " + each + Fore.RED + " - No such node" + Fore.RESET
              continue
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
            if not Kon.Send(Nodes[each] + " SETDNS " + Commands[0]):
              print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
              continue
          Response = Kon.Recieve()
          Kon.Close()
          del Kon
          if Response == "BAD COMMAND":
              print Response

              print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
              continue
          if Response == "Done":
              Color = Fore.GREEN
          else:
              Color = Fore.RED
          print "REMOTE HOST: " + each + Color + " " + Response + Fore.RESET

#Start/stop/restart a service
def Service(Commands):
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  print Commands
  if Commands[0] == 'STASERV':
      print "Starting " + Commands[1],
  if Commands[0] == 'STOSERV':
      print "Stopping " + Commands[1],
  if Commands[0] == 'RESSERV':
      print "Restarting " + Commands[1],
  if len(Commands) == 2:
    print " on " + str(len(Nodes)) + " nodes."
    for each in Nodes:
      Kon = Net.Ping((each,Nodes[each]),True)
      if Kon != False:
         if not Kon.Send(Nodes[each]+ " " + Commands[0] + " " + Commands[1]):
             print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
             continue
         Response = Kon.Recieve()
         Kon.Close()
         del Kon
         if Response == "BAD COMMAND":
             print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
             continue
         if Response == "BAD SECRET":
             print "REMOTE HOST: " + each + Fore.RED + " - BAD SECRET" + Fore.RESET
             continuei

         if Response == "Executed":
            Color = Fore.GREEN
         else:
            Color = Fore.RED

         print "REMOTE HOST: " + each + Color + " " + Response + Fore.RESET
  else:
      Hosts = Commands[2].split(',')
      for each in Hosts:
          if each not in Nodes:
              print "REMOTE HOST: " + each + Fore.RED + " No such node" + Fore.RESET
              continue
          
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
            if not Kon.Send(Nodes[each]+ " " + Commands[0] + " " + Commands[1]):
                print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                continue
            Response = Kon.Recieve()
            Kon.Close()
            del Kon
            if Response == "BAD COMMAND":
              print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
              continue
            if Response == "BAD SECRET":
                 print "REMOTE HOST: " + each + Fore.RED + " - BAD SECRET" + Fore.RESET
                 continue
            if Response == "Executed":
              Color = Fore.GREEN
            else:
              Color = Fore.RED

            print "REMOTE HOST: " + each + Color + " " + Response + Fore.RESET

      

#Run a command on the server
def Run(Commands):
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  if len(Commands) == 1:
      print "Running command on " + str(len(Nodes)) + " nodes."
      for each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
            if not Kon.Send(Nodes[each] + "  EXECUT"):
                print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                continue
            Response = Kon.Recieve()
            print Response
            if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
            else:
                  if not Kon.Send(Commands[0]):
                    print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                    continue
                  Response = Kon.Recieve()
                  Kon.Close()
                  del Kon
                  print "REMOTE HOST: " + each + Fore.GREEN + " " + Response + Fore.RESET

  else:
      Hosts = Commands[0].split(',')
      for each in Hosts:
          if each not in Nodes:
              print "REMOTE HOST: " + each + Fore.RED + "- No such node." + Fore.RESET
              continue
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
            if not Kon.Send(Nodes[each] + "  EXECUT"):
                print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                continue
            Response = Kon.Recieve()
            print Response
            if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
            else:
                  if not Kon.Send(Commands[1]):
                    print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                    continue
                  Response = Kon.Recieve()
                  Kon.Close()
                  del Kon
                  print "REMOTE HOST: " + each + Fore.GREEN + " " + Response + Fore.RESET

#Rebooot the hosts
def ReBoot(Hosts):
 Nodes = Tools.Nodes().GetList()
 Net = Tools.Network()
 if Hosts == 'NULL':
     print "Reebooting " + str(len(Nodes)) + " nodes." 
     for each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
              if not Kon.Send(Nodes[each] + " REBOOT"):
                  print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                  continue
              Response = Kon.Recieve()
              Kon.Close()
              del Kon
              if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
              print "REMOTE HOST: " + each + " " + Fore.GREEN + Response + Fore.RESET
 else:
     Hosts = Hosts[0].split(',')
     for each in Hosts:
         if each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
              if not Kon.Send(Nodes[each] + " REBOOT"):
                  print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                  continue
              Response = Kon.Recieve()
              Kon.Close()
              del Kon
              if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
              print "REMOTE HOST: " + each + " " + Fore.GREEN + Response + Fore.RESET
         else:
          print "REMOTE HOST: " + each + Fore.RED + " - No such node" + Fore.RESET 



#Poweroff the hosts
def PowerOff(Hosts):
 Nodes = Tools.Nodes().GetList()
 Net = Tools.Network()
 if Hosts == 'NULL':
     print "Reebooting " + str(len(Nodes)) + " nodes." 
     for each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
              if not Kon.Send(Nodes[each] + " PWROFF"):
                  print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                  continue
              Response = Kon.Recieve()
              Kon.Close()
              del Kon
              if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
              print "REMOTE HOST: " + each + " " + Fore.GREEN + Response + Fore.RESET
 else:
     Hosts = Hosts[0].split(',')
     for each in Hosts:
         if each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
              if not Kon.Send(Nodes[each] + " PWROFF"):
                  print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                  continue
              Response = Kon.Recieve()
              Kon.Close()
              del Kon
              if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
              print "REMOTE HOST: " + each + " " + Fore.GREEN + Response + Fore.RESET
         else:
          print "REMOTE HOST: " + each + Fore.RED + " - No such node" + Fore.RESET 





#Add a new node to Nodes.Kronos
def AddNode(Key):
  Key = (Key[0].replace("'",''),Key[1])
  Net = Tools.Network()
  Nodes = Tools.Nodes().GetList()
  if Key[0] in Nodes:
      print "Node already exist."
      return False
  if Net.Ping(Key) !=  False:
      Tools.Nodes().NodeAdd(Key)
  else:
      return False

#List processes on hosts
def LsProc(Hosts):
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  if  Hosts == "NULL":
      print "Listing processes on " + str(len(Nodes)) + " nodes."
      for each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
              if not Kon.Send(Nodes[each] + " LISPS"):
                  print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                  continue
              Response = Kon.Recieve()
              Kon.Close()
              del Kon
              if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
              if Response == "BAD SECRET":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD SECRET" + Fore.RESET
              print "=============== HOST: " + each + " ==============="
              print Response
  else:
      print "Listing processes on " + str(len(Hosts)) + " nodes."
      for each in Hosts:
          if each not in Nodes:
              print "REMOTE HOST: " + each + Fore.RED + " - No such node" + Fore.RESET 
              continue
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon != False:
              if not Kon.Send(Nodes[each] + " LISPS"):
                print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
                return False
              Response = Kon.Recieve()
              Kon.Close()
              del Kon
              if Response == "BAD COMMAND":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD COMMAND" + Fore.RESET
                  continue
              if Response == "BAD SECRET":
                  print "REMOTE HOST: " + each + Fore.RED + " - BAD SECRET" + Fore.RESET
              print "=============== HOST: " + each + " ==============="
              print Response
          else:
              print "REMOTE HOST: " + each + Fore.RED + " Failed" + Fore.RESET
              return False
#Kill a process on host
def Kill(Commands):
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  if Commands[1] not in Nodes:
      print "REMOTE HOST: " + Commands[1] + Fore.RED + " - No such node." + Fore.RESET
      return False
  else:
      Kon = Net.Ping((Commands[1],Nodes[Commands[1]]),True)
      if Kon != False:
          if not Kon.Send(Nodes[Commands[1]] + " KILLPID " + Commands[0]):
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " Failed" + Fore.RESET
            return False
          Response = Kon.Recieve()
          Kon.Close()
          del Kon
          if Response == "BAD COMMAND":
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " - BAD COMMAND" + Fore.RESET
            return False
          if Response == "BAD SECRET":
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " - BAD COMMAND" + Fore.RESET
            return False
          if Response == 'Killed':
              Color = Fore.GREEN
          else:
              Color = Fore.RED

          print Color + Response + Fore.RESET
          return True
      else:
        print "REMOTE HOST: " + Commands[1] + Fore.RED + " Failed" + Fore.RESET
        return False

#Kill all instances of a process on a host
def KillAll(Commands):
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  if len(Commands)== 1:
      print "Killing " + Commands[0] + " in " + str(len(Nodes)) + " nodes."
      for each in Nodes:
          Kon = Net.Ping((each,Nodes[each]),True)
          if Kon == False:
              continue
          if not Kon.Send(Nodes[each] + " KILLPS " + Commands[0]):
            print "REMOTE HOST: " + each + Fore.RED + " - Failed" + Fore.RESET
            continue
          Response = Kon.Recieve()
          Kon.Close()
          del Kon
          if Response == "BAD COMMAND":
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " - BAD COMMAND" + Fore.RESET
            continue
          if Response == "BAD SECRET":
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " - BAD COMMAND" + Fore.RESET
            continue
          if Response == 'Killed':
              Color = Fore.GREEN
          else:
              Color = Fore.RED

          print "REMOTE HOST: " + each + " " + Color + Response + Fore.RESET
      return True
  else:
      List = Commands[1].split(',')
      print "Killing " + Commands[0] + " in " + str(len(List)) + " nodes."
      for each in List:
          if each not in Nodes:
              print "REMOTE HOST: " + each + Fore.RED + " - no such node" + Fore.RESET 
              continue
          else:
              Kon = Net.Ping((each,Nodes[each]),True)

          if Kon == False:
              continue
          if not Kon.Send(Nodes[each] + " KILLPS " + Commands[0]):
            print "REMOTE HOST: " + each + Fore.RED + " - Failed" + Fore.RESET
            continue
          Response = Kon.Recieve()
          Kon.Close()
          del Kon
          if Response == "BAD COMMAND":
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " - BAD COMMAND" + Fore.RESET
            continue
          if Response == "BAD SECRET":
            print "REMOTE HOST: " + Commands[1] + Fore.RED + " - BAD COMMAND" + Fore.RESET
            continue
          if Response == 'Killed':
              Color = Fore.GREEN
          else:
              Color = Fore.RED
          print "REMOTE HOST: " + each + " " + Color + Response + Fore.RESET
      return True


#Check if a host is up
def IfUp(Hosts):
  Nodes = Tools.Nodes().GetList()
  Net = Tools.Network()
  if Hosts == "NULL":
      print "Pinging " + str(len(Nodes)) + " nodes."
      for each in Nodes:
          Net.Ping((each,Nodes[each]))
  else:
      print "Pinging " + str(len(Hosts)) + " nodes."
      for each in Hosts:
          if each in Nodes:
              Net.Ping((each,Nodes[each]))
          else:
              print "REMOTE HOST: " + Fore.RED + each +  " - No such node." + Fore.RESET
