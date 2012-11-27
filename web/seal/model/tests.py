"""

This file exists for the only purpouse of having Django acknowledging the tests

"""

from seal.test.integration.courseTest import CourseTest
from seal.test.integration.studentTest import StudentTest
from seal.test.integration.practiceTest import PracticeTest
from seal.test.integration.deliveryTest import DeliveryTest
from seal.test.integration.correctionTest import CorrectionTest
from seal.test.integration.teacherTest import TeacherTest
from seal.test.integration.autocheckTest import AutocheckTest

from seal.test.unit.courseTest import CourseTest
from seal.test.unit.studentTest import StudentTest
from seal.test.unit.practiceTest import PracticeTest
from seal.test.unit.deliveryTest import DeliveryTest
from seal.test.unit.teacherTest import TeacherTest
from seal.test.unit.suscriptionTest import SuscriptionTest