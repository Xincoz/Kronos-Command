import os
import sys
import Parser
import Engines

from colorama import init
init()
from colorama import Fore

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
    'SETDNS':Engines.SetDNS}


def Helper():
  print "==Help=="
  print "Commands | Use                                         | Format "  
  print "-----------------------------------------------------------------------------------------------------------------"
  print "help     | Print this help message                     | 'help'"
  print "addnode  | Add new node to databse                     | 'addnode <IP / Domain> <Node Secret>'"
  print "lsnodes  | List all nodes                              | 'lsnodes'"
  print "ifup     | Check if node/nodes are up by ping          | 'ifup  *<IP/Domain/Coma separated Domain or IP List>'"
  print "status   | Get machine status data of the node         | 'status *<Coma separated IP/Domain list>'"
  print "setdns   | Set the DNS server for the node             | 'setdns <Coma separated DNS server list> *<coma separated IP/Domain list>'"
  print "lsproc   | List Name and PID of all processes running  | 'lsproc *<Coma separater IP/Domain list>'"
  print "kill     | Kill a process by it's PID on a given host  | 'kill <PID> <IP/Domain of host>'"
  print "killall  | Kill all processes by name on  nodes        | 'killall <Process Name> *<Coma separated IP/Domain>'"
  print "reboot   | Reboot all or few of the nodes              | 'reboot  *<Coma separated IP/Domain list>'  (add --yes to avoid prompt)"
  print "poweroff | Shutdown all or few of the nodes            | 'poweroff *<Coma separated IP/Domain list>' (add --yes to avoid prompt)"
  print "run      | Run a shell command in the node             | 'run  *<Coma separated IP/Domain list>"
  print "start    | Start a service                             | 'start <Service Name> *<Coma separated IP/Domain list>"
  print "stop     | Stop a service                              | 'stop <Service Name>  *<Coma separated IP/Domain list>"
  print "restart  | Restart a service                           | 'restart  <Service Name> *<Coma separated IP/Domain list>"
  print "exit     | Exit from console                           | 'exit'"
  print Fore.GREEN + "Note: Parameters marked * are optional" + Fore.RESET
  print Fore.RED + "Warning! 'poweroff' command do not have a reverse option available, you will need to start the nodes back manually" + Fore.RESET
  print "\n"
class Console:
        
    def Start(self):
      print "Starting console.\nEnter 'help' for help and 'exit' to exit console."
      while(1):
          Command = raw_input(">>")
          Command = Command.strip()
          if Command == 'exit':
              print "Exiting.."
              exit()
          else:
              if Command == 'help':
                Helper()
              else:
                State,Command = Parser.Parse(Command)
                print State,Command
                try:
                  LINKS[State](Command)
                except:
                  continue 


if __name__ == '__main__':
    if len(sys.argv) > 1:
      Arguments = ""
      for each in sys.argv[1:]:
          Arguments = Arguments + " " + each
      Arguments = Arguments.strip()
      State,Command = Parser.Parse(Arguments)
      try:
       LINKS[State](Command)
      except:
        exit(121)
      exit()
    else:  
      os.system("clear")
      print "Kronos Command Centre - Cluster Monitoring and Control Toolkit"
      print "Copyright 2014 Blaise M Crowly | Xincoz "
      print "This is a free software and comes with no warranties or guarantees to the extend permitted by law"
      print "Released under GNU GPL 3 License"
      Console().Start()
