#Python script for syncing your Google Documents locally.
#Vivek Karuturi

import urllib
import os
import glob
import sys
from stat import *
import gdata.docs.service
import gdata.data
import gdata.acl.data
import gdata.docs.client
import gdata.docs.data
import gdata.sample_util

#ensure the directory exists and if not, creates it
def configdir(f):
    dir = os.path.join(os.path.expanduser('~'),f)
    if not os.path.exists(dir):
        print 'making %s'%dir
        os.makedirs(os.path.join(os.path.expanduser('~'),f))
    return dir

#app data for client
class AppConfig(object):
    APP_NAME = "GSYNC"
    DEBUG = False
    path = configdir('MyGoogleDocuments')

#creates a client after authenticating the user
def CreateClient():
    client = gdata.docs.client.DocsClient(source=AppConfig.APP_NAME)
    client.http_client.debut = AppConfig.DEBUG
    
    #auth
    try:
        gdata.sample_util.authorize_client(
            client,
            service = client.auth_service,
            source = client.source,
            scopes= client.auth_scopes
        )
    except gdata.client.BadAuthentication:
        exit('Invalid user credentials!')
    except gdata.client.Error:
        exit('Error during login!')
    return client

#Gets a list of each gdoc and when it was last changed.
def GListLastChanged(inclient):
    changes = inclient.GetChanges()
    changedgdocs = {}
    for change in changes.entry:
        changedgdocs[change.title.text]= change.changestamp.value
    return changedgdocs    

#Gets a list of each local doc and when it was last changed
def LListLastChanged():
    changedlocals = {} 
    listing = os.listdir(AppConfig.path)
    for infile in listing:
        changedlocals[infile]= os.path.getmtime(os.path.join(AppConfig.path, infile))
    return changedlocals

