'''
Created on 19/10/2012

@author: anibal
'''
from __future__ import with_statement
from fabric.api import local
from fabric.context_managers import lcd

import ConfigParser, os
config = ConfigParser.ConfigParser()
config.readfp(open('conf/local.cfg'))

def prepare_db():
    print("fabric: preparing database.")
    user = config.get("Database", "user")
    passwd = config.get("Database", "pass")
    if(config.get("Enviroment", "location") == "travis"):
        print("Travis location detected. Seting up database layout...")
        cmd = "mysql -e 'create database seal;' -u " + user
        if(passwd != ""):
            cmd += " -p" + passwd
        local(cmd)
        cmd = "mysql -u " + user
        if(passwd != ""):
            cmd += " -p" + passwd
        local(cmd + " < ci_scripts/ci_dbuser.sql")
        print("Layout set.")
    else:
        print("Environment detected. No need to create either database user nor schema.")

def run_tests():
    print("fabric: invoking tests.")
    local("python seal/manage.py test")

def run_features_tests():
    print("fabric: invoking feature testing.")
    with lcd("featureTest"):
        local("behave")

def prepare_deploy():
    prepare_db()
    run_tests()
    run_features_tests()

def invoke_test_deploy():
    if(config.get("Enviroment", "location") == "travis"):
        print("fabric: tests run successfully... deploying to test instance.")
        local("wget http://ixion-tech.com.ar/seal/requestUpdate.php")

def run():
    prepare_deploy()
    invoke_test_deploy()
