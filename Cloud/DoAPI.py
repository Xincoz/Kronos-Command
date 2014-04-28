# -*- coding: utf-8 -*-
#Kronos - 0.1 [Abstract Anion] - Alpha
#Copyright (C) 2014 Blaise M Crowly  - All rights reserved
#Created at Xincoz [xincoz.com]
#GPL v3

"""This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.)"""

"""This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details."""


####################################################################
# A simple Digital Ocean API to handle the communication           #
# with digital ocean cloud platform. It is a wrapper over the      #
# ifficial Digital Ocean Web API                                   #
####################################################################




import urllib2 #To fetch required URL
import json  #To handle incoming JSON

#Create a DoClient object with proper ClientID and API-Key Set
def makeclient(Cli,Api):
  Client = DoClient()
  Client.setauth(Cli,Api)
  return Client

#DoCleint Class
class DoClient:
  CID ="" #Client ID
  APIKEY = "" #API Key from Digital Ocean

#Set the CliID and APIkey valued 
  def setauth(self,Cli,Api):
    self.CID = Cli
    self.APIKEY = Api

#Call to get lost of droplets, also used to validate the API credentials
  def droplets(self):
    try:
      Request =  "https://api.digitalocean.com/droplets/?client_id=" + self.CID + "&api_key=" + self.APIKEY
      Response = urllib2.urlopen(Request).read()
    except Exception,e:
      return e
    return json.loads(Response.strip())
      
#Call to power on a droplet in Digital Ocean Platform
  def poweron(self,Id):
    try:
      Request = "https://api.digitalocean.com/droplets/" + Id  + "/power_on/?client_id=" + self.CID + "&api_key=" + self.APIKEY
      Response = urllib2.urlopen(Request).read()
    except Exception,e:
      print e
    return json.loads(Response.strip())


