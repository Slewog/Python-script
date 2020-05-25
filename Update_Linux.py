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


def manage_logs(log_file):
    if not os.path.exists(folder_location):  # Checks if the folder exists
        os.mkdir(folder_location)
    if not os.path.exists(log_file):  # Checks if the file exists
        file = open(log_file, "w+")
        file.close()
    else:  # Otherwise he creates it
        file = open(log_file, "r")
        number_line = len(open(log_file).readlines())
        file.close()
        if number_line > 97:     # If the file is longer than 97 lines we rename it
            os.rename(r'' + logs_file, r'' + logs_file_rename)


def date_organization():
    unorganized_date = datetime.datetime.now()
    date = unorganized_date.strftime("%d-%m-%Y à %H:%M:%S")
    return date


def write_result(log_file, message_return):
    file = open(log_file, "a")
    file.write(message_return + "\n")
    file.close()


manage_logs(logs_file)
for command in [command_update, command_upgrade, command_auto_remove]:
    return_sub_process_run = subprocess.run(command, shell=True)
    return_code = return_sub_process_run.returncode
    date_result = date_organization()
    if return_code == 0:
        message = "OK : " + date_result + ", [" + command + "]"
        write_result(logs_file, message)
    else:
        message = "ERROR !!! " + date_result + ", [" + command + "]"
        write_result(logs_file, message)