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

    def test_execute_ora_immediate_opcode_executes_ora_command(self):
        factory = Mock(OpCodeFactory)
        ora_command = Mock(OraCommand)
        factory.get_command.return_value = ora_command
        chip = Chip6502()
        chip.set_opcode_factory(factory)
        chip.execute(OpCodeDefinitions.ora_immediate_command)
        self.assertTrue(ora_command.execute.called)










