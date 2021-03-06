"""
Persist TM1Service in a file.
Helps to avoid (unreasonably slow) CAM Authentication
"""
import time
from TM1py.Services import TM1Service
import configparser

config = configparser.ConfigParser()
# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config.read(r'..\config.ini')


# Connect to TM1
tm1 = TM1Service(**config['tm1srv01'])
print(tm1.server.get_server_name())
# Save TM1Service instance to file
tm1.save_to_file('tm1_connection')

# Wait...
time.sleep(7)

# Restore TM1Service instance from file
tm1 = TM1Service.restore_from_file('tm1_connection')
print(tm1.server.get_server_name())

# Logout
tm1.logout()
