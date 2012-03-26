#The config file for gsync
#Vivek Karuturi

import ConfigParser
import StringIO


defaults = '''
[sync]
time=180

'''

conf = ConfigParser.SafeConfigParser()
conf.readfp(StringIO.StringIO(defaults))



