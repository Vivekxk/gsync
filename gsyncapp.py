#my gsync app
#Vivek Karuturi

import gdocscript
import dboxscript
from Config import conf, config_init
import os
from time import sleep
from dropbox import client, rest, session

#executes the dropbox setup
os.system('python2.7 dboxscript.py')

#creates the user's gdocs client
mydocsclient = gdocscript.CreateClient()

#setup the config
config_init()
INTERVAL = conf.getint('sync','interval')
print INTERVAL

#executes the file downloads with an interval of 3min updates
while True:
    myforeign = gdocscript.GListLastChanged(mydocsclient)
    mylocals = gdocscript.LListLastChanged()
    gdocscript.localsync(mydocsclient,mylocals, myforeign)
    dboxscript.sync()
    sleep(INTERVAL)


