'''
Created on 19/10/2012

@author: anibal
'''
from fabric.api import local

def prepare_db():
    local("mysql -e 'create database seal;'")
    local("mysql -u root < ci_scripts/ci_dbuser.sql")

def run_tests():
    local("python seal/manage.py test")

def prepare_deploy():
    prepare_db()
    run_tests()

def invoke_test_deploy():
    local("wget http://ixion-tech.com.ar/seal/requestUpdate.php")

def run():
    prepare_deploy()
    invoke_test_deploy()
