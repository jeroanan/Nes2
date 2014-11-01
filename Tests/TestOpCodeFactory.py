import unittest
from Chip import OpCodeDefinitions
from Chip.OpCodeFactory import OpCodeFactory
from Chip.OpCodes.OraCommand import OraCommand


class TestOpCodeFactory(unittest.TestCase):

    def test_create_command(self):
        factory = OpCodeFactory()
        opcode = OpCodeDefinitions.adc_immediate_command
        factory.get_command(opcode)

    def test_factory_ora_indirect_x_command_creates_ora_command(self):
        factory = OpCodeFactory()
        command = factory.get_command(OpCodeDefinitions.ora_indirect_x_command)
        self.assertIsInstance(command, OraCommand)
