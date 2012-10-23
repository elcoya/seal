'''
Created on 19/10/2012

@author: anibal
'''
from __future__ import with_statement
from fabric.api import local
from fabric.context_managers import lcd
from subprocess import Popen

import ConfigParser, os
import sys
config = ConfigParser.ConfigParser()
config.readfp(open('conf/local.cfg'))

class FabricContext:
    server_process = None

def launch_server(context):
    print("fabric: launching server instance for feature tests.")
    context.server_process = Popen(["python", "seal/manage.py", "runserver", "--noreload"])
    print("fabric: server online... pid: " + str(context.server_process.pid))

def kill_server(context):
    print("fabric: killing server...")
    context.server_process.terminate()
    print("fabric: server killed...")

def prepare_db(context = None):
    print("fabric: preparing database.")
    user = config.get("Database", "user")
    passwd = config.get("Database", "pass")
    if(config.get("Enviroment", "location") == "travis"):
        print("Travis location detected. Seting up database layout...")
        cmd = "mysql -e 'create database seal;' -u " + user
        if(passwd != ""):
            cmd += " -p'" + passwd + "'"
        local(cmd)
        cmd = "mysql -u " + user
        if(passwd != ""):
            cmd += " -p'" + passwd + "'"
        local(cmd + " < ci_scripts/ci_dbuser.sql")
        print("Layout set.")
    else:
        print("Environment detected. No need to create either database user nor schema.")
    print("Sincronizing DB...")
    output = local("mysql -u " + user + " -D seal -e 'show tables;' -r -N -p'" + passwd + "' | sed s/[^a-z_]\+// | grep -v auth | grep -v django", capture=True)
    local_cmd = "mysql -u " + user + " -D seal -e '"
    local_cmd += "SET foreign_key_checks = 0; "
    local_cmd += "DROP TABLE IF EXISTS " + ",".join(output.splitlines()) +" CASCADE; "
    local_cmd += "SET foreign_key_checks = 1;"
    local_cmd += "' -p'" + passwd + "'"
    local(local_cmd)
    local("python seal/manage.py syncdb")
    print("syncdb complete")

def run_tests(context = None):
    print("fabric: invoking tests.")
    local("python seal/manage.py test")

def run_features_tests(context = None):
    launch_server(context)
    print("fabric: invoking feature testing.")
    with lcd("featureTest"):
        local("behave")
    kill_server(context)

def prepare_deploy(context = None):
    prepare_db(context)
    # run_tests(context)
    run_features_tests(context)

def invoke_test_deploy(context = None):
    if(config.get("Enviroment", "location") == "travis"):
        print("fabric: tests run successfully... deploying to test instance.")
        local("wget http://ixion-tech.com.ar/seal/requestUpdate.php")

def run():
    ctxt = FabricContext()
    prepare_deploy(ctxt)
    invoke_test_deploy(ctxt)
