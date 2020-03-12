"""
this module contains Type wise commands which are of same type
"""
from plutox.msg.parser import *
from plutox.msg.typeConst import *
class MsgType():
    def __init__(self):
        """

        """
        self.parse = Parse()

    def command(self, cmd):
        """
        this method will create command and return it
        :param cmd:
        :return: command
        """
        return self.parse.convert([cmd], MSP_SET_COMMAND)

    def arming(self, arm: bool):
        """
        this will create package for arming and disarming
        :param arm: if True : arm the vehicle, if false disarm it
        :return:
        """
        if arm:
            return self.parse.convert([1500], MSP_SET_RAW_RC)
        else:
            return self.parse.convert([1000], MSP_SET_RAW_RC)

