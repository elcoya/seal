"""
Created on 19/10/2012

@author: anibal

Fabric file. This file imports the necessary modules and sets up the enviroment
to be able to perform all the tasks intended for fabric.
"""
from __future__ import with_statement
from fabric.api import local, settings
from fabric.context_managers import lcd
from subprocess import Popen
import ConfigParser, os, sys, time
from fileinput import close
from fabric.state import env

project_base_path = os.path.realpath(os.path.dirname(__file__))
WEB_PATH = project_base_path + "/web/"
DAEMON_PATH = project_base_path + "/daemon/"
MODEL_PATH = project_base_path + "/web/seal/"
sys.path.append(WEB_PATH)           # Required to use the app model
sys.path.append(DAEMON_PATH)
sys.path.append(MODEL_PATH)         # Fixes 'No module named model'
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'
os.environ['PROJECT_PATH'] = project_base_path + "/"

import seal.settings
USER = seal.settings.USER
PASSWORD = seal.settings.PASSWORD


class FabricContext:
    """
    Context class to transfer information from one call to another.
    """
    server_process = None


def set_pythonpath():
    os.environ["PYTHONPATH"] = WEB_PATH + ":" + DAEMON_PATH + ":" + MODEL_PATH
    print "PYTHONPATH set to : \"" + os.environ["PYTHONPATH"] + "\""


# launch and kill server instance to run feature tests
def launch_server(context):
    """
    Launches the test instance of the application server in a separate process
    to run_travis the feature tests.
    """
    print("[fabric] launching server instance for feature tests.")
    set_pythonpath()
    context.server_process = Popen(["python", "web/seal/manage.py", "runserver", "--noreload"])
    print("[fabric] server online... pid: " + str(context.server_process.pid))

def kill_server(context):
    """
    Terminates the tests instance of the application server. It is supposed to
    be called after running the feature tests.
    """
    print("[fabric] killing server...")
    context.server_process.terminate()
    print("[fabric] server killed...")


# Database access utility funtions
def get_mysql_bash(user=None, password=None):
    """
    Builds the string that should be used to call a command over the database.
    It is used to include the username and password to access the service. This
    command would allow you to connect to de database, if you want to invoke a
    given sql command, use get_mysql_bash_cmd.
    """
    if(user is None):
        user = USER
    if(password is None):
        password = PASSWORD
    
    local_cmd = "mysql -u " + user
    if (password != ""):
        local_cmd += " -p'" + password + "'"
    return local_cmd

def get_mysql_bash_cmd(sql_sentence = "SHOW TABLES;", database = None, user=None, password=None):
    """
    Builds the string that should be used to call a command over the database
    with a given sql command. It uses the configuration given in the local.conf
    file.
    """
    if(user is None):
        user = USER
    if(password is None):
        password = PASSWORD
    local_cmd = "mysql -e \"" + sql_sentence + "\" -u " + user
    if (database is not None and database != ""):
        local_cmd += " -D " + database + " "
    if (password != ""):
        local_cmd += " -p'" + password + "' "
    return local_cmd

