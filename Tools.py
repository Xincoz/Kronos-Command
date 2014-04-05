import ping, socket


class Connection:
  Kon = ""
  
  def Comnnect(self,Link):
    Kon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Kon.connect((Link)
    sslSocket = socket.ssl(Kon)
    #print repr(sslSocket.server())
    #print repr(sslSocket.issuer())
    #sslSocket.write('Hello secure socket\n')
    #s.close()
  
  def Close(self):
    Kon.close()

  def 



class Network:
  def IsIP(self,Remote):
    try:
      socket.inet_aton(addr)
      return True
    except:
      return False

  def Ping(self,Remote):
        if not self.IsIP(Remote):
            try:
              Ip = repr(socket.gethostbyname(Remote))
            except:
              print "Could not resolve host "+Remote
              return Fasle
        else:
            Ip = Remote


