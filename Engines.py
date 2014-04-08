import Tools
from colorama import init
init()
from colorama import Fore, Back, Style

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
