from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestStyOpCode(OpCodeTestBase):

    def test_sty_zero_page_command_calls_sty_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sty_zero_page_command, self.target.get_sty_command_executed)

    def test_sty_absolute_command_calls_sty_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sty_absolute_command, self.target.get_sty_command_executed)

    def test_sty_zero_page_x_command_calls_sty_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sty_zero_page_x_command, self.target.get_sty_command_executed)