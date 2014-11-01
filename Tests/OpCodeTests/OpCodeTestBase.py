import unittest
from Tests.Chip6502Spy import Chip6502Spy


class OpCodeTestBase(unittest.TestCase):

    def setUp(self):
        self.target = Chip6502Spy()

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
