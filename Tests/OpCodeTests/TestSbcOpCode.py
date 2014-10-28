from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSbcOpCode(OpCodeTestBase):
    def test_sbc_indirect_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_indirect_x_command, self.target.get_sbc_command_executed)

    def test_sbc_zero_page_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_zero_page_command, self.target.get_sbc_command_executed)

    def test_sbc_immediate_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_immediate_command, self.target.get_sbc_command_executed)

    def test_sbc_absolute_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_command, self.target.get_sbc_command_executed)

    def test_sbc_indirect_y_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_indirect_y_command, self.target.get_sbc_command_executed)

    def test_sbc_zero_page_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_zero_page_x_command, self.target.get_sbc_command_executed)

    def test_sbc_absolute_y_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_y_command, self.target.get_sbc_command_executed)

    def test_sbc_absolute_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_x_command, self.target.get_sbc_command_executed)
