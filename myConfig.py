# save configuration of my python program
# https://stackoverflow.com/questions/15992387/how-to-save-application-settings-in-a-config-file
# https://docs.python.org/3.3/library/configparser.html#module-configparser

import configparser

import myWord
configuration_file_path = 'example.ini'
configuration_file_path = myWord.resource_path(configuration_file_path)
config = configparser.ConfigParser()
config.sections()
config.read(configuration_file_path)

def configuration_file_has_been_persisted():
    #print(config.sections())
    #print('EXCEL' in config)
    return ('EXCEL' in config)

def configuration_file_create_persist():
    print("""
    
    WASAAAAAAAAAAAAAAAAAA
    
    """)
    # config['DEFAULT'] = {'ServerAliveInterval': '45','Compression': 'yes','CompressionLevel': '9'}
    config['EMAIL'] = {'subject': 'Test Subject','body': 'Test Body','body_in_html' : '<p>my test body</p>'}
    
    config['EXCEL'] = {'file': '~tempfile.1.xlsx'}

    config['Automate outlook mailing'] = {'auto_run': False,'time_to_run' : "10",'time_after_run' : 20,'Word_File_Attachement': False,'HTML_format': True}
    
    #config['Automate outlook mailing'] = {'auto_run': False,'time_to_run' : "00:10",'scheduled_time' : "21:00"}
    #config['EXCEL']['file'] = '~tempfile.1.xlsx'


    with open(configuration_file_path, 'w') as configfile:
        config.write(configfile)
    pass

def configuration_file_set_something_to_save(section,key,value):

    config[section][key] = value

    """
    topsecret = config['excel']
    topsecret['file'] = '~tempfile.1.xlsx'

    topsecret = config['email']
    topsecret['subject'] = 'Test Subject'
    topsecret['body'] = 'Test Body'
    topsecret['body_in_html'] = '<p>my test body</p>'
    # myMail.email_send(email,"Hello World","test body body","<p>my test html body</p>",word_file_path)
    # email_send(recipient,subject,body,body_in_html,attachement):
    """
    with open(configuration_file_path, 'w') as configfile:
        config.write(configfile)
    pass

def get_mail_data():
    return config['EMAIL']

def get_saved_data(section,key):

    if section in config:
        if check_data(section,key):
            #print(get_mail_data()[key])
            #get_mail_data()[key]
            print(config[section][key])
            return config[section][key]
        else:
            # print(get_mail_data()[key])
            print("dont work 2")
            print_data(section)
            print(config.sections())
            #print(config[section][key])
            pass
    else:
        print("dont work 1")
        print(config.sections())
        pass


def check_data(section,key):
    #return config[section].getboolean(key)
    print(config[section])
    return (key in config[section])

def print_data(section):
    #return config[section].getboolean(key)
    print(config[section])
    for key in config[section]:
        print(key)
        print(config[section][key])
        pass
    #return (key in config[section])


def getPath(filename):
    import os
    import sys
    from os import chdir
    from os.path import join
    from os.path import dirname
    from os import environ
    
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller >= 1.6
        chdir(sys._MEIPASS)
        filename = join(sys._MEIPASS, filename)
    elif '_MEIPASS2' in environ:
        # PyInstaller < 1.6 (tested on 1.5 only)
        chdir(environ['_MEIPASS2'])
        filename = join(environ['_MEIPASS2'], filename)
    else:
        chdir(dirname(sys.argv[0]))
        filename = join(dirname(sys.argv[0]), filename)
        
    return filename
"""

# save configuration of my python program
# https://stackoverflow.com/questions/15992387/how-to-save-application-settings-in-a-config-file
# https://docs.python.org/3.3/library/configparser.html#module-configparser

import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45','Compression': 'yes','CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)



'bytebong.com' in config

config['bitbucket.org']['User']

config['DEFAULT']['Compression']

topsecret = config['topsecret.server.com']
topsecret['ForwardX11']

topsecret['Port']

for key in config['bitbucket.org']: print(key)

config['bitbucket.org']['ForwardX11']

"""

#

# nuitka --recurse-all --plugin-enable=multiprocessing --prefer-source-code --plugin-enable=pylint-warnings .\main.py


################################################################################
#LOG                        function to log prints
"""
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s %(message)s')

def printandlog(text):
    print(text)
    logging.warning(text)
    pass

"""