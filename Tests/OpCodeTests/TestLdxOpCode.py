from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLdxOpCode(OpCodeTestBase):

    def test_ldx_immediate_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_immediate_command, self.target.get_ldx_command_executed)

    def test_ldx_zero_page_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_zero_page_command, self.target.get_ldx_command_executed)

    def test_ldx_absolute_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_absolute_command, self.target.get_ldx_command_executed)

    def test_ldx_zero_page_y_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_zero_page_y_command, self.target.get_ldx_command_executed)

    def test_ldx_absolute_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.ldx_absolute_y_command, self.target.get_ldx_command_executed)




