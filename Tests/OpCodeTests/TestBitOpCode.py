from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBitOpCode(OpCodeTestBase):

    def test_execute_bit_zero_page_calls_bit_method(self):
        self.assert_opcode_execution(OpCodes.bit_zero_page_command, self.target.get_bit_command_executed)

    def test_execute_bit_absolute_command_calls_bit_method(self):
        self.assert_opcode_execution(OpCodes.bit_absolute_command, self.target.get_bit_command_executed)

