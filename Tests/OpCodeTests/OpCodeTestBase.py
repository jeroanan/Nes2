import unittest
from Tests.Chip6502Spy import Chip6502Spy


class OpCodeTestBase(unittest.TestCase):

    def setUp(self):
        self.target = Chip6502Spy()

    def assert_opcode_execution(self, op_code, status_method):
        self.target.execute(op_code)
        self.assertTrue(status_method())
