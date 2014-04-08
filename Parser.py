

class ParseEngines:
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
    'ifup':ParseEngines().IfUp}
  
  
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
