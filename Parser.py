

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

    def Reboot(self,Command=False):
      if Command == False:
          print "Are you sure you want to reboot the entire cluster (yes/no)) :",
          if raw_input() == 'yes':
              return 'REBOOT',"NULL"
          else:
              return False,0
      else:
          if len(Command) > 2:
            print "Malformed Command - Expecting : reboot *--yes <Coma separated IP/Domain list>"
            return False,0
          if '--yes' not in Command:
            print "Are you sure you want to reboot the entire cluster (yes/no)) :",
            if raw_input() == 'yes':
                return 'REBOOT',Command
            else:
                return False,0
          else:
              if len(Command)!=1:
                Command.remove('--yes')
                return 'REBOOT',Command
              else:
                  return 'REBOOT','NULL'



    def PowerOff(self,Command=False):
      if Command == False:
          print "Are you sure you want to shutdown the entire cluster (yes/no) :",
          if raw_input() == 'yes':
              return 'PWROFF',"NULL"
          else:
              return False,0
      else:
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
              if len(Command)!=1:
                Command.remove('--yes')
                return 'PWROFF',Command
              else:
                  return 'PWROFF','NULL'

    def Run(self,Command=False):
       if Command!=False:
        if len(Command) > 1:
          print "Malformed Command  - Expecting : run <Coma separated IP/Domain list>"
          return False,0
       Code = raw_input("Command >>")
       if Command == False:
          return 'RUN',[Code]
       else:
          return 'RUN',[Command[0],Code]
      
    def ServeStart(self,Command=False):
      if Command == False:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) > 3:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) == 1:
          return 'SERV',['STASERV',Command[0]]
      else:
          return 'SERV',['STASERV',Command[0],Command[1]]


    def ServeStop(self,Command=False):
      if Command == False:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) > 3:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) == 1:
          return 'SERV',['STOSERV',Command[0]]
      else:
          return 'SERV',['STOSERV',Command[0],Command[1]]


    def ServeRestart(self,Command=False):
      if Command == False:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) > 3:
          print "Malformed Command - Expecting : start/stop/restart <Service Name> <Coma separated IP/Domain list>"
          return False,0
      if len(Command) == 1:
          return 'SERV',['RESSERV',Command[0]]
      else:
          return 'SERV',['RESSERV',Command[0],Command[1]]


    def ListNodes(self,Command=False):
        return "LSNODES","NULL"

    def GetStatus(self,Command=False):
      if Command == False:
          return "STATUS","NULL"
      if len(Command)>1:
          print "Malformed Command - Expecting : status *<Comaseparated IP/Domain list>"
          return False,0
      return "STATUS",Command


    def SetDNS(self,Command=False):
      if Command == False:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<somaseparated IP/Domain list>"
          return False,0
      if len(Command) > 2:
          print "Malformed Command - Expecting : setdns <Comaseparated DNS server list> *<somaseparated IP/Domain list>"
          return False,0

      return "SETDNS",Command


class Format:
  def FormatThis(self,Text):
    Text = ' '.join(Text.split()).split(' ')
    Text[0] = Text[0].lower()
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
    'killall':ParseEngines().KillAll,
    'reboot':ParseEngines().Reboot,
    'poweroff':ParseEngines().PowerOff,
    'run':ParseEngines().Run,
    'start':ParseEngines().ServeStart, 
    'stop':ParseEngines().ServeStop,
    'restart':ParseEngines().ServeRestart,
    'lsnodes':ParseEngines().ListNodes,
    'status':ParseEngines().GetStatus,
    'setdns':ParseEngines().SetDNS}
  
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
