#my gsync app
#Vivek Karuturi

import gdocscript
import dboxscript
import os
from time import sleep
from dropbox import client, rest, session

#executes the dropbox setup
os.system('python2.7 dboxscript.py')

dbsession = session.DropboxSession(dboxscript.APP_KEY, dboxscript.APP_SECRET, dboxscript.ACCESS_TYPE)
dbclient = client.DropboxClient(dbsession)


#creates the user's gdocs client
mydocsclient = gdocscript.CreateClient()

while True:
    myforeign = gdocscript.GListLastChanged(mydocsclient)
    mylocals = gdocscript.LListLastChanged()
    gdocscript.localsync(mydocsclient,mylocals, myforeign)
    sleep(480)


