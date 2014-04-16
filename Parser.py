
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


########################################################################
# This file contains the functions designed to parse format and return #
# the input command as proper parameters and state flags to the main   #
# program so that it can be passed to the right operation function     #
########################################################################

#ParseEngine class contains all the function that are induvidually designed to accept
#the input string and process it as per the requirement of the specific command
class ParseEngines:

    #Parse input for the killall command
    def KillAll(self,Command="NULL"):
      #The input must have atmost the name of process and list of hosts. Nothing more.
      if len(Command)>2 or Command == "NULL":
          print "Malformed Command - Expecting : killass <Process Name> <Coma separated IP/Domain list>"
          return False,0
      else:
          return "KILLALL",Command


    #Parse input for an addnode command
    def AddNode(self,Command):
     #Strictly must have only two factors, the name of node and secret
     if len(Command) != 2:
         print "Malformed Command - Expecting  : addnode <IP / Domain> <Node Secret>"
         return False,0
     return "ADDNODE",Command
     

    #Parse the ifup command input 
    def IfUp(self,IPs=False):
      #If list of hosts are NOT passed
      if IPs == False:
          return "IFUP","NULL"
      #If list of hosts are passed
      Hosts = ""
      for each in IPs:
          Hosts = Hosts + each
      Hosts = Hosts.split(',')
      return "IFUP",Hosts 


    #Parses the lsproc command
    def LsProc(self,IPs=False):
      #If list of hosts are not passed
      if IPs == False:
          return  "LSPROC","NULL"
      #If list of hosts are passed
      Hosts = ""
      for each in IPs:
          Hosts = Hosts + each
      Hosts = Hosts.split(',')
      return "LSPROC",Hosts
    
    #Pase the kill command
    def Kill(self,Command=False):
      #A PID and host has to be passed without fail
      if Command == False:
          print "Malformed Command - Ecpecting : kill <PID> <IP/Doman>"
          return False,0
      else:
          #Must have two arguments, the PID and the host
          if len(Command) != 2:
              print "Malformed Command - Expecting : kill <PID> <IP/Domain>"
              return False,0
          else:
              return 'KILL',Command


    #Parse the reboot command
    def Reboot(self,Command=False):
      #If no hosts are passed
      if Command == False:
          #If a --yes flag is not provided make sure that the user means what is beign asked
          print "Are you sure you want to reboot the entire cluster (yes/no) :",
          if raw_input() == 'yes':
              return 'REBOOT',"NULL"
          else:
              return False,0
      else:
          #There can only be  --yes flag and list of hosts
          if len(Command) > 2:
            print "Malformed Command - Expecting : reboot *--yes <Coma separated IP/Domain list>"
            return False,0
          if '--yes' not in Command:
            print "Are you sure you want to reboot the hosts (yes/no) :",
            if raw_input() == 'yes':
                return 'REBOOT',Command
            else:
                return False,0
          else:
              #remove the --yes as it's no longer required
              if len(Command)!=1:
                Command.remove('--yes')
                return 'REBOOT',Command
              else:
                  return 'REBOOT','NULL'


    #parse the poweroff command
    def PowerOff(self,Command=False):
      #If no hosts list is passed
      if Command == False:
          #confirm the users request if no --yes is provided
          print "Are you sure you want to shutdown the entire cluster (yes/no) :",
          if raw_input() == 'yes':
              return 'PWROFF',"NULL"
          else:
              return False,0
      else:
          #Must only have a maximum of 2 arguments, --yes and the hosts list
          if len(Command) > 2:
            print "Malformed Command - Expecting : reboot *--yes <Coma separated IP/Domain list>"
            return False,0
          if '--yes' not in Command:
            print "Are you sure you want to reboot the nodes in cluster (yes/no) :",
            if raw_input() == 'yes':
                return 'PWROFF',Command
            else:
                return False,0
          else:
              # --yes is removed as use is over
              if len(Command)!=1:
                Command.remove('--yes')
                return 'PWROFF',Command
              else:
                  return 'PWROFF','NULL'


    #Run Command - Must check and return host names if provided and the proper string command
    def Run(self,Command=False):
       if Command==False:
          print "Malformed Command  - Expecting : run *<Coma separated IP/Domain list> -c <Command>"
          return False,0
       if Command[0]=='-c':
            if len(Command) <= 1:
               print "Malforme Command - Expecting : run *<Coma separated IP/Domain list> -c <Command>"
               return False,0
            #If no hosts list is provided
            Arg = ""
            #Concatinate the entire string after the -c flag separated by ' '
            for each in Command[1:]:
                Arg = Arg + " " + each
            #Return RUN flag and the Command 
            return "RUN",[Arg]
       else:
           if len(Command) > 1 and  Command [1] == '-c':
            if len(Command) <= 2:
               print "Malforme Command - Expecting : run *<Coma separated IP/Domain list> -c <Command>"
               return False,0
             #If hosts list is provided
            Arg = ""
            #Concatinate the entire string after the -c flag separated by ' '
            for each in Command[2:]:
                Arg = Arg + " " + each
            #Return RUN flag , host list and the Command 
            return "RUN",[Command[0],Arg]

           else:
              print "Malformed Command  - Expecting : run *<Coma separated IP/Domain list> -c <Command>"
              return False,0
    
    
    
    
    #Parse the start command that starts a service
    def ServeStart(self,Command=False):
      #Must have service name
      if Command == False:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      #Can have atmost the service name and hosts list
      if len(Command) > 3:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) == 1:
          return 'SERV',['STASERV',Command[0]]
      else:
          return 'SERV',['STASERV',Command[0],Command[1]]

    #Parses the stop command that stops a service
    def ServeStop(self,Command=False):
      #Must have atleast the process name
      if Command == False:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) > 3:
          #Can atmost have the service name and list of hosts
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) == 1:
          return 'SERV',['STOSERV',Command[0]]
      else:
          return 'SERV',['STOSERV',Command[0],Command[1]]

    #Parses the restart command to restart a process
    def ServeRestart(self,Command=False):
      #Need atleast the process name
      if Command == False:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      #Can have atmost the service name and the hosts list
      if len(Command) > 3:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) == 1:
          return 'SERV',['RESSERV',Command[0]]
      else:
          return 'SERV',['RESSERV',Command[0],Command[1]]

    #Parse the command to list the nodes in the Nodes.Kronos file
    def ListNodes(self,Command=False):
        return "LSNODES","NULL"
    #Parse the getstatus command
    def GetStatus(self,Command=False):
      #If no hosts are passed
      if Command == False:
          return "STATUS","NULL"
      #Can only have atmost the list of hosts
      if len(Command)>1:
          print "Malformed Command - Expecting : status *<Comaseparated IP/Domain list>"
          return False,0
      return "STATUS",Command

    #Parse the setdns command 
    def SetDNS(self,Command=False):
      #must have atleast the DNS server list
      if Command == False:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<somaseparated IP/Domain list>"
          return False,0
      #Can atmost have the DNS server list and the 
      if len(Command) > 2:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<somaseparated IP/Domain list>"
          return False,0

      return "SETDNS",Command

    #Parse the change secret command
    def ChSecret(self,Command=False):
      #Must have the nodename and secret
      if Command == False:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<somaseparated IP/Domain list>"
          return False,0
      #Must have the nodename and new secret strictly
      if len(Command) != 2:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<somaseparated IP/Domain list>"
          return False,0
      return 'CHSECRET',Command


    #Parse the remove node command
    def RmNode(self,Command=False):
      #Must have the nodename
      if Command == False:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<Comaseparated IP/Domain list>"
          return False,0
      #Must have the nodename only
      if len(Command) != 1:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<Comaseparated IP/Domain list>"
          return False,0
      return 'RMNODE',Command

    #Parses the running comand that checks if a said process is running
    def IsRunning(self,Command=False):
      #Must have name of the process
      if Command == False:
          print "Malformed Command - Expecting : running <Process Name> *<Coma separated IP/Domain list>"
          return False,0
      if len(Command) > 2:
          print "Malformed Command - Expecting : running <Process Name> *<Coma separated IP/Domain list>"
          return False,0
      return 'ISRUNING',Command


