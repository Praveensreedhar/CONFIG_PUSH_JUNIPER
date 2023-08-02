import netmiko
import paramiko
from netmiko import ConnectHandler
from netmiko import exceptions
from paramiko.ssh_exception import SSHException
import os
from getpass import getpass, getuser
from tqdm import tqdm
from tqdm import tqdm
import time
from termcolor import colored, cprint

#os.chdir("/AUTOMATION/RE-FILTER/")
os.chdir("C:\\Users\\USER\\Desktop\\SYSLOG")


def get_credentials():
    username = input('Enter username : ')
    #password = None
    #while not password:
    password = getpass('Enter password : ')
    return username, password
    

username, password = get_credentials()
device_type = 'juniper'
devices = open('ip.txt')
row = 0

netmiko_exceptions = (netmiko.exceptions.NetMikoTimeoutException,
                      netmiko.exceptions.NetMikoAuthenticationException,
                      netmiko.exceptions.ReadTimeout)
config_line = input('Enter the config-command : ')
for IP in devices:
    dev = {
        'device_type' : 'juniper',
        'ip' : IP,
        'username' : username,
        'password' : password
              }
    cprint("Connecting to " + IP, 'blue')
    try:
        cprint("Pushing configuration to " + IP, 'green')
        for i in tqdm(range(3)):
            time.sleep(0.2)
        print(config_line)
        connection_1 = ConnectHandler(**dev)
        config_line_push = connection_1.send_config_set(config_line, exit_config_mode=False)
        connection_1.commit()
    except netmiko_exceptions as e:
        cprint("Failed to login/commit..... " + IP, 'red')
