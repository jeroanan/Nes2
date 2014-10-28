from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLdyOpCode(OpCodeTestBase):

    def test_ldy_immediate_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_immediate_command, self.target.get_ldy_command_executed)

    def test_ldy_zero_page_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_zero_page_command, self.target.get_ldy_command_executed)

    def test_ldy_absolute_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_absolute_command, self.target.get_ldy_command_executed)

    def test_ldy_zero_page_x_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_zero_page_x_command, self.target.get_ldy_command_executed)

    def test_ldy_absolute_x_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_absolute_x_command, self.target.get_ldy_command_executed)



