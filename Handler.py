

class ParseEngines:
    def AddNode(self,Command):
     if len(Command) != 2:
         print "Malformed Command - Expecting  : addnode <IP / Domain> <Node Secret>"
         return False,0
     if Format.HasSpecial(Command[0]+Command[1]):
         print "Malformed Command - Contains Special Characters other than (.)"

     



class Format:
  def FormatThis(Self,Text):
    Text = ' '.join(Text.lower().split()).split(' ')

  def HasSpecial(self,Text):
    if any(c in text for c in '`~!@#$%^&*(){}[]:;\'"<>,?/'):
        return True



def Parse(Command):
  

  LINKS={
    'addnode':ParseEngines().AddNode}
  if len(Command) == 0:
      return False,0
  else:
      Command = Format.FormatThis(Command)
      try:
        return LINKS[Command[0]](Command[1:])
      except:
        print "Unknown Command"
