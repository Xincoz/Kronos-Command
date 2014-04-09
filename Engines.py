import Tools
from colorama import init
init()
from colorama import Fore, Back, Style
import time



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
