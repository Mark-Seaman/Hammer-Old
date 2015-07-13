from os import system

def settings_test():
    from settings import BASE_DIR,LOG_DIR,DOC_ROOT,SCRIPTS_DIR
    print "BASE_DIR", BASE_DIR
    print "LOG_DIR",  LOG_DIR
    print "DOC_ROOT", DOC_ROOT
    print "SCRIPTS_DIR", SCRIPTS_DIR

def local_settings_test():
    from local_settings import username,password
    print "username",username
    print "password",password


def cat_settings_test():
    system('cat settings.py')
    system('cat local_settings.py')
