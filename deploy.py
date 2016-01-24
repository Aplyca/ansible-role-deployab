#!/usr/local/bin/python
# Script wrapper to execute ansible commands to release
# Arguments <environment> <version>

import sys, getopt, subprocess

def main(argv):
    environment = ''
    version = '1.0.0'
    environments = ['a', 'b']

    try:
        opts, args = getopt.getopt(argv,"he:v:",["help", "environment=", "version="])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print 'Usage: release.py -e <environment> -v <version>'
                sys.exit()
            elif opt in ("-e", "--environment"):
                environment = arg
            elif opt in ("-v", "--version"):
                version = arg

        if environment not in environments:
            raise Exception('Invalid option for environment, see -h, --help ', environment, environments)

    except Exception as error:
        print error.args
        sys.exit(2)
    except getopt.GetoptError:
        print 'Invalid argumets: deploy.py -e <environment> -v <version>'
        sys.exit(2)

    print 'Releasing version "'+version+'" in environment "'+environment+'"'
    command = "ansible-playbook -i inventories/local playbook.yml  --extra-vars \"env="+environment+" version="+version+"\""
    print 'Executing: "'+command+'"'
    subprocess.call(command, shell=True)

if __name__ == "__main__":
   main(sys.argv[1:])
