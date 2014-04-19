
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
  if os.path.isfile('Digitalocean.Kronos'):
      File = open('Digitalocean.Kronos','r')
      Accounts = {}
      for each in File:
        each = each.strip().replace('\n').split('|')
        Accounts.update({each[0]:each[1]})
      File.close()
      if Commands[0] in Accounts:
          print "Account name already used"
          return False,0
      for each in Accounts:
          if Commands[1] in Accounts[each].split(':'):
            print "Account with same client IS found : " + each
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
      File = open('Digitalocean.Kronos','a')
      File.write(Commands[0] + '|' + Commands[1] + ':' + Commands[2])
      File.close()
    else:
        print "Validating credentials failed"
        return False,0
  except:
    print "Failed to validate details"
    return False,0

