from os.path import join,dirname

# Location of app directory
BASE_DIR    = dirname(dirname(dirname(__file__)))
LOG_DIR     = join(BASE_DIR, 'logs')
DOC_ROOT    = join(BASE_DIR, 'app', 'user_doc')
SCRIPTS_DIR = join(BASE_DIR, 'app', 'scripts')
