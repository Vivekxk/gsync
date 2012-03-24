#hooks up the dropbox api to the gsync app
#Vivek Karuturi

from dropbox import client, rest, session
import webbrowser
import sys
import os

#Debug option
DEBUG = True 

#App Credentials
APP_KEY = 'gg4uctzehi3v156'
APP_SECRET = '21q3mjltwqcdoqx'
ACCESS_TYPE = 'app_folder'

#create a session
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
    
def hookItUp(sess):
    #user authentication and authorization
    request_token = sess.obtain_request_token()
    url = sess.build_authorize_url(request_token)
    webbrowser.open(url)
    print 'Press Enter after you have allowed access'
    raw_input()

    #writes the access token to a file
    file = open('access_token.dat', 'w+')
    access_token = sess.obtain_access_token(request_token)
    file.write(str(access_token))
    file.close()

client = client.DropboxClient(sess)
print 'It seems like gsync has not been hooked up to Dropbox, please take a moment to hook it up!'
hookItUp(sess)
    
accntinfo = 'linked account:', client.account_info()
print accntinfo
    
def sync(myclient=client):
    mypath = os.path.join(os.path.expanduser('~'),'MyGoogleDocuments')
    listing = os.listdir(mypath)
    for infile in listing:
        try:
            f = open(os.path.join(mypath,infile))
            dbresponse = myclient.put_file(infile, f)
            if DEBUG == True:
                print 'uploaded:', dbresponse
        except ErrorResponse:
            pass