def create_super_user():
    """
    After the database is flushed and syncronized, it is necessary to create a
    user to access the admin site. Teachers can be created from the admin site
    and Students register themselves.
    """
    set_pythonpath()
    from django.contrib.auth.models import User
    try:
        admin_user = User.objects.get_by_natural_key('seal')
        print "Super user already exists: " + str(admin_user)
    except:
        u = User.objects.create(
            username='seal',
            first_name='Seal',
            last_name='Administrator',
            email='seal@gmail.com',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        u.set_password('seal')
        u.save()
        print "User account created"

def populate_database():
    """
    After the database is cleaned up, it is necessary to create a set of objects to be able to try out the 
    developed features. A Teacher, a Student, a Course, 2 Practices, 2 Deliveries for each practice with
    their corresponding AutomaticCorrections will be created with basic information.
    """
    set_pythonpath()
    from django.contrib.auth.models import User
    from seal.model.teacher import Teacher
    from seal.model.student import Student
    from seal.model.course import Course
    from seal.model.practice import Practice
    from seal.model.delivery import Delivery
    from seal.model.automatic_correction import AutomaticCorrection
    from seal.model.suscription import Suscription
    from seal.model.innings import Innings

    try:
        admin_user = User.objects.get_by_natural_key('seal')
        print "Super user already exists: " + str(admin_user)
    except:
        u = User.objects.create(
            username='seal',
            first_name='Seal',
            last_name='Administrator',
            email='seal@gmail.com',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        u.set_password('seal')
        u.save()
        print "User account created"
    
    DELIVERY_FILE_PATH = os.path.join(os.path.dirname(__file__), "workspace", "delivery_files")
    PRACTICE_FILE_PATH = os.path.join(os.path.dirname(__file__), "workspace", "practice_files")
    if(os.path.exists(DELIVERY_FILE_PATH)):
        local("rm -r " + DELIVERY_FILE_PATH)
    if(os.path.exists(PRACTICE_FILE_PATH)):
        local("rm -r " + PRACTICE_FILE_PATH)
    local("mkdir " + DELIVERY_FILE_PATH)
    local("mkdir " + PRACTICE_FILE_PATH)
    local("cp web/feature_test/data/pdftest.pdf " + PRACTICE_FILE_PATH)
    local("cp web/feature_test/data/delivery.zip " + DELIVERY_FILE_PATH)
    local("cp web/feature_test/data/delivery-2.zip " + DELIVERY_FILE_PATH)
    local("cp web/feature_test/data/delivery-3.zip " + DELIVERY_FILE_PATH)
    
    teacher_user = User.objects.get_or_create(username="teacher", email='sealteacher@gmail.com', 
                                              first_name="teacher name", last_name="Auto Teacher")[0]
    teacher_user.set_password("teacher")
    teacher_user.save()
    teacher = Teacher.objects.get_or_create(uid="teacher", appointment="teacher", user=teacher_user)[0]
    student_user = User.objects.get_or_create(username="student", email='sealstudent@gmail.com', 
                                              first_name="student name", last_name="Auto Student")[0]
    student_user.set_password("student")
    student_user.save()
    student = Student.objects.get_or_create(user=student_user, uid="student", corrector=teacher)[0]
    course = Course.objects.get_or_create(name="2013-1C")[0]
    inning = Innings.objects.get_or_create(name="Noche", description="Horario", course=course)[0] 
    student.innings.add(inning)
    student.save()
    
    practice_1 = Practice.objects.get_or_create(uid="TP Auto 1", course=course, deadline="2013-04-01")[0]
    practice_2 = Practice.objects.get_or_create(uid="TP Auto 2", course=course, deadline="2013-04-20")[0]
    delivery_1_1 = Delivery.objects.get_or_create(deliverDate="2013-03-21", file=os.path.join(DELIVERY_FILE_PATH,"delivery.zip"), practice=practice_1, student=student)[0]
    delivery_1_2 = Delivery.objects.get_or_create(deliverDate="2013-03-25", file=os.path.join(DELIVERY_FILE_PATH,"delivery-2.zip"), practice=practice_1, student=student)[0]
    delivery_2_1 = Delivery.objects.get_or_create(deliverDate="2013-04-10", file=os.path.join(DELIVERY_FILE_PATH,"delivery.zip"), practice=practice_2, student=student)[0]
    delivery_2_2 = Delivery.objects.get_or_create(deliverDate="2013-04-18", file=os.path.join(DELIVERY_FILE_PATH,"delivery-3.zip"), practice=practice_2, student=student)[0]
    AutomaticCorrection.objects.get_or_create(captured_stdout="automatically generated standard output:\n\nFAILURE", delivery=delivery_1_1, exit_value=1, status=-1)[0]
    AutomaticCorrection.objects.get_or_create(captured_stdout="automatically generated standard output:\n\nSUCCESS", delivery=delivery_1_2, exit_value=0, status= 1)[0]
    AutomaticCorrection.objects.get_or_create(captured_stdout="automatically generated standard output:\n\nFAILURE", delivery=delivery_2_1, exit_value=1, status=-1)[0]
    AutomaticCorrection.objects.get_or_create(captured_stdout="automatically generated standard output:\n\nSUCCESS", delivery=delivery_2_2, exit_value=0, status= 1)[0]


def create_and_prepare_db(context = None):
    """
    Resets the database applying the latests changes made in the app model.
    """
    print("[fabric] creating and preparing database.")
    print("Travis location detected. Seting up database layout...")
    cmd = get_mysql_bash_cmd(sql_sentence = "create database seal;", user='root', password='')
    local(cmd)
    cmd = get_mysql_bash(user='root', password='')
    local(cmd + " < build_files/ci_grant_privileges_in_travis_db.sql")
    print("Layout set.")
    with lcd("web"):
        local("python seal/manage.py syncdb --noinput")
    create_super_user()
    print("syncdb complete")


def prepare_db(context = None):
    """
    Resets the database applying the latests changes made in the app model.
    """
    print("[fabric] preparing database.")
    print("Sincronizing DB...")
    cmd = get_mysql_bash_cmd(sql_sentence = "SHOW TABLES;", database = "seal")
    output = local(cmd + " -N ", capture=True)
    if (output != ""):
        mysql_cmd = "SET foreign_key_checks = 0; "
        mysql_cmd += "DROP TABLE IF EXISTS " + ",".join(output.splitlines()) +" CASCADE; "
        mysql_cmd += "SET foreign_key_checks = 1;"
        cmd = get_mysql_bash_cmd(sql_sentence = mysql_cmd, database = "seal")
        local(cmd)
    with lcd("web"):
        local("python seal/manage.py syncdb --noinput")
    create_super_user()
    print("syncdb complete")

def syncdb(contest = None):
    with lcd("web"):
        local("python seal/manage.py syncdb")
    print("syncdb complete")

def compile_messages(contest = None):
    with lcd("web/seal"):
        local("python manage.py compilemessages")
    print("compile messages complete")

# Running test
def run_tests(context = None):
    """Runs the application tests for the Django app"""
    print("[fabric] invoking tests.")
    with lcd("web"):
        local("python seal/manage.py test")

def run_features_tests(context = None):
    """
    Runs the feature tests. Launches the server before running the tests, and
    kills it after
    """
    launch_server(context)
    print("[fabric] invoking feature testing.")
    with lcd("web/feature_test"):
        local("behave")
    kill_server(context)



# Coverage analysis
def run_html_coverage_analysis(context = None):
    """Invokes the test coverage analysis and generates the reports"""
    set_pythonpath()
    with lcd("web"):
        local("coverage run seal/manage.py test model")
        local("coverage html")

def run_plain_report_coverage_analysis(context = None):
    """Invokes the test coverage analysis and generates the reports"""
    set_pythonpath()
    with lcd("web"):
        local("coverage run seal/manage.py test model")
        local("coverage report")


# Pylint check
def pylint():
    """Runs the pylint analysis and saves the report to be available"""
    print "launching pylint static analysis..."
    set_pythonpath()
    with settings(warn_only=True):
        result = local("pylint web/seal daemon/auto_correction --rcfile=pylintrc > pylint_report/pylint.html")
    print "pylint static analysis complete... exit status: " + str(result.return_code)
    print "you can access the report result pylint_report/pylint.html"


# to be invoked from the development enviroment
def runfullcheck():
    ctxt = FabricContext()
    prepare_db(ctxt)
    test()
    run_features_tests(ctxt)
    run_html_coverage_analysis()


# to call the test update and deploy process and should be used from travis
def invoke_test_deploy(context = None):
    """Calls a url in the test server to update the test instance"""
    print("[fabric] tests run_travis successfully... deploying to test instance.")
    local("wget http://ixion-tech.com.ar/seal/requestUpdate.php")
    local("cat requestUpdate.php")

def runtravis():
    """Main command for the fabric run_travis"""
    ctxt = FabricContext()
    create_and_prepare_db(ctxt)
    test()
    # This line is called to rise the flag in the test server to activate the update and deploy of the changes
    # invoke_test_deploy(ctxt)
    run_plain_report_coverage_analysis()


def start():
    print("[fabric] launching server instance.")
    print("[fabric] Compiling Messages.")
    compile_messages()
    set_pythonpath()
    server_process = Popen(["nohup", "python", "web/seal/manage.py", "runserver", "--noreload"], stdout = open("output.txt", 'w+', 0), env=os.environ)
    local("echo " + str(server_process.pid) + " > /tmp/seal_server.pid")
    print("[fabric] server online... pid: " + str(server_process.pid))


def start_ip(ip):
    print("[fabric] launching server instance.")
    compile_messages()
    set_pythonpath()
    server_process = Popen(["nohup", "python", "web/seal/manage.py", "runserver", str(ip) + ":8000", "--noreload"], stdout = open(os.devnull, 'w+', 0), env=os.environ)
    local("echo " + str(server_process.pid) + " > /tmp/seal_server.pid")
    print("[fabric] server online... pid: " + str(server_process.pid))

def start_web(host='localhost', port='8000'):
    print("[fabric] launching server instance.")
    compile_messages()
    set_pythonpath()
    server_process = Popen(["nohup", "python", "web/seal/manage.py", "runserver", host + ":" + port, "--noreload"], stdout = open(os.devnull, 'w+', 0), env=os.environ)
    local("echo " + str(server_process.pid) + " > /tmp/seal_server.pid")
    print("[fabric] server online... pid: " + str(server_process.pid))

def stop():
    file = open("/tmp/seal_server.pid")
    line = file.readline()
    local("kill -2 " + line)
    file.close()
    os.remove("/tmp/seal_server.pid")

def start_daemon(host='localhost', port='8000'):
    set_pythonpath()
    with lcd("daemon/auto_correction"):
        os.environ['REST_API_BASE_URL'] = "http://" + host + ":" + port
        local("python daemon_control.py start")

def stop_daemon():
    set_pythonpath()
    with lcd("daemon/auto_correction"):
        os.environ['REST_API_BASE_URL'] = ''
        local("python daemon_control.py stop")

def start_daemon_dbg():
    set_pythonpath()
    with lcd("daemon/auto_correction"):
        pdb.set_trace()
        local("python daemon_control.py start")

def test(app_name=''):
    set_pythonpath()
    with lcd("web/seal"):
        local("python manage.py test " + app_name)

def behave():
    set_pythonpath()
    with lcd("web/feature_test"):
        local("behave")

def feature(arg):
    """It runs all behave features which contains te arg value"""
    set_pythonpath()
    with lcd("web/feature_test"):
        local("behave -i " + arg)
