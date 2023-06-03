#1 - logging

from logexample import ILog
from logging import DEBUG, CRITICAL
try:
    log = ILog("Lesson 8 - logging")
    log.LogData(level=DEBUG)
except Exception as ex:
    print(ex)

