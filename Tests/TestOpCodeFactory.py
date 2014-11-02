import unittest
from unittest.mock import Mock
from Chip import OpCodeDefinitions
from Chip.Chip6502 import Chip6502
from Chip.OpCodeFactory import OpCodeFactory
from Chip.OpCodes.OraCommand import OraCommand


class TestOpCodeFactory(unittest.TestCase):

    def setUp(self):
        chip = Mock(Chip6502)
        self.__factory = OpCodeFactory(chip)

    def test_create_command(self):
        opcode = OpCodeDefinitions.adc_immediate_command
        self.__factory.get_command(opcode)

    def test_factory_ora_indirect_x_command_creates_ora_command(self):
        command = self.__factory.get_command(OpCodeDefinitions.ora_indirect_x_command)
        self.assertIsInstance(command, OraCommand)

    def test_factory_ora_immediate_command_creates_ora_command(self):
        command = self.__factory.get_command(OpCodeDefinitions.ora_immediate_command)
        self.assertIsInstance(command, OraCommand)