
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
# Cloud engine contains the functions to handle comm with          #
# cloud services such as Digital Ocean and AWS                     #
####################################################################


import os
import DoAPI  as DO




def AddDOC(Commands):
#If file already exist check if duplicate entry
  if os.path.isfile('Cloud/Digitalocean.Kronos'):
      Accounts = GetDocAccounts()
      if Commands[0] in Accounts:
          print "Account name already in use"
          return False,0
      for each in Accounts:
          if Commands[1] in Accounts[each].split(':'):
            print "Account with same client ID found : " + each
            return False,0
  #Try making a request to validate the API credentials
  Cli = DO.makeclient(Commands[1],Commands[2])
  try:
    Tmp = Cli.droplets()
  except Exception,e:
   print e
  try:
    if Tmp['status'] == 'OK':
      del Cli
      File = open('Cloud/Digitalocean.Kronos','a')
      File.write(Commands[0] + '|' + Commands[1] + ':' + Commands[2])
      File.close()
    else:
        print "Validating credentials failed"
        return False,0
  except:
    print "Failed to validate details"
    return False,0

def GetDocAccounts():
  Accounts = {}
  if os.path.isfile('Cloud/Digitalocean.Kronos'):
      File = open('Cloud/Digitalocean.Kronos','r')
      for each in File:
        each = each.strip().replace('\n','').split('|')
        Accounts.update({each[0]:each[1]})
      File.close()
      return Accounts
  else:
      return Accounts

def GetCloudNodes():
  Accounts={}
  if os.path.isfile('Cloud/Digitalocean.Kronos'):
    return Accounts
  else:
    File = open('Cloud/CloudNodes.Kronos','r')
    for each in File:
        if 'DOC@' in each:
            each = each.replace('DOC@','').replace('\n','').split('|')
            Accounts.update({each[0]:each[1]})
    File.close()
    return Accounts

def AddDocNode(Vals):
  File = open('Cloud/CloudNodes.Kronos','a')
  File.write('DOC@' + Vals[0] + '|' + Vals[1] + ':' + Vals[2] + '\n')
  File.close()

def PoweOn(Vals):
  if not os.path.isfile('Cloud/CloudNodes.Kronos'):
    print "No known cloud nodes"
    return False
  DOCNodes = GetCloudNodes()
  if Vals in  DOCNodes:
    Vals = DOCNodes[Vals].split(':')
    Cloud = GetDocAccounts()
    if Vals[0] not in Cloud:
      print "DOC Account Missing"
      return False
    else:
      APICred = Cloud[Vals[0]].split(':')
      Cli = DO.makeclient(APICred[0],APICred[1])
      Response = Cli.poweron(Vals[1])
      if Response['status'] == 'OK':
        print "Startup Initiated"
  else:
     print "Node is not listed as a Digital Ocean node"
     return False
