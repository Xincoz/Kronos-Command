import ping, socket
from colorama import init
init()
from colorama import Fore, Back, Style
import os

class Nodes:
  def GetList(self):
    if not os.path.isfile('Nodes.Kronos'):
        return {}
    else:
        Nodelist = {}
        NodeFile = open('Nodes.Kronos','r')
        for line in NodeFile:
            line = line.split('|')
            Nodes = Nodelist + {line[0]:Nodes[1]}
        NodeFile.close()
        return Nodelist

  def NodeAdd(self,Remote):
    try:
      NodesFile = open('Nodes.Kronos','a')
    except:
      print "Could not open nodes file"
      return False
    NodesFile.write(Recieve[0]+'|'+Recieve[1])
    NodesFile.close()
    print "Added"
    return True






class Connection:
  Kon = ""
  SSLx = ""
  def Close(self):
    try:
      self.Kon.close()
      return True
    except:
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
  




class Network:
  def IsIP(self,Remote):
    try:
      socket.inet_aton(addr)
      return True
    except:
      return False

  def Ping(self,Remote):
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
            print Response
            return False
        print str("REMOTE HOST: " + Fore.GREEN  + Remote[0] + Fore.RESET  +"     STATUS: " + Fore.GREEN + "Up" + Fore.RESET  
          + "    PING RESPONSE: " + Fore.GREEN + Response + Fore.RESET)
        return True
        
    