#Class to format the incoming list and split 
class Format:
  def FormatThis(self,Text):
    Text = ' '.join(Text.split()).split(' ')
    Text[0] = Text[0].lower()
    return Text


#Main parse command
def Parse(Command):
  
#parse LINK dictionary to link command to the right ParseEngine function
  LINKS={
    'addnode':ParseEngines().AddNode,
    'ifup':ParseEngines().IfUp,
    'lsproc':ParseEngines().LsProc,
    'kill':ParseEngines().Kill,
    'killall':ParseEngines().KillAll,
    'reboot':ParseEngines().Reboot,
    'poweroff':ParseEngines().PowerOff,
    'run':ParseEngines().Run,
    'start':ParseEngines().ServeStart, 
    'stop':ParseEngines().ServeStop,
    'restart':ParseEngines().ServeRestart,
    'lsnodes':ParseEngines().ListNodes,
    'status':ParseEngines().GetStatus,
    'setdns':ParseEngines().SetDNS,
    'chsecret':ParseEngines().ChSecret,
    'rmnode':ParseEngines().RmNode,
    'running':ParseEngines().IsRunning}


#If no command is given just exit
  if len(Command) == 0:
      return False,0
  else:
#Format the incoming text
      Command = Format().FormatThis(Command)
      try: 
#if arguments are passed
       if len(Command) > 1:
         return LINKS[Command[0]](Command[1:])
       else:
#If no arguments are passed
         return LINKS[Command[0]]()
      except Exception,e:
        print e
        print "Unknown Command"
        return False,0
