from celery import task
from auto_correction.automatic_correction_runner import AutomaticCorrectionRunner
from datetime import datetime


@task
def run_automatic_correction():
    automatic_correction_runner = AutomaticCorrectionRunner()
    result = automatic_correction_runner.run()
    current_timestamp = datetime.today()
    print str(current_timestamp) + " - result: " + str(result)
