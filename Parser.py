

class ParseEngines:

    def KillAll(self,Command="NULL"):
      if len(Command)>2 or Command == "NULL":
          print "Malformed Command - Expecting : killass <Process Name> <Coma separated IP/Domain list>"
          return False,0
      else:
          return "KILLALL",Command

    def AddNode(self,Command):
     if len(Command) != 2:
         print "Malformed Command - Expecting  : addnode <IP / Domain> <Node Secret>"
         return False,0
     if Format().HasSpecial(Command[0]+Command[1]):
         print "Malformed Command - Contains Special Characters other than (.)"

     return "ADDNODE",Command
      
    def IfUp(self,IPs=False):
      if IPs == False:
          return "IFUP","NULL"
      Hosts = ""
      for each in IPs:
          Hosts = Hosts + each
      Hosts = Hosts.split(',')
      return "IFUP",Hosts 

    def LsProc(self,IPs=False):
      if IPs == False:
          return  "LSPROC","NULL"
      Hosts = ""
      for each in IPs:
          Hosts = Hosts + each
      Hosts = Hosts.split(',')
      return "LSPROC",Hosts

    def Kill(self,Command=False):
      if Command == False:
          print "Malformed Command - Ecpecting : kill <PID> <IP/Doman>"
          return False,0
      else:
          if len(Command) != 2:
              print "Malformed Command - Expecting : kill <PID> <IP/Domain>"
              return False,0
          else:
              return 'KILL',Command




class Format:
  def FormatThis(self,Text):
    Text = ' '.join(Text.lower().split()).split(' ')
    print Text
    return Text

  def HasSpecial(self,Text):
    if any(c in Text for c in '`~!@#$%^&*(){}[]:;\'"<>,?/'):
        return True



def Parse(Command):
  

  LINKS={
    'addnode':ParseEngines().AddNode,
    'ifup':ParseEngines().IfUp,
    'lsproc':ParseEngines().LsProc,
    'kill':ParseEngines().Kill,
    'killall':ParseEngines().KillAll}
  
  
  if len(Command) == 0:
      return False,0
  else:
      Command = Format().FormatThis(Command)
      try: 
       if len(Command) > 1:
         return LINKS[Command[0]](Command[1:])
       else:
         return LINKS[Command[0]]()
      except Exception,e:
        print e
        print "Unknown Command"
        return False,0
