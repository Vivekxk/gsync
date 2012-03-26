#my gsync app
#Vivek Karuturi

import gdocscript
import dboxscript
from Config import conf as settings
import os
from time import sleep
from dropbox import client, rest, session

#executes the dropbox setup
os.system('python2.7 dboxscript.py')

#creates the user's gdocs client
mydocsclient = gdocscript.CreateClient()

#setup the config


#executes the file downloads with an interval of 3min updates
while True:
    myforeign = gdocscript.GListLastChanged(mydocsclient)
    mylocals = gdocscript.LListLastChanged()
    gdocscript.localsync(mydocsclient,mylocals, myforeign)
    dboxscript.sync()
    sleep(settings.getint('sync','time'))


