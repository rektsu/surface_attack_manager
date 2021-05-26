import os, sys
from shutil import which

#Create project directory and files
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

def create_data_files(project_name, domains_list, credentials_list, white_lists_list):
    domains = project_name + '/domains.txt'
    credentials = project_name + '/credentials.txt'
    white_lists = project_name + '/white_lists.txt'

    if not os.path.isfile(domains):
        write_file(domains, domains_list)
    if not os.path.isfile(credentials):
        write_file(credentials, credentials_list)
    if not os.path.isfile(white_lists):
        write_file(white_lists, white_lists_list)

def write_file(path, data):
    try:
        with open(path, 'w') as f:
            f.write(str([dns for dns in data]))

    except:
        print("Couldnt open file: ", path)

#Check requirements
def check_installations():

    programs = ['python3-pip', 'git', 'pwndb', 'tor', 'zmap']

    for i in range(len(programs)):
        if which(programs[i]) is None:
            option = input(str("You need to install: " + programs[i] + " do you want to install it now? 'y/yes' | 'n/no' "))
            if option == 'y' or option == 'yes':
                if programs[i] == 'pwndb':
                    try:
                        os.system("git clone https://github.com/davidtavarez/pwndb")
                        os.system("cd pwndb")
                        os.system("pip install requirements.txt")
                    except:
                        print("Error trying to install " + programs[i] + " ",sys.exc_info()[0], " occurred, check https://github.com/davidtavarez/pwndb for more details on the instalation")
                        return 0

                else:
                    try:
                        os.system("sudo apt-get install " + programs[i] + " -y")
                    except:
                        print("Error trying to install " + programs[i] + " ",sys.exc_info()[0], " occurred, check " + programs[i] + " installation for more details")
                        return 0


            elif option == 'n' or option == 'no':
                print('Need to install missing programs: ' + programs[i])
                return 0
            else:
                print("Option not contemplated, please try again using 'y/yes | n/no'.")
                return 0
