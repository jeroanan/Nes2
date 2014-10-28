from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestDecOpCode(OpCodeTestBase):
    def test_dec_absolute_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_absolute_command, self.target.get_dec_command_executed)

    def test_dec_zero_page_x_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_zero_page_x_command, self.target.get_dec_command_executed)

    def test_dec_absolute_x_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_absolute_x_command, self.target.get_dec_command_executed)

    def test_dec_zero_page_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_zero_page_command, self.target.get_dec_command_executed)
