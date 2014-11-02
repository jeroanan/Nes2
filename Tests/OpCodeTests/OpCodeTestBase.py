import unittest
from unittest.mock import Mock
from Chip.OpCodeFactory import OpCodeFactory
from Chip.OpCodes.OraCommand import OraCommand
from Tests.Chip6502Spy import Chip6502Spy


class OpCodeTestBase(unittest.TestCase):

    def setUp(self):
        self.target = Chip6502Spy()
        factory = Mock(OpCodeFactory)
        factory.get_command.return_value = OraCommand(self.target)
        self.target.set_opcode_factory(factory)

    def assert_opcode_execution(self, op_code, status_method):
        self.target.execute(op_code)
        self.assertTrue(status_method())

    def assert_overflow_flag_set(self):
        self.assertEqual(0x1, self.target.get_overflow_flag())

    def assert_overflow_flag_clear(self):
        self.assertEqual(0x0, self.target.get_overflow_flag())

    def assert_carry_flag_set(self):
        self.assertEqual(0x1, self.target.get_carry_flag())

    def assert_carry_flag_clear(self):
        self.assertEqual(0x0, self.target.get_carry_flag())

    def assert_zero_flag_set(self):
        self.assertEqual(0x1, self.target.get_zero_flag())

    def assert_zero_flag_clear(self):
        self.assertEqual(0x0, self.target.get_zero_flag())
