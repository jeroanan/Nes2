from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestStxOpCode(OpCodeTestBase):

    def test_stx_absolute_command_calls_stx_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.stx_absolute_command, self.target.get_stx_command_executed)

    def test_stx_zero_page_y_command_calls_stx_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.stx_zero_page_y_command, self.target.get_stx_command_executed)

    def test_stx_zero_page_command_calls_stx_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.stx_zero_page_command, self.target.get_stx_command_executed)
