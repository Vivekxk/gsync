#hooks up the dropbox api to the gsync app
#Vivek Karuturi

from dropbox import client, rest, session
import webbrowser
import sys

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


try:
    file = open('access_token.dat', 'r')
    accesstkn = file.readline()
    client = client.DropboxClient(sess)
except IOError as e:
    print 'It seems like gsync has not been hooked up to Dropbox, please take a moment to hook it up!'
    hookItUp(sess)
    
    file = open('access_token.dat', 'r')
    accesstkn = file.readline()

    client = client.DropboxClient(sess)
except rest.ErrorResponse:
    sys.exit(1)

try:
    accntinfo = 'linked account:', client.account_info()
    print accntinfo
except rest.ErrorResponse:
    print 'account has already been linked'
    sys.exit(1)
