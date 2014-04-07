import os
import sys
import Parser
import Engines


LINKS = {
    'ADDNODE':Engines.AddNode
    }



def Helper():
  print "==Help=="
  print "Commands | Use | Format - If parameters marked * are optional."
  print "help     | Print this help message "
  print "addnode  | Add new node to databse  | 'addnode <IP / Domain> <Node Secret>"
  

class Console:
        
    def Start(self):
      print "Starting console.\nEnter 'help' for help and 'exit' to exit console."
      while(1):
          Command = raw_input(">>")
          Command.strip()
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
    os.system("clear")
    print "Kronos Command Centre - Cluster Monitoring and Control Toolkit"
    print "Copyright 2014 Blaise M Crowly | Xincoz "
    print "This is a free software and comes with no warranties or guarantees to the extend permitted by law"
    print "Released under GNU GPL 3 License"
    if len(sys.argv) > 1:
        print "Parameters Passed"
    else:
        Console().Start()
