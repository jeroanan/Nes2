import unittest
from unittest.mock import Mock
from Chip import OpCodeDefinitions
from Chip.Chip6502 import Chip6502
from Chip.OpCodeFactory import OpCodeFactory
from Chip.OpCodes.OraCommand import OraCommand


class Test6502(unittest.TestCase):

    def test_execute_command_executes_opcode_factory_get_command(self):
        factory = Mock(OpCodeFactory)
        chip = Chip6502()
        chip.set_opcode_factory(factory)
        chip.execute(0x13)
        self.assertTrue(factory.get_command.called)

    def setUp(self):
        factory = Mock(OpCodeFactory)
        self.__target = Mock(OraCommand)
        factory.get_command.return_value = self.__target
        self.__chip = Chip6502()
        self.__chip.set_opcode_factory(factory)

    def test_execute_ora_immediate_opcode_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_immediate_command)

    def test_execute_ora_indirect_x_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_indirect_x_command)

    def test_execute_ora_zero_page_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_zero_page_command)

    def test_execute_ora_absolute_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_absolute_command)

    def test_execute_ora_indirect_y_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_indirect_y_command)

    def test_execute_ora_zero_page_x_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_zero_page_x_command)

    def test_execute_ora_absolute_y_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_absolute_y_command)

    def test_execute_ora_ora_absolute_x_command_executes_ora_command(self):
        self.__assert_opcode_calls_command(OpCodeDefinitions.ora_absolute_x_command)

    def __assert_opcode_calls_command(self, opcode):
        self.__chip.execute(opcode)
        self.assertTrue(self.__target.execute.called)







