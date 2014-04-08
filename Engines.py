import Tools


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


