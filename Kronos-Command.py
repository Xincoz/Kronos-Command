
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

###################################################################
# This is the main program which starts the console or processes  #
# the arguments coming from the terminal.                         #
###################################################################



#Importing necessary modules
import os
import sys
import Parser
import Engines
#Import and initialize color on terminal
from colorama import init
init()
from colorama import Fore


#Link dictionary to link input commands to Operations
LINKS = {
    'ADDNODE':Engines.AddNode,
    'IFUP':Engines.IfUp,
    'LSPROC':Engines.LsProc,
    'KILL':Engines.Kill,
    'KILLALL':Engines.KillAll,
    'REBOOT':Engines.ReBoot,
    'PWROFF':Engines.PowerOff,
    'RUN':Engines.Run,
    'SERV':Engines.Service,
    'LSNODES':Engines.ListNodes,
    'STATUS':Engines.GetStatus,
    'SETDNS':Engines.SetDNS,
    'CHSECRET':Engines.ChSecret,
    'RMNODE':Engines.RmNode,
    'ISRUNING':Engines.IsRunning,
    }

#Help message
def Helper():
  print "==Help=="
  print "Commands | Use                                         | Format "  
  print "-----------------------------------------------------------------------------------------------------------------"
  print "help     | Print this help message                     | 'help'"
  print "addnode  | Add new node to database                    | 'addnode <IP / Domain> <Node Secret>'"
  print "rmnode   | Remove a node from database                 | 'rmnode <IP/Domain>'"
  print "lsnodes  | List all nodes                              | 'lsnodes'"
  print "chsecret | Change secret of a node                     | 'chsecret <Node>  <New secret>'"
  print "ifup     | Check if node/nodes are up by ping          | 'ifup  *<IP/Domain/Coma separated Domain or IP List>'"
  print "status   | Get machine status data of the node         | 'status *<Coma separated IP/Domain list>'"
  print "setdns   | Set the DNS server for the node             | 'setdns <Coma separated DNS server list> *<coma separated IP/Domain list>'"
  print "lsproc   | List Name and PID of all processes running  | 'lsproc *<Coma separater IP/Domain list>'"
  print "running  | Check if a process is running               | 'running <Process name> *<Coma separated IP / Domains>'"
  print "kill     | Kill a process by it's PID on a given host  | 'kill <PID> <IP/Domain of host>'"
  print "killall  | Kill all processes by name on  nodes        | 'killall <Process Name> *<Coma separated IP/Domain>'"
  print "reboot   | Reboot all or few of the nodes              | 'reboot  *<Coma separated IP/Domain list>'  (add --yes to avoid prompt)"
  print "poweroff | Shutdown all or few of the nodes            | 'poweroff *<Coma separated IP/Domain list>' (add --yes to avoid prompt)"
  print "run      | Run a shell command in the node             | 'run  *<Coma separated IP/Domain list> -c <Command>'"
  print "start    | Start a service                             | 'start <Service Name> *<Coma separated IP/Domain list>"
  print "stop     | Stop a service                              | 'stop <Service Name>  *<Coma separated IP/Domain list>"
  print "restart  | Restart a service                           | 'restart  <Service Name> *<Coma separated IP/Domain list>"
  print "exit     | Exit from console                           | 'exit'"
  print Fore.GREEN + "Note: Parameters marked * are optional" + Fore.RESET
  print Fore.RED + "Warning! 'poweroff' command do not have a reverse option available, you will need to start the nodes back manually" + Fore.RESET
  print "\n"

#Console class that controls the consoles
class Console:
        
    def Start(self):
      print "Starting console.\nEnter 'help' for help and 'exit' to exit console."
      #Infinite loop for console 
      while(1):
          Command = raw_input(">>")
          Command = Command.strip()
          #Exit
          if Command == 'exit':
              print "Exiting.."
              exit()
          else:
              #Help 
              if Command == 'help':
                Helper()
              else:
                #Parses the input commands and returns a state (LINK dictionary key) and arguments
                State,Command = Parser.Parse(Command)
                try:
                  #Invoke LINK function 
                  LINKS[State](Command)
                except:
                  continue 

#Main startup
if __name__ == '__main__':
    
    #If commands are passed as arguments from the terminal
    if len(sys.argv) > 1:
      Arguments = ""
      #Convert the arguments into a single long string
      for each in sys.argv[1:]:
          #Replace any ' ' with '\ ' to keep integrity of input in case of run command containing
          #strings with ' ' or paths with ' '
          eachch .replace(' ','\ ')
          Arguments = Arguments + " " + each
      Arguments = Arguments.strip()
      #Print help message if 'help'
      if Arguments == 'help':
          Helper()
          exit()
      #Pass string for parsing
      State,Command = Parser.Parse(Arguments)
      try:
       LINKS[State](Command)
      except:
        exit(121)
      exit()
    else:  
      #Startup the console if no arguments are passed from terminal
      os.system("clear")
      print "Kronos Command Center - Cluster Monitoring and Control"
      print "Copyright 2014 Blaise M Crowly | Xincoz "
      
      print "This program is distributed in the hope that it will be useful,"
      print "but WITHOUT ANY WARRANTY; without even the implied warranty of"
      print "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
      print "GNU General Public License for more details."
      
      print "Released under GNU GPL v3.0 License\n"
      #Console start
      Console().Start()
