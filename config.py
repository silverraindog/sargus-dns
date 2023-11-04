import configparser


parser = configparser.SafeConfigParser(allow_no_value=True)
parser.read('config.ini')  # path of your .ini file
