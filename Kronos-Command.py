import os
import sys
import Parser
import Engines


LINKS = {
    'ADDNODE':Engines.AddNode,
    'IFUP':Engines.IfUp
    }



def Helper():
  print "==Help=="
  print "Commands | Use | Format - Parameters marked * are optional."
  print "----------------------------------------------------------"
  print "help     | Print this help message | 'help'"
  print "addnode  | Add new node to databse  | 'addnode <IP / Domain> <Node Secret>'"
  print "ifup     | Check if node/nodes are up by ping | 'ifup  *<IP/Domain/Coma separated Domain or IP List>"
  

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
