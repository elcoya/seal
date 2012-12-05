"""

This file exists for the only purpouse of having Django acknowledging the tests

"""

# web tests
from seal.test.integration.autocheckIntegrationTest import AutocheckIntegrationTest
from seal.test.integration.correctionIntegrationTest import CorrectionIntegrationTest
from seal.test.integration.courseIntegrationTest import CourseIntegrationTest
from seal.test.integration.deliveryIntegrationTest import DeliveryIntegrationTest
from seal.test.integration.practiceIntegrationTest import PracticeIntegrationTest
from seal.test.integration.studentIntegrationTest import StudentIntegrationTest
from seal.test.integration.teacherIntegrationTest import TeacherIntegrationTest
from seal.test.unit.deliveryTest import DeliveryTest
from seal.test.unit.correctionTest import CorrectionTest
from seal.test.unit.courseTest import CourseTest
from seal.test.unit.practiceTest import PracticeTest
from seal.test.unit.studentTest import StudentTest
from seal.test.unit.suscriptionTest import SuscriptionTest
from seal.test.unit.teacherTest import TeacherTest

# daemon tests
#from daemon_test.autocheck_runner_test import TestAutocheckRunner
from daemon_test.run_script_command_test import TestRunScriptCommand
from daemon_test.publish_result_visitor_test import PublishResultVisitorTest

