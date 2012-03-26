#The config file for gsync
#Vivek Karuturi

import ConfigParser
import StringIO


defaults = '''
[sync]
interval=180

'''

conf = ConfigParser.SafeConfigParser()

def loadDefaults(defaultSett):
    conf.readfp(StringIO.StringIO(defaultSett))

def config_init(conf_file = 'gsync.conf'):
    loadDefaults(defaults)
    conf.read(conf_file)
    
