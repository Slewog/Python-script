#!/usr/bin/python3.8
import os
import subprocess
import datetime
import getpass

username = getpass.getuser()
folder_location = "/home/" + username + "/Log Update"
command_update = " sudo apt-get --yes update"
command_upgrade = " sudo apt-get --yes upgrade"
command_auto_remove = " sudo apt-get --yes autoremove"
date_log = datetime.datetime.today().strftime('%d-%b-%Y')
logs_file = folder_location + "/" + "Log_Upgrade_Local.txt"
logs_file_rename = folder_location + "/" + "Log_Upgrade_Local_" + date_log + ".txt"


# Function to manage the log file.
def manage_logs(log_file):
    # Check if the folder does not exist.
    if not os.path.exists(folder_location):
        # If it does not exist create it.
        os.mkdir(folder_location)
    # Check if the file does not exist.
    if not os.path.exists(log_file):
        # If it does not exist create it.
        file = open(log_file, "w+")
        file.close()
    # otherwise open it.
    else:
        file = open(log_file, "r")
        number_line = len(open(log_file).readlines())
        file.close()
        # Check if the number of lines is greater than 97.
        if number_line > 97:
            # If so, rename the file.
            os.rename(r'' + logs_file, r'' + logs_file_rename)


# Function to organize the date.
def date_organization():
    unorganized_date = datetime.datetime.now()
    date = unorganized_date.strftime("%d-%m-%Y à %H:%M:%S")
    return date


# Function to write result in log file.
def write_result(log_file, message_return):
    file = open(log_file, "a")
    file.write(message_return + "\n")
    file.close()


# Main code.
manage_logs(logs_file)
for command in [command_update, command_upgrade, command_auto_remove]:
    return_sub_process_run = subprocess.run(command, shell=True)
    return_code = return_sub_process_run.returncode
    date_result = date_organization()
    # Check the return code.
    if return_code == 0:
        message = "OK : " + date_result + ", [" + command + "]"
        write_result(logs_file, message)
    else:
        message = "ERROR !!! " + date_result + ", [" + command + "]"
        write_result(logs_file, message)
