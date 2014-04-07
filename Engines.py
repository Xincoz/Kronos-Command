import Tools


def AddNode(Key):
  Key = (Key[0].replace("'",''),Key[1])
  Net = Tools.Network()
  if Net.Ping(Key) !=  False:
      Nodes = Tools.Nodes().GetList()
      if Key[0] in Nodes:
          print "Node already exist."
          return False
      else:
         Tools.Nodes().NodeAdd(Key)


