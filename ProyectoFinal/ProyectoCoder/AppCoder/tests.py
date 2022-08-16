from django.test import TestCase
import unittest

class LogType:
    """ Tipo de registro en URL. Reference https://stackoverflow.com/a/18471309/4956124 ."""
    ADB, TEST_SCRIPT, DBUS, UNIT_TEST, ALL = [1, 2, 4, 8, 1 | 2 | 4 | 8]

    @staticmethod
    def isAdbLog(flag):
        """ Verifique si el indicador de registro de Adb está configurado."""
        return (flag & LogType.ADB) == LogType.ADB

    @staticmethod
    def isTestScriptLog(flag):
        """ Verifique si el indicador de registro del script de prueba está establecido"""
        return (flag & LogType.TEST_SCRIPT) == LogType.TEST_SCRIPT

    @staticmethod
    def isDbusLog(flag):
        """ Verifique si el indicador de registro de Dbus está establecido.."""
        return (flag & LogType.DBUS) == LogType.DBUS

    @staticmethod
    def isUnitTestLog (flag):
        """ Verifique si el indicador de registro de prueba de unidad está establecido."""
        return (flag & LogType.UNIT_TEST) == LogType.UNIT_TEST
